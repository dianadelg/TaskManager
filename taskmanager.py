# what we do with the data
# What is a task?
# What happens when you complete one?
# What rules exist?
# It does NOT care how data is stored
import storage

#add task
def add_task(newTask):
    id = 0 
    task_list = storage.load_tasks()
    new_task = {}
    if not task_list:
        # means empty, 0 elements
        #create dictionary with this
        new_task = {
            "taskId": 1,
            "taskTitle": newTask,
            "taskCompleted": False
        }
    else:
        # get max task id
        latestID = len(task_list)+1
        #create dictionary with this
        new_task = {
            "taskId": latestID,
            "taskTitle": newTask,
            "taskCompleted": False
        }
    task_list.append(new_task)
    storage.save_tasks(task_list)

#update task as complete
def update_complete(taskId):
    task_list = storage.load_tasks()

#rename task
def rename_task(taskId, updatedTask):
    print("Task renamed!")

#delete task
def delete_task(taskId):
    print("Task deleted!")