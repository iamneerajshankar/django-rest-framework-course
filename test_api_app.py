import requests
import json

post_url = "http://127.0.0.1:8000/movie-info/post/"
get_url = "http://127.0.0.1:8000/movie-info/get/"
partial_update_url = "http://127.0.0.1:8000/movie-info/partial-update/"
delete_url = "http://127.0.0.1:8000/movie-info/delete/"


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
        'name': 'Avengers Endgame',
        'director': 'Russo Brothers',
        'year': 2019,
        'rating': 8.9,
        'franchise': 'Marvel Studios'
    }

    json_data = json.dumps(data)
    r = requests.post(url=post_url, data=json_data)
    # print(f"{r.json()}")
    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 1,
        'name': 'Infinity War',
        'director': 'Russo Brothers',
        'year': 2017,
        'rating': 8.8,
        'franchise': 'Marvel Studios'
    }

    json_data = json.dumps(data)
    print(f"The JSON Data {json_data}")
    r = requests.put(url=partial_update_url, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    r = requests.delete(url=delete_url, data=json_data)
    data = r.json()
    print(data)


def list_dict():
    l1 = [{'name': 'Infinity War'}, {'name': 'Infinity War'}, {'name': 'Infinity War'},
          {'name': 'Infinity War'}, {'name': 'Infinity War'}]
    movie_name = 'Infinity War'
    for item in l1:
        if movie_name == item['name']:
            print("Its duplicate")


if __name__ == "__main__":
    post_data()
    #get_data(1)
    #update_data()
     #delete_data()
     #list_dict()
