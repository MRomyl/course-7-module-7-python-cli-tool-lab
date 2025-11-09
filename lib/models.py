
class Task:
    def __init__(self, title):
        self.title = title              # Assign the title
        self.completed = False          # Set completed to False

    def complete(self):
        self.completed = True           # Mark the task as complete
        print(f"Task '{self.title}' has been marked as completed!")  # Print confirmation


class User:
    def __init__(self, name):
        self.name = name               # Store the user's name
        self.tasks = []                # Initialize an empty list of tasks

    def add_task(self, task):
        self.tasks.append(task)        # Add the task to the user's task list
        print(f"Task '{task.title}' added for user '{self.name}'.")  # Confirmation message

    def get_task_by_title(self, title):
        for task in self.tasks:        # Search for a task by title
            if task.title == title:
                return task
        return None                    # Return None if not found



