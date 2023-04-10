import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# ? if __name__ == "__main__":

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)

    r = requests.get(url = URL, data = json_data)

    data = r.json()

    print(data)

# get_data()

def post_data():
    data = {
        'name' : 'Anurag Doe',
        'email' : 'anurag.itmatters@gmail.com',
        'city' : 'San Francisco',
    }

    json_data = json.dumps(data)

    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
    





