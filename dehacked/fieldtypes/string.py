from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from dehacked.fieldtypes.base import BaseFieldType

if TYPE_CHECKING:
    from dehacked.target import Target


class StringFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.min: int = 0
        self.max: int = 0xFFFF

    def validate(self, value: any) -> Optional[str]:
        if not isinstance(value, str):
            return 'String data must be a string.'

        if len(value) < self.min or len(value) > self.max:
            return f'String length must be between {self.min} and {self.max} characters inclusive.'

        return None

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'min' in data:
            field.min = max(0, int(data['min']))
        if 'max' in data:
            field.max = min(0xFFFF, int(data['max']))

        return field
