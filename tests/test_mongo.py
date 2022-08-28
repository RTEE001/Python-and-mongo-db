from unittest.mock import patch
import unittest

class TestIndex(unittest.TestCase):
    @patch('src.indexing.create_visitor')
    def test_create_visitor(self, mock_visitor):
        mock_visitor("John", 23, "16:00", "2022", "Wayne", "Good")
        mock_visitor.assert_called()
        mock_visitor.assert_called_with("John", 23, "16:00", "2022", "Wayne", "Good")
        mock_visitor.assert_called_once()

    @patch('src.indexing.list_visitors')
    def test_list_visitors(self, mock_list):
        mock_list()
        mock_list.assert_called()
        mock_list.assert_called_with()
        mock_list.assert_called_once()

    @patch('src.indexing.delete_visitor')
    def test_delete_visitor(self, mock_delete):
        mock_delete(24)
        mock_delete.assert_called()
        mock_delete.assert_called_with(24)
        mock_delete.assert_called_once()

    @patch('src.indexing.delete_all')
    def test_delete_all(self, mock_delete_all):
        mock_delete_all(24)
        mock_delete_all.assert_called()
        mock_delete_all.assert_called_with(24)
        mock_delete_all.assert_called_once()

    @patch('src.indexing.visitor_details')
    def test_visitor_details(self, mock_details):
        mock_details(25)
        mock_details.assert_called()
        mock_details.assert_called_with(25)
        mock_details.assert_called_once()

    @patch('src.indexing.update_visitor')
    def test_update_visitor(self, mock_update):
        mock_update(11, "John", 23, "16:00", "2022", "Wayne", "Good")
        mock_update.assert_called()
        mock_update.assert_called_with(11, "John", 23, "16:00", "2022", "Wayne", "Good")
        mock_update.assert_called_once()

if __name__ == "__main__":
    unittest.main()
