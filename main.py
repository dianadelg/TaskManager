#CLI
import taskmanager
import storage

#view all tasks
#should this be here or in task manager? -- task manager
# def view_tasks():
#     task_list = storage.load_tasks() # returns a dictionary
#     count = 1
#     for task in task_list:
#         print("Task " + str(count) + ": " + task["taskTitle"] + "   Task Completed: " + str(task["taskCompleted"]))
#         count = count + 1
def print_tasks():
    
    tasks = taskmanager.get_tasks()
    if not tasks:
        print("No tasks!")
    else:
        for task in tasks:
            print(f'{task["taskId"]}. {task["taskTitle"]} - Completed: {task["taskCompleted"]}')

def main():
    # Your program logic goes here
    print("Welcome to Task Manager!")
    storage.initialize_db()
    current_action = -1
    while(current_action != 0):
        print("What would you like to do?")
        print("Type 1: Add task")
        print("Type 2: Delete task")
        print("Type 3: Edit task")
        print("Type 4: Mark task as complete")
        print("Type 5: View all current tasks")
        print("Type 0: Exit Task Manager")
        
        current_action = int(input())
        
        if(current_action == 1):
            # add task
            print("Please enter new task:")
            new_task = input()
            if(taskmanager.add_task(new_task)):
                print("Task: " + new_task + " added!")
            else:
                print("Cannot insert an empty task! Please enter a valid task name.")
            print()

        elif (current_action == 2):
            # delete task
            print("Which task do you want to delete?")
            print_tasks()
            delete_task = int(input())
            if(taskmanager.delete_task(delete_task)):
                print("Task deleted!")
            else:
                print("List empty, nothing to delete!")
            print()

        elif (current_action == 3):
            # edit/rename task
            print("Which task do you want to edit?")
            print_tasks()
            edit_task = int(input())
            # for now, assuming user puts a valid index TODO: will need to fix
            print("What do you want to edit the task to be?")
            updated_task = input()
            if(taskmanager.rename_task(edit_task, updated_task)):
                print("Task edited!")
            else:
                print("List empty, nothing to delete!")
            print()

        elif (current_action == 4):
            # mark task as completed
            print("Which task do you want to mark as completed?")
            print_tasks()
            complete_task = int(input())
            # for now, assuming user puts a valid index
            if(taskmanager.mark_complete(complete_task)):
                print("Task completed!")
            print()

        elif (current_action == 5):
            # view tasks
            print_tasks()
        else:
            # means invalid number entered
            print("Please enter a valid action")
            # does this handle if someone enters a sentence or something? 

if __name__ == "__main__":
    main()
# prompt user
# call taskmanager
# print results