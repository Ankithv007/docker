from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hey, Hi from ankith '

@app.route('/health')
def health():
    return 'Server is up and running'