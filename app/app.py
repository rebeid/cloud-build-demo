import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_release_version() -> str:
    version = os.environ.get('RELEASE', 'undefined')
    return f"Accessing the {version} of the app\n"


@app.route('/say/<something>')
def say_something(something: str) -> str:
    return f"<h1>\\(^o^)/ {something}!</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT')))
