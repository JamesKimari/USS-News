from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__)

from app import views 

