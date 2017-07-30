from flask import Flask
import backend_link as backend

app = Flask(__name__)

@app.route('/')
def init_request():
    model_prediction = backend.initialize_model()
    return model_prediction

app.run(host='0.0.0.0', port='8080')
