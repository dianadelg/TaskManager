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

#rename task
def rename_task(taskId, updatedTask):
    task_list = storage.load_tasks()
    for task in task_list:
         if task["taskId"] == taskId:
             task["taskTitle"] = updatedTask
    storage.save_tasks(task_list)

#delete task
def delete_task(taskId):
    task_list = storage.load_tasks()    
    # used to filter current list and remove id passed in, returns list - that element
    updated_task_list = [t for t in task_list if t.get('taskId') != taskId]
    # when we delete, we need to update all of the taskIds to be in order for clarity to user
    for index, task in enumerate(updated_task_list, 1):
        task["taskId"] = index
    storage.save_tasks(updated_task_list)

#mark task as complete
def mark_complete(taskId):
    task_list = storage.load_tasks()
    for task in task_list:
         if task["taskId"] == taskId:
             task["taskCompleted"] = True
    storage.save_tasks(task_list)