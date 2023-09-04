import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def quoteFunc():
    url = 'https://api.chucknorris.io/jokes/random'
    norris_request = requests.get(url).text
    norris_json = json.loads(norris_request)
    quote = norris_json['value']
    return quote


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/quotegen', methods=['POST', 'GET'])
def generator():
    if request.method == 'GET':
        return render_template('quote.html', quote=quoteFunc())
    else:
        return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=True)
