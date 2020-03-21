from flask import Flask, request
import os

PORT = os.environ.get('PORT')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', ''])
def bla():
    return 'blablabla'

if __name__ == '__main__':
    app.run(host='', port=PORT)
