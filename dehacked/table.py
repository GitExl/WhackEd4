from __future__ import annotations

from typing import Dict, List

from dehacked import fieldtype_factory
from dehacked.fieldtypes.base import BaseFieldType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target


class Table:

    def __init__(self, name: str, target: Target):
        self.name: str = name
        self.target: Target = target

        self.fields: Dict[str, BaseFieldType] = {}
        self.default_row: Dict[str, any] = {}
        self.rows: List = []

    def add_field(self, key: str, data: dict):
        field_type = fieldtype_factory.create(key, data, self.target)
        self.fields[key] = field_type
        self.default_row[key] = field_type.default

    def add_row(self, data: dict):
        row = self.default_row.copy()
        row.update(data)
        self.rows.append(row)

    def validate(self):
        for row_index, row in enumerate(self.rows):
            for field_key, value in row.items():
                if field_key not in self.fields:
                    raise RuntimeError(f'Table "{self.name}", row {row_index} contains unknown field "{field_key}".')
                field = self.fields[field_key]

                if not field.validate(value):
                    raise RuntimeError(f'Table "{self.name}", row {row_index}, field "{field_key}" contains invalid value "{value}".')
