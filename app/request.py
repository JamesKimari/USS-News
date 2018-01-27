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
        
       
        if name:
            source_object = Source(name)
            news_sources.append(source_object)

    return news_sources

def get_news(category):
    get_news_description_url = base_url.format(top_headlines, category, api_key)

    with urllib.request.urlopen(get_news_description_url) as url:
        news_description_data = url.read()
        news_description_response = json.loads(news_description_data)

        news_object = None

        if news_description_response:
            source = news_description_response.get('source').get('name')
            title = news_description_response.get('title')
            description = news_description_response.get('description')
            url = news_description_response.get('url')
            urlToImage = news_description_response.get('urlToImage')
            publishedAt = news_description_response.get('publishedAt')

        news_object = News(source, title, description, url, urlToImage, publishedAt)

    return news_object





