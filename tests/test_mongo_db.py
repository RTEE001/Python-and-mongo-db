import unittest
from src.mongo_db import (
    Visitor,
    create_visitor,
    visitor_details,
    list_visitors,
    update_visitor,
    delete_visitor,
    delete_all,
)


class TestVisitor(unittest.TestCase):
    def test_create_visitor(self):
        visitor_present = False
        create_visitor("John", 22, "20-06-2022", "17:00", "James", "Good")

        for visitor_object in Visitor.objects:
            if visitor_object.visitor_name == "John":
                visitor_present = True
        self.assertTrue(visitor_present)

    def test_visitor_details(self):

        for visitor_object in Visitor.objects:
            self.assertEqual(
                visitor_object.id, visitor_details(visitor_object.id)["id"]
            )
            self.assertEqual(
                visitor_object.visitor_name,
                visitor_details(visitor_object.id)["visitor_name"],
            )
            self.assertEqual(
                visitor_object.visitor_age,
                visitor_details(visitor_object.id)["visitor_age"],
            )
            self.assertEqual(
                visitor_object.date_of_visit,
                visitor_details(visitor_object.id)["date_of_visit"],
            )
            self.assertEqual(
                visitor_object.time_of_visit,
                visitor_details(visitor_object.id)["time_of_visit"],
            )
            self.assertEqual(
                visitor_object.comments, visitor_details(visitor_object.id)["comments"]
            )

    def test_list_visitors(self):
        visitors = []
        for visitor_object in Visitor.objects:
            visitors.append(
                {"id": visitor_object.id, "name": visitor_object.visitor_name}
            )
        self.assertEqual(visitors, list_visitors())

    def test_update_visitor(self):
        create_visitor("Chuck", 22, "20-06-2022", "20:00", "Grace", "Good")
        id = []
        for visitor_object in Visitor.objects:
            if visitor_object.visitor_name == "Chuck":
                id.append(visitor_object.id)
                update_visitor(
                    id[0], "This was chuck", 22, "20-06-2022", "21:00", "Grace", "Good"
                )
                break
        changed_name = False
        for visitor_object in Visitor.objects:
            if visitor_object.visitor_name == "This was chuck":
                changed_name = True
        self.assertTrue(changed_name)

    def test_delete_visitor(self):
        create_visitor("Loki", 22, "20-06-2022", "18:00", "Thor", "Good")
        deleted = False
        id = []
        for visitor_object in Visitor.objects:
            if visitor_object.visitor_name == "Loki":
                id.append(visitor_object.id)
                delete_visitor(id[0])
                deleted = True
                break
        self.assertTrue(deleted)

    def test_delete_all(self):
        delete_all()
        self.assertEqual(len(Visitor.objects()), 0)


if __name__ == "__main__":
    unittest.main()
