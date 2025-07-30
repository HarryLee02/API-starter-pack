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
    
    # Disable OpenAI HTTP request logs
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)
    
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
    print(logger.info("="*100))
    print('''
                      __
                 /\\  |__) |
                /~~\\ |    |

                         __  ___       __  ___  ___  __
                        /__`  |   /\\  |__)  |  |__  |__)
                        .__/  |  /~~\\ |  \\  |  |___ |  \\

                                     __        __
                                    |__)  /\\  /  ` |__/
                                    |    /~~\\ \\__, |  \\
''')
    print(logger.info("="*100))

if __name__ == "__main__":
    menu()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    vector_store_id = os.getenv("OPENAI_VECTOR_STORE_ID")
    url = os.getenv("SUPPORT_URL")

    client = OpenAI(api_key=openai_api_key)

    total_articles = 0
    skipped_articles = 0
    updated_articles = 0
    new_articles = 0

    articles_per_category = {}
    update_file_path = []
    old_ids_to_delete = []
    new_update_ids = []
    
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
            print(logger.info(f"[+] Directory './docs/{category['name']}' created successfully!"))
        except FileExistsError:
            logger.info(f"[-] Directory './docs/{category['name']}' already exists.")
        except Exception as e:
            logger.error(f"[-] An error occurred: {e}")
            continue

        logger.info("-"*100)

        with open(f"./docs/{category['name']}/articles.json", "w", encoding="utf-8") as f:
            data = requests.get(url+f"/categories/{category['id']}/articles").json()
            articles_per_category[category["name"]] = data["count"]

            print(logger.info(f"[+] Fetching articles from {data['page']}..."))
            articles = data["articles"]

            if data["next_page"] is not None:
                while data["next_page"] is not None:
                    print(logger.info(f"[+] Fetching articles from {data['next_page']}..."))
                    data = requests.get(data["next_page"]).json()
                    articles.extend(data["articles"])

            json.dump(articles, f, ensure_ascii=False)
            f.close()
            
        for article in articles:
            article["title"] = re.sub(r'\s*[^A-Za-z0-9]\s*', " ", article["title"]).strip()
            article["title"] = re.sub(r' ', "-", article["title"])

            if not os.path.exists(f"./docs/{category['name']}/updated_at.json"):
                with open(f"./docs/{category['name']}/updated_at.json", "w", encoding="utf-8") as f:
                    print(logger.info(f"[+] First updated_at.json created"))
                    json.dump({article["id"]: article["updated_at"]}, f, ensure_ascii=False)
                    f.close()
                with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as f:
                    f.write(markdown.markdown(article["body"]))
                    f.close()
                
                try:
                    response = client.files.create(
                        file=open(f"./docs/{category['name']}/{article['title']}.md", "rb"),
                        purpose="assistants"
                    )

                    print(logger.info(f"[+] ADDED: New article '{article['title']}'"))
                    new_articles += 1

                    client.vector_stores.files.create(
                        vector_store_id=vector_store_id,
                        file_id=response.id,
                        chunking_strategy={
                            "type": "static",
                            "static": {
                                "max_chunk_size_tokens": 1200,
                                "chunk_overlap_tokens": 300    
                            }
                        }
                    )
                    print(logger.info(f"[+] File '{response.id}' attached to Vector Store successfully!"))

                except Exception as e:
                    print(logger.error(f"[-] An OpenAI error occurred: {e}"))

            else:
                with open(f"./docs/{category['name']}/updated_at.json", "r", encoding="utf-8") as f:
                    old_updated_at = json.load(f)
                    f.close()
                
                if str(article["id"]) not in old_updated_at:
                    with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as updated_file:
                        updated_file.write(markdown.markdown(article["body"]))
                        updated_file.close()
                    old_updated_at[article["id"]] = article["updated_at"]

                    try:
                        response = client.files.create(
                            file=open(f"./docs/{category['name']}/{article['title']}.md", "rb"),
                            purpose="assistants"
                        )
                        print(logger.info(f"[+] ADDED: New article '{article['title']}'"))
                        new_articles += 1

                        client.vector_stores.files.create(
                            vector_store_id=vector_store_id,
                            file_id=response.id,
                            chunking_strategy={
                                "type": "static",
                                "static": {
                                    "max_chunk_size_tokens": 1200,
                                    "chunk_overlap_tokens": 300    
                                }
                            }
                        )
                        print(logger.info(f"[+] File '{response.id}' attached to Vector Store successfully!"))
                    except Exception as e:
                        print(logger.error(f"[-] An OpenAI error occurred: {e}"))

                elif datetime.strptime(old_updated_at[str(article["id"])], "%Y-%m-%dT%H:%M:%SZ") < datetime.strptime(article["updated_at"], "%Y-%m-%dT%H:%M:%SZ"):

                    with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as updated_file:
                        updated_file.write(markdown.markdown(article["body"]))
                        updated_file.close()

                    print(logger.info(f"[+] UPDATED: Article '{article['title']}'"))
                    old_updated_at[article["id"]] = article["updated_at"]
                    updated_articles += 1

                    update_file_path.append({"file_name": f"{article['title']}.md",
                                       "file_path": f"./docs/{category['name']}/{article['title']}.md"})

                else:
                    skipped_articles += 1
                    print(logger.info(f"[-] SKIPPED: Article '{article['title']}'"))

                with open(f"./docs/{category['name']}/updated_at.json", "w", encoding="utf-8") as f:
                    json.dump(old_updated_at, f, ensure_ascii=False)
                    f.close()

            total_articles += 1
        print(logger.info("="*100))

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

    if len(update_file_path) > 0:
        for file in current_list:
            for update_file in update_file_path:
                if file.filename == update_file["file_name"]:
                    old_ids_to_delete.append(file.id)
                    break
        
        for id in old_ids_to_delete:
            client.files.delete(id)
            print(logger.info(f"[+] Deleted file '{id}'"))
        for file in update_file_path:
            new_update_ids.append(client.files.create(
                file=open(file["file_path"], "rb"),
                purpose="assistants"
            ).id)
            print(logger.info(f"[+] Added file '{file['file_name']}'"))
        
    logger.info("[+] Updated files successfully!")

    logger.info("[+] Attach updated files to Vector Store")

    for id in old_ids_to_delete:
        try:
            client.vector_stores.files.delete(vector_store_id=vector_store_id, file_id=id)
            logger.info(f"[+] File '{id}' deleted from Vector Store successfully!")
        except Exception as e:
            logger.error(f"[-] An OpenAI error occurred: {e}")
    
    for id in new_update_ids:
        try:
            client.vector_stores.files.create(
                vector_store_id=vector_store_id,
                file_id=id,
                chunking_strategy={
                    "type": "static",
                    "static": {
                        "max_chunk_size_tokens": 1200,
                        "chunk_overlap_tokens": 300    
                    }
                }
            )
            logger.info(f"[+] File '{id}' updated to Vector Store successfully!")
        except Exception as e:
            logger.error(f"[-] An OpenAI error occurred: {e}")

    logger.info("[+] Task completed!")
    exit()