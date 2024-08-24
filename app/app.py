import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_info() -> str:
    app = os.environ.get('APP_NAME')
    target = os.environ.get('TARGET')
    return f"<h1>This is <b>{app}<b> in <b>{target}<b> environment</h1>"


@app.route('/say/<something>')
def say_something(something: str) -> str:
    return f"<h1>\\(^o^)/ {something}!</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT')))
