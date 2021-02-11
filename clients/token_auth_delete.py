import requests


def delete_user():
    requests.delete('http://127.0.0.1:8000/api/members/users/baris/')



if __name__ == '__main__':
    delete_user()
