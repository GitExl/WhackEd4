from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class FixedPointFieldType(BaseFieldType):

    MIN_ABSOLUTE = -32768.0
    MAX_ABSOLUTE = 32767.0

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.min: float = self.MIN_ABSOLUTE
        self.max: float = self.MAX_ABSOLUTE

    def validate(self, value: any) -> bool:
        if type(value) != int:
            return False
        return self.min <= (value / 65536.0) <= self.max

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(cls.MIN_ABSOLUTE, float(data['min']))
        if 'max' in data:
            field.max = min(cls.MAX_ABSOLUTE, float(data['max']))

        return field
