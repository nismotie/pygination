import unittest
from lib import Paginator


class TestLib(unittest.TestCase):
    valid_content = ['a', 'b', 'c', 'd', 'e', 'f']

    def test_init_empty_content(self):
        self.assertRaises(ValueError, Paginator, [], 10)

    def test_init_zero_pages(self):
        self.assertRaises(ValueError, Paginator, self.valid_content, 0)
        
    def test_init_negative_pages(self):
        self.assertRaises(ValueError, Paginator, self.valid_content, -10)

if __name__ == "__main__":
    unittest.main()
