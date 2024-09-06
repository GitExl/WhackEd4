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
        self.rows: Dict[int, dict] = {}
        self.next_index: int = 0

    def add_field(self, key: str, data: dict):
        field_type = fieldtype_factory.create(key, data, self.target)
        self.fields[key] = field_type
        self.default_row[key] = field_type.transform_from_data(field_type.default)

    def add_row(self, data: dict):

        # Start from a specific index.
        if '_index' in data:
            self.next_index = data['_index']
            del data['_index']

        for key, value in data.items():
            if key not in self.fields:
                raise RuntimeError(f'Table "{self.name}", contains data for unknown field "{key}".')
            field = self.fields[key]
            data[key] = field.transform_from_data(value)

        # Extend an existing row or create a new one from default data.
        if self.next_index in self.rows:
            self.rows[self.next_index].update(data)
        else:
            row = self.default_row.copy()
            row.update(data)
            self.rows[self.next_index] = row

        self.next_index += 1

    def validate(self):
        for row_index, row in self.rows.items():
            for field_key, value in row.items():
                if field_key not in self.fields:
                    raise RuntimeError(f'Table "{self.name}", row {row_index} contains unknown field "{field_key}".')
                field = self.fields[field_key]

                if not field.validate(value):
                    raise RuntimeError(f'Table "{self.name}", row {row_index}, field "{field_key}" contains invalid value "{value}".')
