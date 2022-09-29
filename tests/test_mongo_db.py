from unittest import mock
from mongoengine import connect, disconnect
import unittest
from src.mongo_functions import (
    Visitor,
    create_visitor,
    visitor_details,
    list_visitors,
    update_visitor,
    delete_visitor,
    delete_all,
)
class TestVisitor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
       disconnect()
    
    def test_create_visitor(self):
        visitor = Visitor(visitor_name="Victor",
        visitor_age=27,
        date_of_visit="2019-02-02",
        time_of_visit="17:00",
        assistant="John",
        comments='great person')
        visitor.save()
        fresh_pers = Visitor.objects().first()
        self.assertEqual(fresh_pers.visitor_name, "Victor")

    def test_update_visitor(self):
        create_visitor("Chuck", 22, "20-06-2022", "20:00", "Grace", "Good")
        
        id = Visitor.objects.filter(visitor_name = "Chuck")[0]
        update_visitor(id, "James", 22, "20-06-2022", "21:00", "Grace", "Good")
        self.assetEquals(Visitor.objects.filter(id = id).visitor_name, "James")

    def test_delete_visitor(self):
        create_visitor("Loki", 22, "20-06-2022", "18:00", "Thor", "Good")
        self.assertTrue(len(Visitor.objects.filter(visitor_name = "Loki"))==1)
        delete_visitor(Visitor.objects().first().id)
        self.assertTrue(len(Visitor.objects.filter(visitor_name = "Loki"))==0)
     
      
    def test_delete_all(self):
        self.assertNotEqual(len(Visitor.objects()), 0)
        delete_all()
        self.assertEqual(len(Visitor.objects()), 0)
if __name__ == "__main__":
    unittest.main()
