from mongoengine import Document, connect, IntField, StringField
from dotenv import load_dotenv
import os


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


def create_visitor(name, age, date, time, assistant, comments):
    visitor = Visitor(
        visitor_name=name,
        visitor_age=age,
        date_of_visit=date,
        time_of_visit=time,
        assistant=assistant,
        comments=comments,
    )
    visitor.save()


def list_visitors():
    visitors = []
    for visitor in Visitor.objects:
        visitors.append({"name": visitor.visitor_name, "id": visitor.id})

    return visitors


def delete_visitor(id):
    Visitor.objects(id=id).delete()


def delete_all():

    for visitor in Visitor.objects:
        id = visitor.id
        delete_visitor(id)


def visitor_details(id):
    for visitor in Visitor.objects(id=id):
        return {
            "id": visitor.id,
            "visitor_name": visitor.visitor_name,
            "visitor_age": visitor.visitor_age,
            "date_of_visit": visitor.date_of_visit,
            "time_of_visit": visitor.time_of_visit,
            "assistant": visitor.assistant,
            "comments": visitor.comments,
        }


def update_visitor(id, name, age, date, time, assistant, comments):

    visitor = Visitor.objects(id=id).first()
    visitor.update(
        visitor_name=name,
        visitor_age=age,
        date_of_visit=date,
        time_of_visit=time,
        assistant=assistant,
        comments=comments,
    )
    visitor.save()
