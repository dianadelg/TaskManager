#CLI
import taskmanager
import storage

#view all tasks
#should this be here or in main?
def view_tasks():
    task_list = storage.load_tasks() # returns a dictionary
    count = 0
    for task in task_list:
        print(str(count) + ": " + task)
        count = count + 1

def main():
    # Your program logic goes here
    print("Welcome to Task Manager!")
    currentAction = -1
    while(currentAction != 0):
        print("What would you like to do?")
        print("Type 1: Add task")
        print("Type 2: Delete task")
        print("Type 3: Edit task")
        print("Type 4: View all current tasks")
        print("Type 0: Exit Task Manager")
        currentAction = int(input())
        
        if(currentAction == 1):
            # do add
            print("Please enter task:")
            newTask = input()
            taskmanager.add_task(newTask)
            print("Task: " + newTask + " added!")
            print()
        elif (currentAction == 2):
            # do delete
            print("Which task do you want to delete?")
            view_tasks()
            deleteTask = int(input())
            taskmanager.delete_task(deleteTask)
            print("Task deleted!")
            print()
        elif (currentAction == 3):
            # do edit
            taskmanager.rename_task()
            print("Task updated!")
            print()
        elif (currentAction == 4):
            # do list all tasks
            view_tasks()
            print()
        else:
            # means invalid number entered
            print("Please enter a valid action")
            # does this handle if someone enters a sentence or something? 

if __name__ == "__main__":
    main()