from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class BoolFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any):
        super().__init__(key, name, default)

        self.value_true: any = 1
        self.value_false: any = 0

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = BaseFieldType.parse(key, data, target)

        if 'value_true' in data:
            field.value_true = data['value_true']
        if 'value_false' in data:
            field.value_false = data['value_false']

        return field
