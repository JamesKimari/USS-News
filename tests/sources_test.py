import unittest
from app.models import Source

class SourcesTest(unittest.TestCase):
    """
    Test Case to test the behavior of the sources class
    """
    def setUp(self):
        """
        setUp method that will run before every test
        """
        self.new_sources = Source("abc-news","ABC News", "abcnews.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Source))

if __name__ == '__main__':
    unittest.main()
    