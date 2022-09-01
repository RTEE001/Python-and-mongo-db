import unittest
from mongoengine import connect, disconnect
from src.mongo_db import *
from pymongo import MongoClient


class TestVisitor(unittest.TestCase):
    
    def test_create_visitor(self):
        visitor = create_visitor("John", 22, "20-06-2022", "17:00", "James", "Good")
        test_visitor = Visitor.objects().first()
        assert test_visitor.visitor_name ==  'John'

    def test_visitor_details(self):
       
        first_object = Visitor.objects.first()
        assert first_object.id ==visitor_details(first_object.id)["id"]
        assert first_object.visitor_name ==visitor_details(first_object.id)["visitor_name"]
        assert first_object.visitor_age ==visitor_details(first_object.id)["visitor_age"]
        assert first_object.date_of_visit ==visitor_details(first_object.id)["date_of_visit"]
        assert first_object.time_of_visit ==visitor_details(first_object.id)["time_of_visit"]
        assert first_object.comments ==visitor_details(first_object.id)["comments"]


    # def test_delete_visitor(self):
    #     visitor = create_visitor("Loki", 22, "20-06-2022", "18:00", "Thor", "Good")
    #     visitor_object = Visitor.objects.visitor
    #     # delete_visitor(visitor_object["id"])
        assert visitor_object not in Visitor.objects

    def test_delete_all(self):
        delete_all()
        assert len(Visitor.objects())==0


if __name__ == "__main__":
    unittest.main()