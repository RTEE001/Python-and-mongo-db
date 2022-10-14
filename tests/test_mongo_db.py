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
        visitor = create_visitor("Victor", 27, "2019-02-02", "17:00", "John",'great person')
        self.assertEqual(Visitor.objects.all().first().visitor_name, "Victor")

    def test_update_visitor(self):
        visitor = Visitor(visitor_name="Chuck",
        visitor_age=22,
        date_of_visit="20-06-2022",
        time_of_visit="20:00",
        assistant="Grace",
        comments="Good")
        visitor.save()     
        id = Visitor.objects.filter(visitor_name = "Chuck")[0].id
        update_visitor(id, "James", 22, "20-06-2022", "21:00", "Grace", "Good")
        self.assertEqual(Visitor.objects.filter(id = id)[0].visitor_name, "James")

    def test_visitor_details(self):
        visitor = Visitor(visitor_name="Louis",
        visitor_age=32,
        date_of_visit="25-06-2022",
        time_of_visit="23:00",
        assistant="Graca",
        comments="Good mate")
        visitor.save()     
        id = Visitor.objects.filter(visitor_name = "Louis")[0].id
        visitor_by_code = Visitor.objects.filter(id = id)[0]
        visitor_by_function = visitor_details(id)
        self.assertEqual(visitor_by_code.visitor_name, visitor_by_function["visitor_name"])
        self.assertEqual(visitor_by_code.visitor_age, visitor_by_function["visitor_age"])
        self.assertEqual(visitor_by_code.time_of_visit, visitor_by_function["time_of_visit"])
        self.assertEqual(visitor_by_code.date_of_visit, visitor_by_function["date_of_visit"])
        self.assertEqual(visitor_by_code.assistant, visitor_by_function["assistant"])
        self.assertEqual(visitor_by_code.comments, visitor_by_function["comments"])

    def test_delete_visitor(self):
        visitor = Visitor(visitor_name="Loki",
        visitor_age=22,
        date_of_visit="22-06-2022",
        time_of_visit="18:00",
        assistant="Thor",
        comments="Great")
        visitor.save() 
        self.assertTrue(len(Visitor.objects.filter(visitor_name = "Loki"))==1)
        delete_visitor(Visitor.objects().first().id)
        self.assertTrue(len(Visitor.objects.filter(visitor_name = "Loki"))==0)
     
      
    def test_delete_all(self):
        self.assertNotEqual(len(Visitor.objects()), 0)
        delete_all()
        self.assertEqual(len(Visitor.objects()), 0)

    def test_list_visitors(self):
        visitor1 = Visitor(visitor_name="Travis",
        visitor_age=33,
        date_of_visit="25-07-2022",
        time_of_visit="03:00",
        assistant="Tree",
        comments="bad mate")
        visitor1.save()


        visitor2 = Visitor(visitor_name="John",
        visitor_age=23,
        date_of_visit="25-09-2022",
        time_of_visit="08:00",
        assistant="Slim",
        comments="bad soulmate")
        visitor2.save()

        visitors = []
        for visitor in Visitor.objects:
            visitors.append({"name": visitor.visitor_name, "id": visitor.id})

        self.assertEqual(visitors, list_visitors())

if __name__ == "__main__":
    unittest.main()
