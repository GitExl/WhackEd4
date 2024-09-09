from __future__ import annotations

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class AmmoFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

    def validate(self, value: any) -> Optional[str]:
        if type(value) != int:
            return 'Ammo type data must be an integer.'

        if 'ammo' not in self.target.tables:
            return 'An ammo table and schema must be present.'

        if value == 5:
            return None
        if value == 4:
            return 'Ammo type 4 is not allowed.'

        table = self.target.tables['ammo']
        if value < 0 or value >= len(table.rows):
            return f'Ammo value {value} is unknown.'
