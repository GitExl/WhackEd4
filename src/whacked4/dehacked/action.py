from typing import List, Optional

from whacked4.dehacked.entry import Entry
from whacked4.enum import WhackedEnum
from whacked4.dehacked.action_argument import ActionArgument


class ActionType(WhackedEnum):
    """
    Entity types that actions can be intended for.
    """

    THING = 'thing'
    WEAPON = 'weapon'


class Action:
    """
    Stores information about a state action as supported by an engine.
    """

    def __init__(self, name: str, description: str, action_type: ActionType):
        """
        Constructor.

        :param name: the name of the action as used in a patch.
        :param description: a short description of what the action does.
        :param action_type: the type of entity the action is meant to be used on.
        """

        self.name: str = name
        self.description: str = description
        self.type: ActionType = action_type

        self.sound: Optional[str] = None
        self.spawns: Optional[int] = None
        self.sets_momentum: bool = False
        self.uses_extra_flash_state: bool = False

        self.unused: List[ActionArgument] = []
        self.arguments: List[ActionArgument] = []

    def get_state_parameter_properties(self, state: Entry) -> List[str]:
        """
        Returns a list of action argument properties from a state that are valid for this action.

        :param state: the state to return the property values of.

        :return: a list of the state's property values.
        """

        param_keys = []

        param_keys.extend(['unused1', 'unused2'])
        param_keys.extend(['arg{}'.format(x) for x in range(1, len(self.arguments) + 1)])

        return [str(state[key]) for key in param_keys]

    @classmethod
    def from_json(cls, json: dict):
        """
        Creates a new Action instance from a dict of JSON data.

        :param json: data to create the instance with.

        :return: a new Action instance.
        """

        action = cls(
            str(json['name']),
            str(json['description']),
            ActionType.get(json['type'])
        )

        if 'spawns' in json:
            action.spawns = int(json['spawns'])

        if 'sound' in json:
            action.sound = str(json['sound'])

        if 'setsMomentum' in json:
            action.sets_momentum = bool(json['setsMomentum'])

        if 'usesExtraFlashState' in json:
            action.uses_extra_flash_state = bool(json['usesExtraFlashState'])

        if 'unused' in json:
            for unused in json['unused']:
                action.unused.append(ActionArgument.from_json(unused))

        if 'arguments' in json:
            for argument in json['arguments']:
                action.arguments.append(ActionArgument.from_json(argument))

        return action
