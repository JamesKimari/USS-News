from flask import render_template
from . import main
from ..request import get_sources, get_news, get_category

@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    # Getting various news categories
    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    health_news = get_sources('health')
    technology_news = get_sources('technology')
    sports_news = get_sources('sports')

    title = "US News"
    return render_template('index.html', title=title, general = general_news,
    business = business_news, entertainment = entertainment_news, health = health_news, technology = technology_news, sports = sports_news)

@main.route('/news/<id>')
def news(id):
    """
    view root page function that returns the news page and its data
    """
    news_articles = get_news(id)
       
    return render_template('news.html', news = news_articles)

@main.route('/categories/<category>')
def general(category):
    """
    view root page function that returns the categories page and its data
    """
    news_categories_articles = get_category(category)

    return render_template('general.html', general = news_categories_articles)


@main.route('/categories/<category>')
def business(category):
    """
    view root page function that returns the categories page and its data
    """
    news_categories_articles = get_category(category)

    return render_template('business.html', business = news_categories_articles)
