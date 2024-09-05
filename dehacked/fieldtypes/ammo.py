from __future__ import annotations

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class AmmoFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'ammo' not in target.tables:
            raise RuntimeError(f'Field "{key}" requires an "ammo" table.')

        return field

    def validate(self, value: any) -> bool:
        if type(value) != int:
            return False

        if value == 5:
            return True
        if value == 4:
            return False

        table = self.target.tables['ammo']
        return 0 <= value < len(table.rows)
