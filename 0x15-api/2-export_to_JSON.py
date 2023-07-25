#!/usr/bin/python3
"""
    a Python script that, REST API for a given employee ID, returns
    information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


def to_csv(user_id):
    """A fuction export data to JSON format"""
    records = {user_id: []}
    file_name = '{}.json'.format(user_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    get_name = requests.get(user_url)
    USER_NAME = get_name.json().get('name')

    user_todos = requests.get(user_url + '/todos')
    todos = user_todos.json()

    for item in todos:
        record = {}
        record['task'] = item.get('title')
        record['completed'] = item.get('completed')
        record['username'] = USER_NAME
        records[user_id].append(record)

    with open(file_name, 'w') as json_file:
        json.dump(records, json_file)


if __name__ == '__main__':
    to_csv(argv[1])
