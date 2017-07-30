from flask import Flask
import backend_link as backend

app = Flask(__name__)



@app.route('/')
def init_request():
    backend.model_prediction = backend.update_model(backend.model_prediction)
    return backend.model_prediction

app.run(host='0.0.0.0', port='8080')
