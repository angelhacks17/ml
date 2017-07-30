from flask import Flask
import backend_link.py as backend

app = Flask(__name__)

@app.route('/')
def init_request():
    return backend.initialize_model();


app.run()
