#!/usr/bin/python3

'''
returns to-do list of a given employee id
script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
'''

import requests
import sys

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"
    employees_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employees_id))
    user_response = user.json()
    params = {"userId": employees_id}
    todos = requests.get(url + "to_do_response", params=params)
    to_do_response = todos.json()
    done_tasks = []
    for todo in to_do_response:
        if todo.get("done_tasks") is True:
            done_tasks.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{})".format(
        user_response.get("name"), len(done_tasks), len(to_do_response)))
    for done in done_tasks:
        print("\t {}".format(done))
