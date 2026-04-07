#CLI
import taskmanager
import storage

#view all tasks
#should this be here or in main?
def view_tasks():
    task_list = storage.load_tasks() # returns a dictionary
    count = 1
    for task in task_list:
        print("Task " + str(count) + ": " + task["taskTitle"] + "   Task Completed: " + str(task["taskCompleted"]))
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
        print("Type 4: Mark task as complete")
        print("Type 5: View all current tasks")
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
            task_list = storage.load_tasks() #should we make this like a global var?
                # if no elements to delete, print no elements to delete
            if not task_list:
                # means empty, 0 elements
                print("List empty, nothing to delete!")
            else:
                # do delete
                print("Which task do you want to delete?")
                view_tasks()
                deleteTask = int(input())
                # for now, assuming user puts a valid index
                taskmanager.delete_task(deleteTask)
                print("Task deleted!")
                print()
        elif (currentAction == 3):
            # do edit
            taskmanager.rename_task()
            print("Task updated!")
            print()
        elif (currentAction == 4):
            # do mark task as complete
            taskmanager.mark_complete()
            print("Task completed!")
        elif (currentAction == 5):
            # do list all tasks
            view_tasks()
            print()
        elif (currentAction == 0):
            print("Goodbye!")
            return
        else:
            # means invalid number entered
            print("Please enter a valid action")
            # does this handle if someone enters a sentence or something? 

if __name__ == "__main__":
    main()