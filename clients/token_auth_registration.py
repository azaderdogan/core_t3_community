from pprint import pprint

import requests

# ACCOUNT_EMAIL_REQUIRED = (True,)
"""status code:  400
{'email': ['A user is already registered with this e-mail address.']}
"""


def registration():
    # LOGİN
    credentials = {
        'username': 'community',
        'email': 'community@gmail.co',
        'password1': 'test123.',
        'password2': 'test123.',
    }
    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/',
        data=credentials,
    )
    print('status code: ', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    registration()
