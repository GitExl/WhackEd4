from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class FlagsFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any):
        super().__init__(key, name, default)

        self.flagset_name: str

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'flagset' not in data:
            raise RuntimeError(f'Field {key} requires a flagset argument.')

        flagset_name = data['flagset']
        if flagset_name not in target.flagsets:
            raise RuntimeError(f'Field {key} references unknown flagset {flagset_name}.')
        field.flagset_name = flagset_name

        return field
