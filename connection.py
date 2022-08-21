from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
PORT = int(os.getenv("PORT"))
HOST = os.getenv("HOST")


client = MongoClient(host = HOST, port = PORT)
db = client["UmuziProspects"]
visitor = db["visitor"]

first_visitor = {
    "visitor_name": "Victor",
    "visitor_age": 20,
    "date_of_visit": "2022-08-10",
    "time_of_visit": "17:00",
    "name_of_assistant": "Will",
    "comments": "None"
}
