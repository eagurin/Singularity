## app/models/group.py

from typing import List

class Group:
    def __init__(self, name: str, members: List[str] = None):
        """
        Initialize a Group instance.

        Args:
            name (str): The name of the group.
            members (List[str]): The members of the group, defaults to None and is set to an empty list if not provided.
        """
        self.name = name
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_member(self, member: str) -> None:
        """
        Add a member to the group.

        Args:
            member (str): The member to be added.
        """
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member: str) -> None:
        """
        Remove a member from the group.

        Args:
            member (str): The member to be removed.
        """
        if member in self.members:
            self.members.remove(member)

    def get_members(self) -> List[str]:
        """
        Get the list of members in the group.

        Returns:
            List[str]: The list of members.
        """
        return self.members

    def __repr__(self) -> str:
        """
        Return a string representation of the group.

        Returns:
            str: The string representation of the group.
        """
        return f"Group(name={self.name}, members={self.members})"
