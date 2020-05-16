# --coding:utf-8--

from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello():
    return '<h1>Hello Flask!</h1>'


if __name__ == '__main__':
    app.run()
