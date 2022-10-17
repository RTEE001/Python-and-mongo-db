from dotenv import load_dotenv
import os
from mongoengine import Document, connect, IntField, StringField, disconnect

load_dotenv()
HOST = os.getenv("HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")


def connect_to_database():
    connect(DATABASE_NAME, host=HOST)


connect_to_database()


class Visitor(Document):

    visitor_name = StringField(max_length=200, required=True)
    visitor_age = IntField(min_value=0, max_value=125)
    date_of_visit = StringField(max_length=200, required=True)
    time_of_visit = StringField(max_length=200, required=True)
    assistant = StringField(max_length=200, required=True)
    comments = StringField(max_length=400, required=True)

    meta = {"strict": False}


disconnect()
