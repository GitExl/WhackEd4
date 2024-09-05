from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dehacked.target import Target

from dehacked.fieldtypes.base import BaseFieldType


class FlagsFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.flagset_name: Optional[str] = None

    def validate(self, value: any) -> bool:
        if type(value) != int:
            return False

        flagset = self.target.flagsets[self.flagset_name]
        for flag_index in range(0, 32):
            bit = 2 ** (flag_index + 1)
            if value & bit and flag_index not in flagset.flag_by_index:
                return False

        return True

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        field = super().parse(key, data, target)

        if 'flagset' not in data:
            raise RuntimeError(f'Field "{key}" requires a "flagset" property.')

        flagset_name = data['flagset']
        if flagset_name not in target.flagsets:
            raise RuntimeError(f'Field "{key}" references unknown flagset "{flagset_name}".')
        field.flagset_name = flagset_name

        return field
