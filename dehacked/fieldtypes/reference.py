from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class ReferenceFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any):
        super().__init__(key, name, default)

        self.table_name: str

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'reference' not in data:
            raise RuntimeError(f'Field {key} requires a reference argument.')

        table_name = data['reference']
        if table_name not in target.tables:
            raise RuntimeError(f'Field {key} references unknown table {table_name}.')
        field.table_name = table_name

        return field
