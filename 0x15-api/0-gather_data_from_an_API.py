#!/usr/bin/python3
""" Using this REST API, for a given employee ID
returns information about his/her TODO list progress. """

from urllib import response
import requests
from sys import argv


def request_api(argv):
    """Module for do request api"""
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    response_todo = requests.get(todo)
    response_user = requests.get(users)
    todo_json = response_todo.json()
    user_json = response_user.json()
    name_user = user_json.get('name')
    task_done = 0
    task_do = 0
    count = 0
    my_list = []

    for task in todo_json:
        task_done += 1
        if task['completed'] is True:
            my_list = [task['title']]
            task_do += 1

    print(f"Employee {name_user} is done with tasks({task_do}/{task_done}):")

    for count in my_list:
        print('\t', str(count))


if __name__ == "__main__":
    request_api(argv)
