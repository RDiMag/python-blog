from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Rachel'}
  posts = [
    {
      'author': {'username': 'Mina'},
      'body': 'Barbie movie blows Oppenheimer away.'
    },
    {
      'author': {'username': 'Roxy'},
      'body': 'Veep season 3 continues to amuse.'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)