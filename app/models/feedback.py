## app/models/feedback.py

class Feedback:
    def __init__(self, user: str, content: str):
        """
        Initialize a Feedback instance.

        Args:
            user (str): The user who provided the feedback.
            content (str): The content of the feedback.
        """
        self.user = user
        self.content = content

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the feedback.

        Args:
            new_content (str): The new content to be updated.
        """
        self.content = new_content

    def get_summary(self) -> str:
        """
        Get a summary of the feedback.

        Returns:
            str: The summary of the feedback.
        """
        return self.content[:100] + '...' if len(self.content) > 100 else self.content

    def __repr__(self) -> str:
        """
        Return a string representation of the feedback.

        Returns:
            str: The string representation of the feedback.
        """
        return f"Feedback(user={self.user}, content={self.content})"
