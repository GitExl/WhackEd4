from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from dehacked.fieldtypes.base import BaseFieldType

if TYPE_CHECKING:
    from dehacked.target import Target


class BoolFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.value_true: any = 1
        self.value_false: any = 0

    def validate(self, value: any) -> Optional[str]:
        if not isinstance(value, int):
            return 'Boolean data must be an integer.'

        if value not in {self.value_true, self.value_false}:
            return f'Expected {self.value_true} or {self.value_false} for boolean data.'

        return None

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = BaseFieldType.parse(key, data, target)

        if 'value_true' in data:
            field.value_true = data['value_true']
        if 'value_false' in data:
            field.value_false = data['value_false']

        return field
