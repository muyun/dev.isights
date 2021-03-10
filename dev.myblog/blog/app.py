import os
import logging 

from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages

app = Flask(__name__)
pages = FlatPages(app)


@app.route('/hello')
def hello():
    page = pages.get('hello')
    logging.debug(f'page.meta:{page.meta}')
    title = page.meta['title']

#    posts = (p for p in pages if 'date' in p.meta)
#    print(posts)
#    sorted(posts,key=lambda p: p.meta['date'], reverse=True)
    return render_template('hello.html', titles=title)

@app.route('/about')
def about():
    return "About"

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=4000)
    
    with app.test_request_context('/'):
        print(request.posts)
