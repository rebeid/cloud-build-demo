from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def say_hello(name):
    return f"<h1>\\(^o^)/ HELLO {name.upper()}</h1>"


if __name__ == '__main__':
    app.run()
