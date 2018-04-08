from app import app
import urllib.request, json
from newsapi import NewsApiClient
from .models import news

News=news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

#Getting the articles base url
articles_base_url = app.config ['ARTICLES_API_BASE_URL']



def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url + api_key

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results= None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    Function that process the movie result and transforms them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain news source details

    Returns :
        sources_results: A list of news sources
    '''

    sources_results = []

    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url= sources_item.get('url')

        if url:
            sources_object = News(id,name,description,url)
            sources_results.append(sources_object)

    return sources_results

def get_articles(id):
    get_articles_url= articles_base_url + api_key

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_object = None
        if get_articles_response:
            author = get_articles_response.get('author')
            title = get_articles_response.get('title')
            description = get_articles_response.get('description')
            url = get_articles_response.get('url')
            urlToImage = get_articles_response.get('urlToImage')
            publishedAt= get_articles_response.get('publishedAt')

            articles_object = Article(author,title,description,url,urlToImage,publishedAt)

        return articles_object
