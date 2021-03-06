from flask import Flask, jsonify, render_template, request, url_for
import random

app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)


@app.route('/_random_number')
def random_number():
    return str(random.randrange(1, 100))


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Ajax Test'
        )


if __name__ == '__main__':
    app.run(debug=True)
