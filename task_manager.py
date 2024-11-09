def task():
    tasks=[]
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")
    total_task=int(input("Enter how many task you wnat to add = "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} : ")
        tasks.append(task_name)
    print(f"Today's tasks are \n {tasks} ")
    while True:
        try:
            operation =int(input("Enter 1-Add \n 2-Update \n 3-Delete  \n 4-View \n 5-Exit \n"))
            match operation :
                case 1:
                    add=input("Enter task you want to add : ")
                    tasks.append(add)
                    print(f"Task {add} has been successfully added...")
                case 2:
                    update_val=input("Enter the task name you want to update = ")
                    if update_val in tasks:
                        up=input("Enter new task : ")
                        ind=tasks.index(up)
                        tasks[ind]=up
                        print(f"Updated task '{update_val}' to '{up}'")
                    else:
                        print("Task not found")
                case 3:
                    del_val=input("Enter the task name you want to delete = ")
                    if del_val in tasks :
                        ind=tasks.index(del_val)
                        tasks.pop(ind)
                        print(f"Delete task '{del_val}'")
                    else:
                        print("Task not found")
                case 4:
                    print(f"Total tasks = {tasks}")
                case 5:
                    print("Closing the program...")
                    break
                case _:
                    print("Invaild input. Please enter a number from 1 to 5 ")
        except ValueError:
            print("Invalid Input. Plese enter a valid number.")
task()