from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

count = 0

vector_store_id = os.getenv("OPENAI_VECTOR_STORE_ID")

data = client.vector_stores.files.list(vector_store_id)

while data.has_more and len(data.data) > 0:
    for file in data.data:
        count += 1
        print(f"File[{count}] deleted")
        client.vector_stores.files.delete(
            vector_store_id=vector_store_id,
            file_id=file.id
        )
    data = client.vector_stores.files.list(vector_store_id)

print(f"Total files deleted: {count}")

count = 0
delete_files = client.files.list().data
if len(delete_files) > 0:
    for file in delete_files:
        count += 1
        print(f"File[{count}] {file.filename} deleted")
        client.files.delete(file.id)
else:
    print("No files to delete")

print(f"Total files deleted: {count}")

