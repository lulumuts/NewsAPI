from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title='Home - Get the most up to date news on News One'
    return render_template('index.html', title = title)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns news details page and its data
    '''
    return render_template('news.html')