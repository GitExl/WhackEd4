from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class EnumFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any):
        super().__init__(key, name, default)

        self.enum_name: str

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'enum' not in data:
            raise RuntimeError(f'Field {key} requires an enum argument.')

        enum_name = data['enum']
        if enum_name not in target.enums:
            raise RuntimeError(f'Field {key} references unknown enum {enum_name}.')
        field.enum_name = enum_name

        return field
