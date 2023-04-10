import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# ? if __name__ == "__main__":

# ! get the data program;
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)

    r = requests.get(url = URL, data = json_data)

    data = r.json()

    print(data)

# get_data()

    # ! create a new data program;
    def post_data():
        data = {
            'name' : 'Anurag Doe',
            'roll' : 116009,
            'city' : 'San Francisco',
        }

        json_data = json.dumps(data)

        r = requests.post(url = URL, data = json_data)
        data = r.json()
        print(data)

    # post_data()

    # ! update data program;
    def update_data():
        data = {
            'id' : 5,
            'name' : 'Anurag Doe',
            'roll' : 105,
            'city' : 'San Francisco',
        }

        json_data = json.dumps(data)

        r = requests.put(url = URL, data = json_data)
        data = r.json()
        print(data)

    # update_data()

    # ! Delete data program;
    def delete_data():
        data = {
            'id' : 5,
        }
        json_data = json.dumps(data)
        r = requests.delete(url = URL, data = json_data)
        data = r.json()
        print(data)

    # delete_data()


    





