# what we do with the data
# What is a task?
# What happens when you complete one?
# What rules exist?
# It does NOT care how data is stored
import storage

#add task
def add_task(newTask):
    task_list = storage.load_tasks()
    task_list.append(newTask)
    storage.save_tasks(task_list)
    # AHH add this:
    # 1. Load existing tasks → task_list

    # 2. If empty:
    # → id = 1

    # 3. Else:
    # → find max(taskId)
    # → id = max + 1

    # 4. Create new task:
    # {
    #     taskId: ?
    #     taskTitle: ?
    #     taskCompleted: false
    # } which should be type dictionary. tasks are a list of dictionaries!!!

    # 5. Append that object

    # 6. Save

#update task as complete
def update_complete(taskId):
    task_list = storage.load_tasks()

#rename task
def rename_task(taskId, updatedTask):
    print("Task renamed!")

#delete task
def delete_task(taskId):
    print("Task deleted!")