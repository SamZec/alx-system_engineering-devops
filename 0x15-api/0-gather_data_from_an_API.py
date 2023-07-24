#!/usr/bin/python3
"""
    a Python script that, REST API for a given employee ID, returns
    information about his/her TODO list progress.
"""

import requests
from sys import argv


def get_todos(user_id):
    """A fuction returning about user_id from a REST API"""
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    get_name = requests.get(user_url)

    EMPLOYEE_NAME = get_name.json().get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    user_todos = requests.get(user_url + '/todos')
    todos = user_todos.json()
    TOTAL_NUMBER_OF_TASKS = len(todos)

    for item in todos:
        if item.get("completed"):
            TASK_TITLE.append(item.get("title"))
            NUMBER_OF_DONE_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'.format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print("\t {}".format(title))


if __name__ == '__main__':
    get_todos(argv[1])
