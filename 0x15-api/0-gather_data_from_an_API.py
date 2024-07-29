#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""
import requests
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_url = "{}users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Failed to fetch user information")
        sys.exit(1)

    user_data = user_response.json()

    # Fetch todos for the user
    todo_url = "{}todos".format(base_url)
    todo_response = requests.get(todo_url, params={'userId': employee_id})
    if todo_response.status_code != 200:
        print("Failed to fetch todos")
        sys.exit(1)

    todos = todo_response.json()
    completed = []
    for todo in todos:
        if todo["completed"]:
            completed.append(todo["title"])

    # Print user tasks information
    print("Employee {} is done with tasks ({}/{}):".format(user_data.get('name'), len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task))

