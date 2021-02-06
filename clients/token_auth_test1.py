import requests

from pprint import pprint


def client():
    #LOGİN
    credentials = {
        'username': 'azad',
        'password': 'azad'
    }
    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
    )
    print('statsus code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
