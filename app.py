from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'INDEX'

@app.route('/greet/<string:name>/')
def greet(name):
    return name


if __name__ == '__main__':
    app.run(debug=True)