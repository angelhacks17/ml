import requests
import random_tree as model

url = 'https://angelhacks17-nihaleg.c9users.io/'

def initialize_model():
    init_url = url + 'initial'
    r = requests.get(init_url)
    return model.predict(r.text)

def update_model(current_cuisine):
    return model.predict(current_cuisine)


model_prediction = initialize_model()
