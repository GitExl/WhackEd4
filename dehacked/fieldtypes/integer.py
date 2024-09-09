from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from dehacked.fieldtypes.base import BaseFieldType

if TYPE_CHECKING:
    from dehacked.target import Target


class IntegerFieldType(BaseFieldType):

    MIN_ABSOLUTE = 0
    MAX_ABSOLUTE = 255

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.min: int = self.MIN_ABSOLUTE
        self.max: int = self.MAX_ABSOLUTE

    def validate(self, value: any) -> Optional[str]:
        if isinstance(value, int):
            return 'Integer data must be an integer.'

        if value < self.min or value > self.max:
            return f'Integer value {value} must be between {self.min} and {self.max} inclusive.'

        return None

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(cls.MIN_ABSOLUTE, int(data['min']))
        if 'max' in data:
            field.max = min(cls.MAX_ABSOLUTE, int(data['max']))

        return field


class Int32FieldType(IntegerFieldType):

    MIN_ABSOLUTE = -2147483648
    MAX_ABSOLUTE = 2147483647

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.min = self.MIN_ABSOLUTE
        self.max = self.MAX_ABSOLUTE


class Uint32FieldType(IntegerFieldType):

    MIN_ABSOLUTE = 0
    MAX_ABSOLUTE = 4294967295


class ByteFieldType(IntegerFieldType):

    MIN_ABSOLUTE = -128
    MAX_ABSOLUTE = 127


class UbyteFieldType(IntegerFieldType):

    MIN_ABSOLUTE = 0
    MAX_ABSOLUTE = 255
