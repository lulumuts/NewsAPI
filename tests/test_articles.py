import unittest
from .models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Articles Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.article_articles = Articles('Im confused', 'What it do', 'Get me a fidget spinner','whatever whatever','blah blah blah', 'another one')

    def test_instance(self):
        self.assertTrue(isinstance(self.article_articles, Articles))

    if __name__ == '__main__':
        unittest.main()
