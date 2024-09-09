from typing import Optional
from dehacked.fieldtypes.base import BaseFieldType


class AmmoFieldType(BaseFieldType):

    def validate(self, value: any) -> Optional[str]:
        if not isinstance(value, int):
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

        return None
