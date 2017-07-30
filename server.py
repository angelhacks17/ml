from flask import Flask

app = Flask(__name__)

@app.route('/')
def init_request():
    return 'initializing model...'
