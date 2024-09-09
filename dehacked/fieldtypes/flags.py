from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from dehacked.fieldtypes.base import BaseFieldType

if TYPE_CHECKING:
    from dehacked.target import Target


class FlagsFieldType(BaseFieldType):

    def __init__(self, key: str, name: str, default: any, target: Target):
        super().__init__(key, name, default, target)

        self.flagset_name: Optional[str] = None

    def validate(self, value: any) -> Optional[str]:
        if not isinstance(value, set):
            return 'Flags data must be a set.'

        flagset = self.target.flagsets[self.flagset_name]
        for flag_key in value:
            if flag_key not in flagset.flags:
                return f'Flag {flag_key} is not part of flagset {self.flagset_name}.'

        return None

    def transform_from_data(self, value: any) -> any:

        # Parse integers into known flags.
        # @todo replace integers in all data with arrays and skip this step
        if isinstance(value, int):
            flags = set()
            flagset = self.target.flagsets[self.flagset_name]
            for flag_index, flag in flagset.flag_by_index.items():
                bit = 2 ** flag_index
                if value & bit:
                    flags.add(flag.key)
            return flags

        if isinstance(value, list):
            return set(value)

        raise RuntimeError(f'Cannot transform "{value}" into flag data.')

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
