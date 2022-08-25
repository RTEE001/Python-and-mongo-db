
from mongoengine import Document, connect, IntField, StringField
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE = os.getenv('DATABASE')
def connect_to_database():
    connect(DATABASE)
    print("connected")
connect_to_database()

class UmuziProspects(Document):
    id = IntField(auto_incriment = True, primary_key = True )
    visitor_name = StringField(max_length=200, required=True)
    visitor_age = IntField(min_value=0, max_value=125)
    date_of_visit =  StringField(max_length=200, required=True)
    time_of_visit =  StringField(max_length=200, required=True)
    assistant = StringField(max_length=200, required=True)
    comments = StringField(max_length=400, required=True)

    # def __init__(self, visitor_name, visitor_age, date_of_visit, time_of_visit, assistant, comments):
    #     self.visitor_name = visitor_name
    #     self.visitor_age = visitor_age
    #     self.date_of_visit = date_of_visit
    #     self.time_of_visit = time_of_visit
    #     self.assistant = assistant
    #     self.comments = comments


