import os
from dotenv import load_dotenv

load_dotenv("./.env")

KEY = "USERNAME1"

username1 = os.getenv(KEY, None)
username2 = os.environ.get(KEY, None)

print(username2)
