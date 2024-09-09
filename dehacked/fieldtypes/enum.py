from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class EnumFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.enum_name: Optional[str] = None

    def validate(self, value: any) -> Optional[str]:
        if type(value) != int:
            return 'Enum data must be an integer.'

        if value not in self.target.enums[self.enum_name]:
            return f'Unknown enum key {value}.'

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'enum' not in data:
            raise RuntimeError(f'Field "{key}" requires an "enum" property.')

        enum_name = data['enum']
        if enum_name not in target.enums:
            raise RuntimeError(f'Field "{key}" references unknown enum "{enum_name}".')
        field.enum_name = enum_name

        return field
