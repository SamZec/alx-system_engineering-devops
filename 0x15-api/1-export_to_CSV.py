#!/usr/bin/python3
"""
    a Python script that, REST API for a given employee ID, returns
    information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


def to_csv(user_id):
    """A fuction export data to CSV format"""
    user_records = []
    file_name = '{}.csv'.format(user_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    get_name = requests.get(user_url)
    USER_NAME = get_name.json().get('name')

    user_todos = requests.get(user_url + '/todos')
    todos = user_todos.json()

    for item in todos:
        record = {}
        record["USER_ID"] = item.get('userId')
        record["USERNAME"] = USER_NAME
        record["TASK_COMPLETED_STATUS"] = item.get('completed')
        record["TASK_TITLE"] = item.get('title')
        user_records.append(record)

    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for line in user_records:
            csv_writer.writerow(line.values())


if __name__ == '__main__':
    to_csv(argv[1])
