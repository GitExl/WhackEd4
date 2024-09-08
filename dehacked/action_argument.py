"""
State action argument descriptors.
"""
from enum import Enum
from typing import Tuple, Optional


class ActionArgumentType(Enum):
    """
    Types of action arguments.
    """

    THING = 'thing'
    STATE = 'state'
    SOUND = 'sound'
    AMMO = 'ammo'
    WEAPON = 'weapon'
    INTEGER_SIGNED = 'int'
    INTEGER_UNSIGNED = 'uint'
    FIXED_POINT = 'fixed'


class ActionArgument:
    """
    Describes an argument of an action.
    """

    def __init__(self, name: str, description: str, argument_type: ActionArgumentType):
        """
        Constructor.

        :param name: the name of the argument.
        :param description: a short description of the argument.
        :param argument_type: the type of argument, determining how its value is handled.
        """

        self.name: str = name
        self.description: str = description
        self.type: ActionArgumentType = argument_type

        self.range: Optional[Tuple[int, int]] = None

    @classmethod
    def parse(cls, action_key: str, argument_key: str, data: dict):
        """
        Creates a new ActionArgument instance from a data dict.

        :param action_key: the key of the action this argument belongs to.
        :param argument_key: the key of this argument.
        :param data: a dict of data to create the instance from.

        :return: a new ActionArgument instance.
        """

        if 'name' not in data:
            raise RuntimeError(f'Action "{action_key}" argument "{argument_key}" requires a "name" property.')
        if 'description' not in data:
            raise RuntimeError(f'Action "{action_key}" argument "{argument_key}" requires a "description" property.')
        if 'type' not in data:
            raise RuntimeError(f'Action "{action_key}" argument "{argument_key}" requires a "type" property.')

        argument = cls(
            data['name'],
            data['description'],
            ActionArgumentType(data['type'])
        )

        if 'range' in data:
            argument.range = (data['range'][0], data['range'][1])

        return argument
