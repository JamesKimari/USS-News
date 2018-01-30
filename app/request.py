import urllib.request, json
from .models import Source, News, Category


# Getting api key
api_key = None

# Getting the news base url
base_url = None
news_url = None
catg_url = None

def configure_request(app):
    global api_key, base_url, news_url, catg_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    news_url = app.config['NEWS_API_BASE_URL']
    catg_url = app.config['CATG_API_BASE_URL']

def get_sources(category):
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(category, api_key)

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
    news_articles = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        url = source.get('url')       
       
        if name:
            source_object = Source(id, name, url)
            news_articles.append(source_object) 
                
    return news_articles  

def get_news(id):
    get_news_url = news_url.format(id, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        news_data = url.read()
        news_response = json.loads(news_data)

        news_articles = None

        if news_response['articles']:
            news_articles_list = news_response['articles']
            news_articles = process_articles(news_articles_list)  
           
    return news_articles    
    
def process_articles(news_list):
    """
    Function that processes the news sources and transforms them to a list of objects
    """
    news_articles = []
    news_dictionary = {}   
    
    for news in news_list:
        news_id = news['source']

        news_dictionary['id'] = news_id['id']
        news_dictionary['name'] = news_id['name']

        id = news_dictionary['id']
        name = news_dictionary['name']         

        author = news.get('author')
        title = news.get('title')
        description = news.get('description')
        url = news.get('url')
        urlToImage = news.get('urlToImage')
        publishedAt = news.get('publishedAt')
        
        if urlToImage:
            news_object = News(author, title, description, url, urlToImage, publishedAt)
            news_articles.append(news_object)
          
    return news_articles


def get_category(category):
    """
    Function that gets the json response to our url request
    """
    get_sources_url = catg_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_categories_data = url.read()
        get_categories_response = json.loads(get_categories_data)

        news_categories_articles = None

        if get_categories_response['articles']:
            news_categories_list = get_categories_response['articles']
            news_categories_articles = process_categories(news_categories_list)

    return news_categories_articles


def process_categories(categories_list):
    """
    Function that processes the news sources and transforms them to a list of objects
    """
    news_categories_articles = []

    for category in categories_list:
        title = category.get('title')
        description = category.get('description')
        url = category.get('url')
        urlToImage = category.get('urlToImage')
        publishedAt = category.get('publishedAt')

        if urlToImage:
            source_object = Category(title, description, url, urlToImage, publishedAt)
            news_categories_articles.append(source_object)

    return news_categories_articles
