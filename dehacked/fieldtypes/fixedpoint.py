from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from dehacked.fieldtypes.base import BaseFieldType

if TYPE_CHECKING:
    from dehacked.target import Target


class FixedPointFieldType(BaseFieldType):

    MIN_ABSOLUTE = -32768.0
    MAX_ABSOLUTE = 32767.0

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.min: float = self.MIN_ABSOLUTE
        self.max: float = self.MAX_ABSOLUTE

    def validate(self, value: any) -> Optional[str]:
        if not isinstance(value, int):
            return 'Fixed point data must be an integer.'

        norm = value / 65536.0
        if norm < self.min or norm > self.max:
            return f'Fixed point value {norm} must be between {self.min} and {self.max} inclusive.'

        return None

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(cls.MIN_ABSOLUTE, float(data['min']))
        if 'max' in data:
            field.max = min(cls.MAX_ABSOLUTE, float(data['max']))

        return field
