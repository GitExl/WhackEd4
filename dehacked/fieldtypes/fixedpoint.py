from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class FixedPointFieldType(BaseFieldType):

    MIN_ABSOLUTE = -32768.0
    MAX_ABSOLUTE = 32767.0

    def __init__(self, key: str, name: str, default: any):
        super().__init__(key, name, default)

        self.min: float = self.MIN_ABSOLUTE
        self.max: float = self.MAX_ABSOLUTE

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(cls.MIN_ABSOLUTE, float(data['min']))
        if 'max' in data:
            field.max = min(cls.MAX_ABSOLUTE, float(data['max']))

        return field
