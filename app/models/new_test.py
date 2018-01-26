import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    """
    Test class to test the behavior of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_news = News("the-washington-post",
                            "Bush Man", 
                             "Trump apologizes for retweeting",
                             "In an interview with ...",
                             "https://www.washingtonpost.com/world/trump-apologizes-for-retweeting-anti-muslim-videos-from-far-right-british-group/2018/01/26/7d334e0c-0268-11e8-9d31-d72cf78dbeee_story.html",
                             "https://www.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2018/01/26/Foreign/Images/Trump_32516-08392.jpg?t=20170517",
                             "2018-01-26T07:58:21Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()
