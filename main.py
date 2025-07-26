def main():
    tasks = []


    print("---------Welcome to to do app---------")
    total_tasks = int(input("Enter Number of tasks you want to add: "))
    for i in range(1, total_tasks+1):
        task =  input(f"Enter task {i}: ")
        tasks.append(task)
    print(f"Today tasks are: {tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit: "))

        if operation == 1:
            add_task = input("Enter a task you want to add: ")
            tasks.append(add_task)
            print("Task Added!")
            print(f"Now your tasks are {tasks}")
        elif operation == 2:
            update_task = input("Enter the task you want to update: ")
            if update_task in tasks:
                updated_task = input("Enter the task: ")
                index = tasks.index(update_task)
                tasks[index] = updated_task
                print("Task Updated!")
            else:
                print("There is no such task")
        elif operation == 3:
            del_task = input("Enter task you want to delete: ")
            if del_task in tasks:
                tasks.remove(del_task)
                print("Task Removed!")
            else:
                print("There is no such task")
        elif operation == 4:
            print(f"Your tasks are {tasks}")
        elif operation == 5:
            print("Closing The Program...")
        else:
            print("Invalid Input")
        break
main()