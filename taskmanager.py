# what we do with the data
# What is a task?
# What happens when you complete one?
# What rules exist?
# It does NOT care how data is stored
import storage

#add task
def add_task(task_title):
    # validate that the title is not empty
    # maybe trim whitespace
    if(len(task_title) == 0):
        # means Empty
        return False
    else:
        storage.insert_task(task_title)
        return True

#delete task
def delete_task(task_ID):
    if not storage.get_all_tasks():
        return False
    else:
        storage.delete_task(task_ID)
        return True

#rename task -- we assume task exists, hence 
def rename_task(task_ID, updated_task):
    if not storage.get_all_tasks():
    # means empty, 0 elements
        return False # I don't like this, but I'm not sure if I should keep the prompts in here or not?
    else:
        # for now, assuming user puts a valid index
        # delete
        storage.update_task_title(task_ID, updated_task)        
        return True

def get_tasks():
# call storage.get_all_tasks()
# take each row tuple
# convert it into a task dictionary
# return the list of task dictionaries
    rows = storage.get_all_tasks()
    tasks = []
    for row in rows:
        task = {
            "taskId": row[0],
            "taskTitle": row[1],
            "taskCompleted": bool(row[2])
        }
        tasks.append(task)
    return tasks


#mark task as complete
def mark_complete(task_ID):
    if not storage.get_all_tasks():
        return False
    else: 
        storage.mark_task_completed(task_ID)
        return True    


#TO DO
#if not storage.get_all_tasks() --> 
# okay for now, but they only check whether any tasks exist, not whether the specific ID exists
# So if the user enters 999, code will still say “Task deleted!” even if that task wasn’t there.
# As expected. Need to fix

#TO DO:
# Add handling for invalid task IDs
# Add handling for non-numeric input