"""
Action definition.
"""

from enum import Enum
from typing import List, Optional

from dehacked.action_argument import ActionArgument


class ActionType(Enum):
    """
    Entity types that actions can be intended for.
    """

    NONE = 'none'
    THING = 'thing'
    WEAPON = 'weapon'


class Action:
    """
    Stores information about a state action.
    """

    def __init__(self, name: str, description: str, action_type: ActionType):
        """
        Constructor.

        :param name: the name of the action as used in a patch.
        :param description: a short description of what the action does.
        :param action_type: the type of entity the action is meant to be used by.
        """

        self.name: str = name
        self.description: str = description
        self.type: ActionType = action_type

        self.sound: Optional[str] = None
        self.spawn: Optional[int] = None
        self.set_momentum: bool = False
        self.use_extra_flash_state: bool = False

        self.unused: List[ActionArgument] = []
        self.arguments: List[ActionArgument] = []

    # def get_state_parameter_properties(self, state: Entry) -> List[str]:
    #     """
    #     Returns a list of action argument properties from a state that are valid
    #     for this action.
    #
    #     :param state: the state to return the property values of.
    #
    #     :return: a list of the state's property values.
    #     """
    #
    #     param_keys = []
    #
    #     param_keys.extend(['unused1', 'unused2'])
    #     param_keys.extend([f'arg{x}' for x in range(1, len(self.arguments) + 1)])
    #
    #     return [str(state[key]) for key in param_keys]

    @classmethod
    def parse(cls, key: str, data: dict):
        """
        Creates a new Action instance from a data dict.

        :param key: the key of this action.
        :param data: data to create the instance with.

        :return: a new Action instance.
        """

        if 'description' not in data:
            raise RuntimeError(f'Action "{key}" requires a "description" property.')

        if 'name' not in data:
            name = key
        else:
            name = data['name']
        if 'type' in data:
            action_type = ActionType(data['type'])
        else:
            action_type = ActionType.NONE

        action = cls(name, data['description'], action_type)

        if 'spawn' in data:
            action.spawn = data['spawn']
        if 'sound' in data:
            action.sound = data['sound']
        if 'set_momentum' in data:
            action.sets_momentum = bool(data['set_momentum'])
        if 'use_extra_flash_state' in data:
            action.uses_extra_flash_state = bool(data['use_extra_flash_state'])
        if 'unused' in data:
            for index, unused in enumerate(data['unused']):
                action.unused.append(ActionArgument.parse(key, f'unused{index}', unused))
        if 'arguments' in data:
            for index, argument in enumerate(data['arguments']):
                action.arguments.append(ActionArgument.parse(key, f'arg{index}', argument))

        return action
