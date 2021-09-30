from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'HeroicHitesh'}
    posts = [
        {
            'title': 'Hello World',
            'body': 'Create Hello World Application in Flask'
        },
        {
            'title': 'Templating',
            'body': 'Use conditional statements, loops and template inheritance to learn templating in Flask'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)