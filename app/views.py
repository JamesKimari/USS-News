from flask import render_template
from app import app

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    title = "News Hub"
    return render_template('index.html', title=title)

#views
@app.route('/news/<int:news_id>')
def news(news_id):
    """
    View root page function that returns the index page and its data
    """
    return render_template('news.html', id = news_id)