from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional, List

from dehacked import fieldtype_factory
from dehacked.fieldtypes.base import BaseFieldType

if TYPE_CHECKING:
    from dehacked.target import Target


class Schema:

    def __init__(self, name: str, target: Target):
        self.name: str = name
        self.target: Target = target

        self.fields: Dict[str, BaseFieldType] = {}
        self.default_row: Dict[str, any] = {}

    def add_field(self, key: str, data: dict):
        field_type = fieldtype_factory.create(key, data, self.target)
        self.fields[key] = field_type
        self.default_row[key] = field_type.transform_from_data(field_type.default)

    def transform_field_from_data(self, data: dict):
        for key, value in data.items():
            if key not in self.fields:
                raise RuntimeError(f'Schema "{self.name}" contains data for unknown field "{key}".')
            field = self.fields[key]
            data[key] = field.transform_from_data(value)

    def validate_row(self, row: dict, index: int) -> List[str]:
        errors: List[str] = []

        for field_key, value in row.items():
            error = self.validate_field(field_key, value)
            if error is not None:
                errors.append(f'Validation error for {self.name} {index}, "{field_key}": {error}')

        return errors

    def validate_field(self, field_key: str, value: any) -> Optional[str]:
        if field_key not in self.fields:
            return f'Unknown field "{field_key}".'

        field = self.fields[field_key]
        return field.validate(value)
