from __future__ import annotations

from typing import Dict, List
from dehacked.schema import Schema

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target


class Table:

    def __init__(self, name: str, schema: Schema, target: Target):
        self.name: str = name
        self.target: Target = target
        self.schema: Schema = schema

        self.rows: Dict[int, dict] = {}
        self.next_index: int = 0

    def add_row(self, data: dict):

        # Start from a specific index.
        if '_index' in data:
            self.next_index = data['_index']
            del data['_index']

        self.schema.transform_field_from_data(data)

        # Extend an existing row or create a new one from default data.
        if self.next_index in self.rows:
            self.rows[self.next_index].update(data)
        else:
            row = self.schema.default_row.copy()
            row.update(data)
            self.rows[self.next_index] = row

        self.next_index += 1

    def validate(self) -> List[str]:
        errors: List[str] = []
        for row_index, row in self.rows.items():
            errors.extend(self.schema.validate_row(row, row_index))
        return errors
