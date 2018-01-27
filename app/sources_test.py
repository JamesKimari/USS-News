import unittest
from models import sources
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    """
    Test Case to test the behavior of the sources class
    """
    def setUp(self):
        """
        setUp method that will run before every test
        """
        self.new_sources = Sources("abc-news","ABC News")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))

if __name__ == '__main__':
    unittest.main()
    