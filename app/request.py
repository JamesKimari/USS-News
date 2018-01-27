from app import app
import urllib.request, json
from .models import sources

Source = sources.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
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

def process_sources(source_list):
    """
    Function that processes the news result and transforms them to a list of objects
    """
    news_sources = []
    for source in source_list:
        name = source.get('name')
        
       
        if name:
            source_object = Source(name)
            news_sources.append(source_object)

    return news_sources


