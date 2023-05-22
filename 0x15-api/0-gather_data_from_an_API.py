import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee information
    response = requests.get(employee_url)
    if response.status_code != 200:
        print("Error retrieving employee information.")
        return

    employee_data = response.json()
    employee_name = employee_data["name"]

    # Fetch TODO list
    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error retrieving TODO list.")
        return

    todos_data = response.json()
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo["completed"]]

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print("\t", task["title"])

# Example usage: pass the employee ID as a command-line argument
import sys

if len(sys.argv) < 2:
    print("Please provide an employee ID as a command-line argument.")
else:
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
