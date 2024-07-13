## app/models/influence.py

class Influence:
    def __init__(self, name: str, effect: str):
        """
        Initialize an Influence instance.

        Args:
            name (str): The name of the influence.
            effect (str): The effect of the influence.
        """
        self.name = name
        self.effect = effect

    def __repr__(self) -> str:
        """
        Return a string representation of the influence.

        Returns:
            str: The string representation of the influence.
        """
        return f"Influence(name={self.name}, effect={self.effect})"
