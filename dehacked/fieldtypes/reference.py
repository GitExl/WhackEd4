from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class ReferenceFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.table_name: Optional[str] = None

    def validate(self, value: any) -> Optional[str]:
        if type(value) != int:
            return 'Reference data must be an integer.'

        if self.table_name not in self.target.tables:
            return f'Unknown reference of type "{self.table_name}".'

        table = self.target.tables[self.table_name]
        if value not in table.rows:
            return f'Table "{self.table_name}" does not contain index {value}.'

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'reference' not in data:
            raise RuntimeError(f'Field "{key}" requires a "reference" property.')

        field.table_name = data['reference']

        return field
