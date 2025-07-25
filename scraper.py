import requests
import json
import markdown
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# GET /api/v2/help_center/categories/{category_id}/articles
# GET /api/v2/help_center/categories/
class Colors:
    GREEN = "\033[1;92m"
    YELLOW = "\033[1;93m"
    RED = "\033[1;91m"
    BLUE = "\033[1;94m"
    RESET = "\033[0m"
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
    articles_per_category = {}
    url = os.getenv("SUPPORT_URL")

    with open("./categories.json", "w", encoding="utf-8") as f:
        json.dump(requests.get(url+"/categories").json(), f, ensure_ascii=False)
        f.close()

    print(Colors.log("Categories loaded successfully!", Colors.GREEN))

    with open("./categories.json", "r", encoding="utf-8") as f:
        f_json = json.load(f)
        f.close()

    print(Colors.log("="*100, Colors.YELLOW))

    if not os.path.exists("./docs"):
        os.mkdir("./docs")
        print(Colors.log(f"[+] Directory './docs' not found, created successfully!", Colors.BLUE))
    else:
        print(Colors.log(f"[+] Directory './docs' found, skipping creation.", Colors.BLUE))

    for category in f_json["categories"]:
        category["name"] = re.sub(r'\s*[/\:?*<>"|]\s*', " ", category["name"])
        category["name"] = re.sub(r' ', "-", category["name"])
        try:
            os.mkdir(f"./docs/{category['name']}")
            print(Colors.log(f"[+] Directory './docs/{category['name']}' created successfully!", Colors.BLUE))
        except FileExistsError:
            print(Colors.log(f"[-] Directory './docs/{category['name']}' already exists.", Colors.BLUE))
        except Exception as e:
            print(Colors.log(f"[-] An error occurred: {e}", Colors.RED))
            continue

        print(Colors.log("="*100, Colors.YELLOW))

        with open(f"./docs/{category['name']}/articles.json", "w", encoding="utf-8") as f:
            articles = requests.get(url+f"/categories/{category['id']}/articles").json()["articles"]
            articles_per_category[category["name"]] = len(articles)
            json.dump(articles, f, ensure_ascii=False)
            f.close()
            
        for article in articles:
            article["title"] = re.sub(r'\s*[/\:?*<>"|]\s*', " ", article["title"])
            article["title"] = re.sub(r' ', "-", article["title"])

            with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as f:
                f.write(markdown.markdown(article["body"]))
                f.close()
            print(Colors.log(f"[+] Article '{article['title']}' saved successfully!", Colors.GREEN))
            try:
                client.files.create(
                    file=open(f"./docs/{category['name']}/{article['title']}.md", "rb"),
                    purpose="assistants"
                )
            except Exception as e:
                print(Colors.log(f"[-] An OpenAI error occurred: {e}", Colors.RED))

            total_articles += 1
        print(Colors.log("-"*100, Colors.YELLOW))

    print(Colors.log(f"[+] Task completed!", Colors.GREEN))
    print(Colors.log(f"[+] Total articles: {total_articles}", Colors.GREEN))

    print(Colors.log("-"*100, Colors.YELLOW))

    print(Colors.log("Articles per category:", Colors.GREEN))
    for category, articles in articles_per_category.items():
        print(Colors.log(f"[+] {category}: {articles}", Colors.GREEN))

    print(Colors.log("-"*100, Colors.YELLOW))

    print(Colors.log("[+] Attach files to Vector Store", Colors.GREEN))

    vector_store_id= os.getenv("OPENAI_VECTOR_STORE_ID")
    
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
            print(Colors.log(f"[-] An OpenAI error occurred: {e}", Colors.RED))

    print(Colors.log("[+] Files attached to Vector Store successfully!", Colors.GREEN))

    exit()