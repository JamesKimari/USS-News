from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    # Getting business news
    general_news = get_news('general')
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    sports_news = get_news('sports')
    print(business_news)
    title = "US News"
    return render_template('index.html', title=title, general = general_news,
     business=business_news, entertainment=entertainment_news, sports = sports_news)

#views
@app.route('/news/<int:news_id>')
def news(news_id):
    """
    View root page function that returns the index page and its data
    """
    return render_template('news.html', id = news_id)
