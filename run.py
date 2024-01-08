from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    first = 'Ricardo'
    last = 'Cordero'
    age = '24'
    return f'Hello World -{first} {last} {age}'
