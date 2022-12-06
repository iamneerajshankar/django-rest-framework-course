import requests
import json

URL = "http://127.0.0.1:8000/get_user_info/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


get_data()


def post_data():
    data = {
        'name': 'Neeraj',
        'profession': 'Software Engineer',
        'job_location': 'Pune, Maharashtra',
        'area_pin': 45288,
        'date_of_birth': '2022-04-10'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    # print(f"{r.json()}")
    data = r.json()
    print(data)


#post_data()

def update_data():
    data = {
        'id': 5,
        'name': 'Jack',
        'city': 'Ranchi'
    }

    json_data = json.dumps(data)
    print(f"The JSON Data {json_data}")
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {'id': 5}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# delete_data()
