from typing import Tuple, Optional

from whacked4.enum import WhackedEnum


class ActionArgumentType(WhackedEnum):
    """
    Types of action arguments.
    """

    THING = 'thing'
    STATE = 'state'
    SOUND = 'sound'
    AMMO = 'ammo'
    WEAPON = 'weapon'
    INTEGER = 'integer'
    FIXED_POINT = 'fixedpoint'


class ActionArgument:
    """
    Describes an argument of an action.
    """

    def __init__(self, name: str, description: str, argument_type: ActionArgumentType):
        """
        Constructor.

        :param name: the name of the argument.
        :param description: a short description of the argument.
        :param argument_type: the type of argument, determining how it's value is handled.
        """

        self.name: str = name
        self.description: str = description
        self.type: ActionArgumentType = argument_type

        self.range: Optional[Tuple[int, int]] = None

    @classmethod
    def from_json(cls, json: dict):
        """
        Creates a new ActionArgument instance from a dict of JSON data.

        :param json: a dict of JSON data.

        :return: a new ActionArgument instance.
        """

        argument = cls(
            str(json['name']),
            str(json['description']),
            ActionArgumentType.get(json['type'])
        )

        # Accept range for numeric types.
        if argument.type == ActionArgumentType.INTEGER or argument.type == ActionArgumentType.FIXED_POINT:
            argument.range = (int(json['range'][0]), int(json['range'][1]))

        return argument
