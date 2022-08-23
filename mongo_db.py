from mongoengine import connect, Document, ListField, StringField
from dotenv import load_dotenv
import os

load_dotenv()
PORT = int(os.getenv("PORT"))
HOST = os.getenv("HOST")


connect (db = 'UmuziProspects', host = HOST, port = PORT  )

# class Visitor(Document):
#     visitor_name = StringField(max_length=50)
#     visitor_age = StringField(max_length=50)
#     date_of_visit = StringField(max_length=50)
#     date_of_visit = StringField(max_length=50)
#     time_of_visit = StringField(max_length=50)
#     name_of_assistant = StringField(max_length=50)
#     comments = StringField(max_length=50)

