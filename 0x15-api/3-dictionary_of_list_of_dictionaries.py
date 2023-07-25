#!/usr/bin/python3
"""
    a Python script that, using REST API for all employees ID, returns
    information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


def employees():
    """A fuction that export data to JSON format"""
    employees_record = {}
    file_name = 'todo_all_employees.json'
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    get_employees = requests.get(user_url).json()

    for rec in get_employees:
        USERNAME = rec.get('username')
        USER_ID = rec.get('id')
        records = {USER_ID: []}
        user_todos = requests.get(user_url + str(USER_ID) + '/todos')
        todos = user_todos.json()

        for item in todos:
            record = {}
            record['username'] = USERNAME
            record['task'] = item.get('title')
            record['completed'] = item.get('completed')
            records[USER_ID].append(record)
            employees_record.update(records)

    with open(file_name, 'w') as json_file:
        json.dump(employees_record, json_file)


if __name__ == '__main__':
    employees()
