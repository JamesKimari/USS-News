from app import app
import urllib.request, json
from .models import sources
from .models import news

Source = sources.Source
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

# Getting the endpoints
sources = 'sources'
top_headlines = 'top-headlines'

def get_sources(category):
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(sources, category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_sources = None

        if get_sources_response['sources']:
            news_sources_list = get_sources_response['sources']
            news_sources = process_sources(news_sources_list)
    
    return news_sources

def process_sources(sources_list):
    """
    Function that processes the news sources and transforms them to a list of objects
    """
    news_sources = []
    for source in sources_list:
        name = source.get('name')
        url = source.get('url')       
       
        if name:
            source_object = Source(name, url)
            news_sources.append(source_object)
    
    return news_sources

def get_general(category):
    get_news_url = base_url.format(top_headlines,category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        news_data = url.read()
        news_response = json.loads(news_data)

        news_object = None

        if news_response['articles']:
            news_articles_list = news_response['articles']
            news_articles = process_news(news_articles_list)            

    return news_articles

def process_news(news_list):
    """
    Function that processes the news sources and transforms them to a list of objects
    """
    news_articles = []
    for news in news_list:             
        title = news.get('title')
        description = news.get('description')
        url = news.get('url')
        urlToImage = news.get('urlToImage')
        publishedAt = news.get('publishedAt')
        
        if urlToImage:
            news_object = News(title, description, url, urlToImage, publishedAt)
            news_articles.append(news_object)

    return news_articles
    



