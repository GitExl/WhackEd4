from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class StringFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.min: int = 0
        self.max: int = 0xFFFF

    def validate(self, value: any) -> bool:
        if type(value) != str:
            return False

        return self.min <= len(value) <= self.max

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(0, int(data['min']))
        if 'max' in data:
            field.max = min(0xFFFF, int(data['max']))

        return field


