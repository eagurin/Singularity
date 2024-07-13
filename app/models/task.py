## app/models/task.py

class Task:
    def __init__(self, name: str, action: str):
        """
        Initialize a Task instance.

        Args:
            name (str): The name of the task.
            action (str): The action associated with the task.
        """
        self.name = name
        self.action = action

    def __repr__(self) -> str:
        """
        Return a string representation of the task.

        Returns:
            str: The string representation of the task.
        """
        return f"Task(name={self.name}, action={self.action})"
