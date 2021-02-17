from pprint import pprint

import requests


def get_data():
    token = 'Token 5002b9a4e14d126c8b2b6021e1148a5b66fd846b'
    headers = {
        'Authorization': token,
    }
    response = requests.get(
        url='http://127.0.0.1:8000/api/members/users',
        headers=headers
    )
    print('status code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)


def activity_create():
    token = 'Token 39413f018e799b7877d2f89ee0086db526ba0396'
    headers = {
        'Authorization': token,
    }
    data = {

    "activity_name": "Django etkinliği 2020",
    "about": "django rest framework öğreniyoruz",
    "is_online": True,
    "is_private": False,
    "is_active": False,
    "starting_date": "2021-02-13T20:56:00+03:00",
    "due_date": "2021-02-13T22:56:00+03:00",
    "broadcasting_url": "url",
    'creator':2
}

    response = requests.post(
        url='http://127.0.0.1:8000/api/actions/activities/',
        headers=headers,
        data=data
    )
    print('status code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    activity_create()
