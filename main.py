from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', ''])
def bla():
    if request.method
    return 'blablabla'

if __name__ == '__main__':
    app.run(host='', port=8000)
