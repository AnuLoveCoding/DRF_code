import requests
import json

URL = ""

# ? if __name__ == "__main__":

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
        json_data = json.dumps(data)

        r = requests.get(url = URL, data = json_data)

        data = r.json()

        print(data)

get_data(1)
