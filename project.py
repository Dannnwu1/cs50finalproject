import csv
import os
import sys
import time
from typing import List, Dict

import tabulate

TASK_FILE = "to_do_list.csv"
HEADER = ["No", "Description", "Status"]


def main():
    while True:
        clear_screen()
        try:
            # TODO 1 print out the menu
            task_list = load_task_list()
            # print(task_list)
            print_menu()
            # let user choose the function
            user_choice = get_user_choice()
            # check user input
            # check user's input is correct form
            if check_user_choice(user_choice):
                # do the function user selected
                # TODO 2 load task list
                # Task list should have a NO. Description, Status

                user_choice = int(user_choice)
                if user_choice == 1:
                    view_tasks(task_list)


                # TODO 3 add task to the task list
                # let user enter the task and add to the task list
                # Save the task list to a csv
                # go back to menu
                elif user_choice == 2:
                    add_task(task_list)

                elif user_choice == 3:
                    mark_task(task_list)

                elif user_choice == 4:
                    del_task(task_list)



                # TODO 6 exit the app
                elif user_choice == 5:
                    save_tasks(task_list)
                    sys.exit("Bye, see you next time.")
                # exit app

        except ValueError:
            print("Invalid Input")
        except KeyboardInterrupt:
            save_tasks(task_list)
            sys.exit()


def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_menu() -> None:
    border = [
        "***************************************************",
        "* Welcome to Daniel's To-Do List App             ",
        "***************************************************",
        "* Please select the function:                     ",
        "* 1. 📊 View all tasks                             ",
        "* 2. ➕ Add a Task                           ",
        "* 3. ✅ Mark a task as done                      ",
        "* 4. ❌ Delete a Task                            ",
        "* 5. ⏎️ Exit                                      ",
        "***************************************************"
    ]

    for line in border:
        print(line)


def get_user_choice() -> str:
    return input("Please enter (1 to 5) to select the function: ")


def check_user_choice(prompt) -> bool:
    if not prompt.isdigit():
        raise ValueError
    if 1 <= int(prompt) <= 5:
        return True
    else:
        raise ValueError


def load_task_list() -> List[str]:
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        with open(TASK_FILE, "w", encoding="utf-8", ) as file:
            writer = csv.DictWriter(file,fieldnames= HEADER)
            writer.writerow(HEADER)
        return []


def view_tasks(task_list) -> None:
    if not task_list:
        print("No task to view")
        time.sleep(2)
        return

    headers = HEADER
    table_data = []
    for task in task_list:
        status_icon = "✅" if task["Status"] == "Completed" else "❌"
        row = [
            task['No'],
            task['Description'],
            status_icon
        ]
        table_data.append(row)
    print(tabulate.tabulate(table_data, headers=headers, tablefmt="grid"))
    time.sleep(2)


def add_task(task_list: List[Dict[str, str]]) -> List[Dict[str, str]] or print_menu():
    task = input("Please enter the task description: ").strip()

    if not task:
        print("Task cannot be empty")
        return

    if not back_to_menu(task):
        pass

    index = get_max_index(task_list)

    new_task = {
        'No': index,
        'Description': task,
        'Status': 'Not done'
    }

    task_list.append(new_task)
    # print(task_list)
    save_tasks(task_list)


# TODO 4 delete the task from the task list
# view task list
# user input the task no
# search the task in the list
# delete the task
# save task list to a csv
# go back to menu
def del_task(task_list: List[Dict[str, str]]) -> None or print_menu():
    if not task_list:
        print("No task to delete.")
        return

    view_tasks(task_list)
    task = input("Please enter the no of the task to delete: ")

    if not back_to_menu(task):
        pass

    if not task.isdigit():
        raise ValueError

    if search_task(task, task_list):
        found_tasks = search_task(task, task_list)
        index = task_list.index(found_tasks[0])
        task_list.pop(index)
    else:
        print("Not found the task")

    save_tasks(task_list)

    return


# TODO 5 update the task status
# view task list
# user input the task no
# search the task in the list
# update the task status
# save task list to a csv
# go back to menu
def mark_task(task_list: List[Dict[str, str]]) -> None:
    if not task_list:
        print("No task to mark.")
        return

    view_tasks(task_list)

    task = input("Please enter the no to mark as done: ")
    if not back_to_menu(task):
        pass

    if not task.isdigit():
        raise ValueError

    if search_task(task, task_list):
        found_tasks = search_task(task, task_list)
        index = task_list.index(found_tasks[0])
        task_list[index]["Status"] = "Completed"
    else:
        print("Not found the task")
    save_tasks(task_list)
    return


def search_task(task_number: str, task_list: List[Dict[str, str]]):
    return [task for task in task_list if task["No"] == task_number]


def save_tasks(task_list: List[Dict[str, str]]) -> None:
    try:
        with open(TASK_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(task_list)
        print(f"✅ The task list had been saved")
        time.sleep(2)
    except Exception as e:
        print(f"❌ Failed to add task：{e}")
        time.sleep(20)


def get_max_index(task_list):
    max_index = 0
    for task in task_list:
        current_index = int(task["No"])
        if current_index > max_index:
            max_index = current_index
    return max_index + 1


def back_to_menu(prompt):
    if prompt in ('b', 'back', 'B', 'Back'):
        return print_menu()


if __name__ == "__main__":
    main()
