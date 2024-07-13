## app/models/role.py

class Role:
    def __init__(self, name: str, description: str):
        """
        Initialize a Role instance.

        Args:
            name (str): The name of the role.
            description (str): The description of the role.
        """
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        """
        Return a string representation of the role.

        Returns:
            str: The string representation of the role.
        """
        return f"Role(name={self.name}, description={self.description})"
