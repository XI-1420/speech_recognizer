import unittest
from .util import utils

data = "two words"


class TestingUtilMethods(unittest.TestCase):
    def test_total_words_in_file(self):
        total = utils.total_words(data)
        self.assertEqual(total, 2)


if __name__ == "__main__":
    main()
