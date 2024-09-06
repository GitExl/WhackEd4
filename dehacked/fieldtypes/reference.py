from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class ReferenceFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.table_name: Optional[str] = None

    def validate(self, value: any) -> bool:
        if type(value) != int:
            return False

        table = self.target.tables[self.table_name]
        return value in table.rows

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'reference' not in data:
            raise RuntimeError(f'Field "{key}" requires a "reference" property.')

        table_name = data['reference']
        if table_name not in target.tables:
            raise RuntimeError(f'Field "{key}" references unknown table "{table_name}".')
        field.table_name = table_name

        return field
