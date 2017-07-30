from flask import Flask
import backend_link as backend

app = Flask(__name__)

@app.route('/')
def init_request():
    return backend.initialize_model();


app.run(host='0.0.0.0', port='8080')
