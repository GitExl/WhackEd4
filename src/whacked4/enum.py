"""
Custom enum class.
"""

from enum import Enum


class WhackedEnum(Enum):
    """
    Extended enum.
    """

    @classmethod
    def contains(cls, value: any) -> bool:
        """
        Returns if a value is present in this enum.
        """

        return value in cls._value2member_map_

    @classmethod
    def get(cls, value: any) -> any:
        """
        Get a value from this enum.
        """

        if cls.contains(value):
            return value

        raise KeyError(f'Enum {cls.__name__} does not contain value "{value}".')
