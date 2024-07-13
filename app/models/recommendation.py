## app/models/recommendation.py

class Recommendation:
    def __init__(self, title: str, content: str):
        """
        Initialize a Recommendation instance.

        Args:
            title (str): The title of the recommendation.
            content (str): The content of the recommendation.
        """
        self.title = title
        self.content = content

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the recommendation.

        Args:
            new_content (str): The new content to be updated.
        """
        self.content = new_content

    def get_summary(self) -> str:
        """
        Get a summary of the recommendation.

        Returns:
            str: The summary of the recommendation.
        """
        # Placeholder for summary logic
        # This should be replaced with actual summary generation logic
        return self.content[:100] + '...' if len(self.content) > 100 else self.content

    def __repr__(self) -> str:
        """
        Return a string representation of the recommendation.

        Returns:
            str: The string representation of the recommendation.
        """
        return f"Recommendation(title={self.title}, content={self.content})"
