import unittest
from lib import Paginator


class TestLib(unittest.TestCase):

    def setUp(self):
        self.paginator = Paginator(['item1', 'item2', 'item3', 'item4', 'item5'], 2)

    def tearDown(self):
        pass

    def test_init_attrs(self):
        self.assertEqual(self.paginator.content, ['item1', 'item2', 'item3', 'item4', 'item5'])
        self.assertEqual(self.paginator.items_per_page, 2)

    valid_content = ['a', 'b', 'c', 'd', 'e', 'f']

    def test_init_empty_content(self):
        self.assertRaises(ValueError, Paginator, [], 10)

    def test_init_zero_pages(self):
        self.assertRaises(ValueError, Paginator, self.valid_content, 0)
        
    def test_init_negative_pages(self):
        self.assertRaises(ValueError, Paginator, self.valid_content, -10)


if __name__ == "__main__":
    unittest.main()
