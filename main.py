import requests
import json
import markdown
import os
import re
import logging
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Setup logging
def setup_logging():
    """Setup logging to both file and console"""
    # Create logs directory if it doesn't exist
    if not os.path.exists("./logs"):
        os.mkdir("./logs")
    
    # Configure logging
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler('./logs/scraper.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

# Initialize logger
logger = setup_logging()

# GET /api/v2/help_center/categories/{category_id}/articles
# GET /api/v2/help_center/categories/
class Colors:
    GREEN = "\033[1;92m"
    YELLOW = "\033[1;93m"
    RED = "\033[1;91m"
    BLUE = "\033[1;94m"
    RESET = "\033[0m"
    GRAY = "\033[1;90m"
    def log(text, color):
        return f"{color}{text}{Colors.RESET}" 

def menu():
    print(Colors.log("="*100, Colors.YELLOW))
    print("""
                      __
                 /\  |__) |
                /~~\ |    |

                         __  ___       __  ___  ___  __
                        /__`  |   /\  |__)  |  |__  |__)
                        .__/  |  /~~\ |  \  |  |___ |  \

                                     __        __
                                    |__)  /\  /  ` |__/
                                    |    /~~\ \__, |  \
""")
    print(Colors.log("="*100, Colors.YELLOW))

if __name__ == "__main__":
    menu()

    openai_api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=openai_api_key)

    total_articles = 0
    skipped_articles = 0
    updated_articles = 0
    new_articles = 0
    articles_per_category = {}
    update_ids=[]
    
    url = os.getenv("SUPPORT_URL")

    with open("./categories.json", "w", encoding="utf-8") as f:
        json.dump(requests.get(url+"/categories").json(), f, ensure_ascii=False)
        f.close()

    logger.info("Categories loaded successfully!")

    with open("./categories.json", "r", encoding="utf-8") as f:
        f_json = json.load(f)
        f.close()

    logger.info("="*100)

    if not os.path.exists("./docs"):
        os.mkdir("./docs")
        logger.info("[+] Directory './docs' not found, created successfully!")
    else:
        logger.info("[+] Directory './docs' found, skipping creation.")

    for category in f_json["categories"]:

        category["name"] = re.sub(r'\s*[/\:?*<>"|]\s*', " ", category["name"])
        category["name"] = re.sub(r' ', "-", category["name"])
        try:
            os.mkdir(f"./docs/{category['name']}")
            print(Colors.log(f"[+] Directory './docs/{category['name']}' created successfully!", Colors.BLUE))
        except FileExistsError:
            logger.info(f"[-] Directory './docs/{category['name']}' already exists.")
        except Exception as e:
            logger.error(f"[-] An error occurred: {e}")
            continue

        logger.info("="*100)

        with open(f"./docs/{category['name']}/articles.json", "w", encoding="utf-8") as f:
            data = requests.get(url+f"/categories/{category['id']}/articles").json()
            articles_per_category[category["name"]] = data["count"]

            print(Colors.log(f"[+] Fetching articles from {data['page']}...", Colors.GRAY))
            articles = data["articles"]

            if data["next_page"] is not None:
                while data["next_page"] is not None:
                    print(Colors.log(f"[+] Fetching articles from {data['next_page']}...", Colors.GRAY))
                    data = requests.get(data["next_page"]).json()
                    articles.extend(data["articles"])

            json.dump(articles, f, ensure_ascii=False)
            f.close()
            
        for article in articles:
            article["title"] = re.sub(r'\s*[^A-Za-z0-9]\s*', " ", article["title"]).strip()
            article["title"] = re.sub(r' ', "-", article["title"])

            if not os.path.exists(f"./docs/{category['name']}/updated_at.json"):
                with open(f"./docs/{category['name']}/updated_at.json", "w", encoding="utf-8") as f:
                    print(Colors.log(f"[+] First updated_at.json created", Colors.GREEN))
                    json.dump({article["id"]: article["updated_at"]}, f, ensure_ascii=False)
                    f.close()
                with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as f:
                    f.write(markdown.markdown(article["body"]))
                    f.close()
                print(Colors.log(f"[+] ADDED: New article '{article['title']}'", Colors.GREEN))
                new_articles += 1


                # Create file in OpenAI
                try:
                    response = client.files.create(
                        file=open(f"./docs/{category['name']}/{article['title']}.md", "rb"),
                        purpose="assistants"
                    )
                except Exception as e:
                    print(Colors.log(f"[-] An OpenAI error occurred: {e}", Colors.RED))

            else:
                with open(f"./docs/{category['name']}/updated_at.json", "r", encoding="utf-8") as f:
                    old_updated_at = json.load(f)
                    f.close()
                
                if str(article["id"]) not in old_updated_at:
                    with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as updated_file:
                        updated_file.write(markdown.markdown(article["body"]))
                        updated_file.close()
                    print(Colors.log(f"[+] ADDED: New article '{article['title']}'", Colors.GREEN))
                    old_updated_at[article["id"]] = article["updated_at"]
                    new_articles += 1
                    
                    # Create file in OpenAI
                    try:
                        response = client.files.create(
                            file=open(f"./docs/{category['name']}/{article['title']}.md", "rb"),
                            purpose="assistants"
                        )
                    
                    except Exception as e:
                        print(Colors.log(f"[-] An OpenAI error occurred: {e}", Colors.RED))

                elif datetime.strptime(old_updated_at[str(article["id"])], "%Y-%m-%dT%H:%M:%SZ") < datetime.strptime(article["updated_at"], "%Y-%m-%dT%H:%M:%SZ"):

                    with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as updated_file:
                        updated_file.write(markdown.markdown(article["body"]))
                        updated_file.close()

                    print(Colors.log(f"[+] UPDATED: Article '{article['title']}'", Colors.YELLOW))
                    old_updated_at[article["id"]] = article["updated_at"]
                    updated_articles += 1

                    update_ids.append({"file_name": f"{article['title']}.md",
                                       "file_path": f"./docs/{category['name']}/{article['title']}.md"})

                else:
                    skipped_articles += 1
                    print(Colors.log(f"[-] SKIPPED: Article '{article['title']}'", Colors.GRAY))

                with open(f"./docs/{category['name']}/updated_at.json", "w", encoding="utf-8") as f:
                    json.dump(old_updated_at, f, ensure_ascii=False)
                    f.close()

            total_articles += 1
        print(Colors.log("-"*100, Colors.YELLOW))

    logger.info(f"[+] Task completed!")
    logger.info(f"[+] Total articles: {total_articles}")
    logger.info(f"[+] New articles: {new_articles}")
    logger.info(f"[+] Updated articles: {updated_articles}")
    logger.info(f"[-] Skipped articles: {skipped_articles}")

    logger.info("-"*100)

    logger.info("Articles per category:")
    for category, articles in articles_per_category.items():
        logger.info(f"[+] {category}: {articles}")

    logger.info("-"*100)

    current_list = client.files.list().data

    ids_to_delete = []

    if len(update_ids) > 0:
        for file in current_list:
            if file.filename in update_ids:
                ids_to_delete.append(file.id)
        
        for id in ids_to_delete:
            client.files.delete(id)
        
        for file in update_ids:
            client.files.create(
                file=open(file["file_path"], "rb"),
                purpose="assistants"
            )
        
    logger.info("[+] Updated files successfully!")

    logger.info("[+] Attach files to Vector Store")

    vector_store_id = os.getenv("OPENAI_VECTOR_STORE_ID")
    
    for file in client.files.list().data:
        try:
            client.vector_stores.files.create(
                vector_store_id=vector_store_id,
                file_id=file.id,
                chunking_strategy={
                    "type": "static",
                    "static": {
                        "max_chunk_size_tokens": 1200,
                        "chunk_overlap_tokens": 300    
                    }
                }
            )
        except Exception as e:
            logger.error(f"[-] An OpenAI error occurred: {e}")

    logger.info("[+] Files attached to Vector Store successfully!")
    logger.info("[+] Task completed!")
    exit()