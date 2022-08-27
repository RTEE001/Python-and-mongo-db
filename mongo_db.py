from mongoengine import Document, connect, IntField, StringField
from dotenv import load_dotenv
import os

load_dotenv()


URL = os.getenv("URL")


def connect_to_database():
    connect(db="UmuziProspects", host="mongodb://localhost:27017")


connect_to_database()


class Visitor(Document):
    id = IntField(AUTO_INCREMENT=True, primary_key=True)
    visitor_name = StringField(max_length=200, required=True)
    visitor_age = IntField(min_value=0, max_value=125)
    date_of_visit = StringField(max_length=200, required=True)
    time_of_visit = StringField(max_length=200, required=True)
    assistant = StringField(max_length=200, required=True)
    comments = StringField(max_length=400, required=True)

    meta = {"strict": False}
