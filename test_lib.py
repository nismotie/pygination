import unittest
from lib import Paginator


class TestLib(unittest.TestCase):

    def setUp(self):
        self.paginator1 = Paginator(['item1', 'item2', 'item3', 'item4', 'item5'], 2)
        self.paginator2 = Paginator(list(range(1, 54)), 8)
        self.paginator3 = Paginator(list(range(1, 25)), 6)


    def tearDown(self):
        pass

    def test_init_attrs(self):
        self.assertEqual(self.paginator1.content, ['item1', 'item2', 'item3', 'item4', 'item5'])
        self.assertEqual(self.paginator1.items_per_page, 2)

    valid_content = ['a', 'b', 'c', 'd', 'e', 'f']

    def test_init_empty_content(self):
        self.assertRaises(ValueError, Paginator, [], 10)

    def test_init_zero_pages(self):
        self.assertRaises(ValueError, Paginator, self.valid_content, 0)
        
    def test_init_negative_pages(self):
        self.assertRaises(ValueError, Paginator, self.valid_content, -10)

    def test_num_items(self):
        self.assertEqual(self.paginator1.num_items(), 5)

    def test_num_pages(self):
        self.assertEqual(self.paginator2.num_pages(), 7)
        self.assertEqual(self.paginator3.num_pages(), 4)


    def test_page_item_count(self):
        self.assertEqual(self.paginator2.page_item_count(5), 8)
        self.assertEqual(self.paginator2.page_item_count(6), 5)


if __name__ == "__main__":
    unittest.main()
