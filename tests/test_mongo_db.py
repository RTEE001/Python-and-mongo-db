from unittest import mock
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

@mock.patch("pymongo.collection.Collection.find")
def test_name(self, mock_create_visitor):
    mock_create_visitor.return_value = {
        "visitor_name":"Victor",
        "visitor_age":27,
        "date_of_visit":"2019-02-02",
        "time_of_visit":"17:00",
        "assistant":"John",
        "comments":'great person',
        }
    self.assertEqual(mock_create_visitor, visitor_details("Victor",27,"2019-02-02",17,"John",'great person'))


if __name__ == "__main__":
    test_name()
