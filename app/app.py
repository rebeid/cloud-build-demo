import os
from flask import Flask

app = Flask(__name__)


@app.route('/say/<something>')
def say_hello(something: str):
    return f"<h1>\\(^o^)/ {something}!</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT')))
