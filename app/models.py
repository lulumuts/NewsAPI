class News:
    '''
    News class to define News Source Objects
    '''

    def __init__(self,id, name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Article:

    all_articles=[]

    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

    @classmethod
    def get_articles(cls,id):
        response = []

        for article in cls.all_articles:
            if article.article_id == id:
                response.append(articles)

        return response
