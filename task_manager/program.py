# by Paulina Czempiel

# modules
import sqlite
import datetime
from tasks import Tasks


# main func to say hello and start looping
def main():
    print("Hello")
    input_loop()


# program main loop
def input_loop():
    while True:
        print("What do you want to do?")
        val = input("[l]ist tasks, [a]dd task, [e]dit task, [d]elete task, or e[x]it? ").lower().strip()
        if val == 'l':
            list_tasks()
        elif val == 'a':
            add_task()
        elif val == 'e':
            edit_task()
        elif val == 'd':
            delete_task()
        elif val == 'x':
            print("Bye!")
            break
        else:
            print(f"Don't know what to do with '{val}'")
        print()


# lists all, today's or month's tasks
def list_tasks():
    val = input("Would you like to list [a]ll tasks, [t]oday's tasks or tasks this [m]onth? ")
    if val == 'a':
        print("Your task list: ")
        sqlite.list_tasks()
    elif val == 't':
        day = str(datetime.datetime.now().day)
        month = str(datetime.datetime.now().month)
        year = str(datetime.datetime.now().year)
        if len(day) == 1:
            day = '0' + day
        if len(month) == 1:
            month = '0' + month
        sqlite.list_tasks_today(day, month, year)
    elif val == 'm':
        month = str(datetime.datetime.now().month)
        year = str(datetime.datetime.now().year)
        if len(month) == 1:
            month = '0' + month
        sqlite.list_tasks_month(month, year)
    else:
        print(f"Don't know what to do with '{val}'")
        list_tasks()


# add task to base
def add_task():
    name = input("Name of the task: ")
    date = input("Deadline of this task (DD-MM-YYYY): ")
    if date[5] != '-' or date[2] != '-' or len(date) > 10:
        print("Wrong input!")
        add_task()
    values = list(map(int, date.split('-')))
    if values[0] < 1 or values[0] > 31:
        print("Wrong input!")
        add_task()
    elif values[1] < 1 or values[1] > 12:
        print("Wrong input!")
        add_task()
    elif values[2] < 2020:
        print("Wrong input!")
        add_task()
    description = input("Description of the task: ")
    t = Tasks(name, date, description)
    sqlite.add_task(t)


# edit task (by hash)
def edit_task():
    task_hash = input("What task would you like to edit? Describe by task hash: ")
    if len(task_hash) != 20:
        print("Wrong input!")
        edit_task()
    val = input("Would you like to edit [n]ame, [d]ate or de[s]cription? ").lower().strip()
    if val == 'n':
        edit_name(task_hash)
    elif val == 'd':
        edit_date(task_hash)
    elif val == 's':
        edit_description(task_hash)
    else:
        print(f"Don't know what to do with '{val}'")
        edit_task()


# delete task (by hash)
def delete_task():
    task_hash = input("What task would you like to delete? Describe by task hash: ")
    if len(task_hash) != 20:
        print("Wrong input!")
        delete_task()
    sqlite.delete_task(task_hash)


# edit name of task (by hash)
def edit_name(task_hash):
    name = input("Write new name of the task: ")
    sqlite.edit_task_name(task_hash, name)


# edit date in selected task
def edit_date(task_hash):
    date = input("Write new date of the task (DD-MM-YYY): ")
    if date[5] != '-' or date[2] != '-' or len(date) > 10:
        print("Wrong input!")
        edit_date(task_hash)
    values = list(map(int, date.split('-')))
    if values[0] < 1 or values[0] > 31:
        print("Wrong input!")
        edit_date(task_hash)
    elif values[1] < 1 or values[1] > 12:
        print("Wrong input!")
        edit_date(task_hash)
    elif values[2] < 2020:
        print("Wrong input!")
        edit_date(task_hash)
    sqlite.edit_task_date(task_hash, date)


# edit description in selected task
def edit_description(task_hash):
    description = input("Write new description of the task: ")
    sqlite.edit_task_description(task_hash, description)


if __name__ == "__main__":
    main()
