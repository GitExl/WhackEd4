from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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

    def validate(self, value: any) -> Optional[str]:
        if type(value) != int:
            return 'Fixed point data must be an integer.'

        normalized_value = value / 65536.0
        if normalized_value < self.min or normalized_value > self.max:
            return f'Fixed point value {normalized_value} must be between {self.min} and {self.max} inclusive.'

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(cls.MIN_ABSOLUTE, float(data['min']))
        if 'max' in data:
            field.max = min(cls.MAX_ABSOLUTE, float(data['max']))

        return field
