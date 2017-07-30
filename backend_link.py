import requests
import random_tree as model

url = 'https://angelhacks17-nihaleg.c9users.io'

def initialize_model():
    init_url = url + 'initial'
    r = requests.get(init_url)
    print(r.text);
    return model.get_correlations(r.text, model.get_init_data())
