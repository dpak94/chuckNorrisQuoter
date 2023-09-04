import requests, json
from flask import Flask, url_for, render_template, redirect

def quoteFunc():
    url = 'https://api.chucknorris.io/jokes/random'
    norris_request = requests.get(url).text
    norris_json = json.loads(norris_request)
    quote = norris_json['value']
    return quote

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', quote = quoteFunc)




if __name__ == '__main__':
    app.run(debug = True)
