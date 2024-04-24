#!/usr/bin/python3

'''
returns to-do list of a given employee id 
script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
'''

import requests
import sys

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"
    employees_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employees_id)).json()
    parameters = {"userId": employees_id}
    todos = requests.get(url + "todos", parameters).json()
    done_tasks =  [t.get("title") for t in todos if t.get("done_tasks") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    [print("\t {}".format(done)) for done in done_tasks]

