from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


try:
    a = client.files.create(
        file=open(f"README.md", "rb"),
        purpose="assistants"
    ).id
    print(a)
except Exception as e:
    print(f"[-] An OpenAI error occurred: {e}")
