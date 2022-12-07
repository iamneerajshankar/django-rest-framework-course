import requests
import json

post_url = "http://127.0.0.1:8000/user-info/post/"
get_url = "http://127.0.0.1:8000/get_user_info/"
partial_update_url = "http://127.0.0.1:8000/user-info/partial-update/"
delete_url = "http://127.0.0.1:8000/user-info/delete/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=get_url, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name': 'Shivam Raj',
        'profession': 'Software Engineer Database',
        'job_location': 'Bangalore, Karnataka',
        'area_pin': 45288,
        'date_of_birth': '2022-04-10'
    }

    json_data = json.dumps(data)
    r = requests.post(url=post_url, data=json_data)
    # print(f"{r.json()}")
    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 1,
        'name': 'Neeraj Shankar',
        'profession': 'Software Engineer',
        'job_location': 'Pune, Maharashtra',
        'area_pin': 45201,
        'date_of_birth': '1997-10-10'
    }

    json_data = json.dumps(data)
    print(f"The JSON Data {json_data}")
    r = requests.put(url=partial_update_url, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    r = requests.delete(url=delete_url, data=json_data)
    data = r.json()
    print(data)


if __name__ == "__main__":
    # post_data()
    update_data()
    # delete_data()
