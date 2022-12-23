import random

HELP = """
help - напечатать справку по программе
add - добавить задачу в список(название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
exit - выход
random - add a random task to Today"""

RANDOM_TASKS = ["sleep", "eat", "run", "want"]

tasks = {

}

run = True

def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задач
        tasks[date].append(task)
    else:
        # Даты нет в словаре
        # Создаем запись с ключом data
        tasks[date] = []
        tasks[date].append(task)
    print("Task " + task + " added on " + date)

while run:
    command = input("Input command: ")
    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Input date: ")
        task = input("Input task's name: ")
        add_todo(date, task)
    elif command == "show":
        date = input("Input date to display list of tasks: ")
        if date in tasks:
            for task in tasks[date]:
                print("- " + task)
        else:
            print("Date is incorect.")
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Today", task)
    elif command == "exit":
        print("Thank you for using this program.")
        break
    else:
        print("unknown task")
        break

print("Good buy!")
