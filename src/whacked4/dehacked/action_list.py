"""
Action list functionality.
"""

from typing import Dict, Optional, List

from whacked4.dehacked.action import Action


class ActionList:
    """
    A list of known state actions.
    """

    def __init__(self):
        self._actions: Dict[str, Action] = {}

    def get_by_key(self, key: str) -> Optional[Action]:
        """
        Returns an action from a key.

        @param key: The key of the action to find.

        :return: An Action or None if it cannot be found.
        """

        key = key.lower()
        return self._actions.get(key, None)

    def get_by_name(self, name: str) -> Optional[Action]:
        """
        Returns an action from its name.

        :param name: The name to search.

        :return: An Action or None if it cannot be found.
        """

        for action in self._actions.values():
            if action.name == name:
                return action

        return None

    def add_from_json(self, data: dict):
        """
        Adds new actions from raw data.

        :param data: A dictionary with parsed JSON data.
        """

        for key, value in data.items():
            key = key.lower()
            self._actions[key] = Action.from_json(key, value)

    def get_names(self) -> List[str]:
        """
        :return: A list of all action names.
        """
        return list(map(lambda action: action.name, self._actions.values()))
