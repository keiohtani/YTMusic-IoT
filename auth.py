import dotenv
import os

dotenv.load_dotenv(verbose=True)

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
TOPIC = os.getenv("TOPIC")
USERNAME = os.getenv("USERNAME")
