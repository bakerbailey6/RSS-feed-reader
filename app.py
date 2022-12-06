from flask import Flask, render_template, request
from rss.feed import *


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        return showResults(request.form['url'])
    else:
        return render_template('index.html')

def showResults(url=None):
    feed = Feed(url)
    title = feed.getTitle()
    description = feed.getDescription()
    published = feed.getPublished()
    length = feed.getLength()
    entries = feed.getEntries()
    image = feed.getImage()
    results = [{'title':entry.getTitle(), 'description':entry.getDescription(), 'published':entry.getPublished(), 'link':entry.getLink()} for entry in entries]
    return render_template('feed.html', title=title, description=description, published=published, image=image, results=results)

if __name__ == '__main__':
    app.run(debug=True)
