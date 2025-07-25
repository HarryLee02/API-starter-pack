import requests
import json
import markdown
import os
import re

# I want to create a script capable of :
# scrape the articles based on the category
# auto make dirs based on the category
# auto make files based on the article inside the category

# GET /api/v2/help_center/categories/{category_id}/articles

class Colors:
    GREEN = "\033[1;92m"
    YELLOW = "\033[1;93m"
    RED = "\033[1;91m"
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
    total_articles = 0
    url = "https://support.optisigns.com/api/v2/help_center"

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
        print(Colors.log(f"[+] Directory './docs' not found, created successfully!", Colors.GREEN))
    else:
        print(Colors.log(f"[+] Directory './docs' found, skipping creation.", Colors.YELLOW))

    for category in f_json["categories"]:
        category["name"] = re.sub(r'\s*[/\:?*<>"|]\s*', " ", category["name"])
        category["name"] = re.sub(r' ', "-", category["name"])
        try:
            os.mkdir(f"./docs/{category['name']}")
            print(Colors.log(f"[+] Directory './docs/{category['name']}' created successfully!", Colors.GREEN))
        except FileExistsError:
            print(Colors.log(f"[-] Directory './docs/{category['name']}' already exists.", Colors.YELLOW))
        except Exception as e:
            print(Colors.log(f"[-] An error occurred: {e}", Colors.RED))
            continue

        print(Colors.log("="*100, Colors.YELLOW))

        with open(f"./docs/{category['name']}/articles.json", "w", encoding="utf-8") as f:
            articles = requests.get(url+f"/categories/{category['id']}/articles").json()["articles"]
            json.dump(articles, f, ensure_ascii=False)
            f.close()
            
        for article in articles:
            article["title"] = re.sub(r'\s*[/\:?*<>"|]\s*', " ", article["title"])
            article["title"] = re.sub(r' ', "-", article["title"])

            with open(f"./docs/{category['name']}/{article['title']}.md", "w", encoding="utf-8") as f:
                f.write(markdown.markdown(article["body"]))
                f.close()
            print(Colors.log(f"Article '{article['title']}' saved successfully!", Colors.GREEN))
            total_articles += 1
        print(Colors.log("="*100, Colors.YELLOW))

    print(Colors.log(f"Task completed!", Colors.GREEN))
    print(Colors.log(f"Total articles: {total_articles}", Colors.GREEN))

    exit()



        

    


