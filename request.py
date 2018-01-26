from app import app
import urllib.request, json
from .models import news

news = news.News

# Getting api key
api_key = app.config['MOVIE_API_KEY']