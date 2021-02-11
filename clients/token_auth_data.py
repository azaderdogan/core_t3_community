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


def create_new_user():
    pass


if __name__ == '__main__':
    get_data()
