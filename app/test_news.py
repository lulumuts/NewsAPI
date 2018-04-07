import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Im confused', 'What it do', 'Get me a fidget spinner','whatever whatever',"http://www.blahblahblah.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    if __name__ == '__main__':
        unittest.main()
