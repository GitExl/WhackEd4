from enum import Enum


class WhackedEnum(Enum):

    @classmethod
    def contains(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def get(cls, value):
        if cls.contains(value):
            return value

        raise KeyError('Enum {} does not contain value "{}".'.format(cls.__name__, value))