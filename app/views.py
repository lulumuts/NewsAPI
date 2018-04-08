from flask import render_template
from app import app
from .request import get_sources,get_articles

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    status_sources = get_sources('status')

    title='Home - Get the most up to date news on News One'
    return render_template('index.html', title = title, status = status_sources)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns news details page and its data
    '''
    # return render_template('news.html')

@app.route('/article/<int:id>')
def article(id):
    '''
    View articles page function for all the articles for specific source
    '''
    articles_sources = get_articles('article')


    articles = get_articles(id)
    title = f'{article.title}'
    # reviews = Review.get_reviews(movie.id)


    return render_template('news.html', title=title,status = status_sources, articles = articles_sources)
