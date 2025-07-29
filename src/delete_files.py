from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

count = 0

for file in client.files.list().data:
    count += 1
    print(f"File[{count}] {file.filename} deleted")
    client.files.delete(file.id)

print(f"Total files deleted: {count}")

