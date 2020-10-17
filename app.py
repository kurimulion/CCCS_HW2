from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main():
    url = 'https://asia-east2-genial-beaker-292809.cloudfunctions.net/getNews'
    response = requests.get(url, params={'clientAddr': request.remote_addr})
    try:
        response = response.json()
        article = response['articles'][0]
        return render_template('index.html', title=article['title'], author=article['author'],
                               source=article['source']['name'], date=article['publishedAt'],
                               url=article['urlToImage'], description=article['description'])
    except:
        return "Some problems with the request."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

