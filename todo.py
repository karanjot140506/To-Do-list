
todo = []
def add(task):
    todo.append({"task": task, "status": "Not Done"})
def delete(ind):
    if 0 <= ind < len(todo):
        del todo[ind]
    else:
        print("Invalid index")
def mark(ind):
    if 0 <= ind < len(todo):
        todo[ind]["status"] = "Done"
    else:
        print("Invalid index")
def update(ind, new_task):
    if 0 <= ind < len(todo):
        todo[ind]["task"] = new_task
    else:
        print("Invalid index")
def display():
    if todo == []:
        print("No Task")
    else:
        print("Tasks:-") 
        for ind, task in enumerate(todo, start=1):
            print(f"{ind}. {task['task']} - {task['status']}")
def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Display Tasks")
        print("6. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            task = input("Enter your task:")
            add(task)
        elif choice == "2":
            ind = int(input("Enter the index of task to delete:")) - 1
            delete(ind)
        elif choice == "3":
            ind = int(input("Enter the index of task to mark as done:")) - 1
            mark(ind)
        elif choice == "4":
            ind = int(input("Enter the index of task to update:")) - 1
            new_task = input("Enter the new task:")
            update(ind, new_task)
        elif choice == "5":
            display()
        elif choice == "6":
            break
        else:
            print("Invalid Choice. Try again")

if __name__ == "__main__":
    main()
            
            
            
            
    
                

