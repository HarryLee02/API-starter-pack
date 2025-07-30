from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
vector_store_id = os.getenv("OPENAI_VECTOR_STORE_ID")

try:
    a = client.files.create(
        file=open(f"README.md", "rb"),
        purpose="assistants"
    ).id
    print(a)
except Exception as e:
    print(f"[-] An OpenAI error occurred: {e}")

try:
    client.vector_stores.files.create(
        vector_store_id=vector_store_id,
        file_id="file-DLybiMPF3S93QXkAhGTgm2",
        chunking_strategy={
            "type": "static",
            "static": {
                "max_chunk_size_tokens": 1200,
                "chunk_overlap_tokens": 300    
            }
        }
    )
    client.vector_stores.files.delete(vector_store_id=vector_store_id, file_id="file-DLybiMPF3S93QXkAhGTgm2")
    print(f"[+] File 'file-DLybiMPF3S93QXkAhGTgm2' deleted from Vector Store successfully!")
except Exception as e:
    print(f"[-] An OpenAI error occurred: {e}")