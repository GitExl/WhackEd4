from typing import Optional

from dehacked.fieldtypes.base import BaseFieldType


class ActionFieldType(BaseFieldType):

    def validate(self, value: any) -> Optional[str]:
        if not isinstance(value, str):
            return 'Action data must be a string.'

        if value not in self.target.actions:
            return f'Action "{value}" is unknown.'

        return None
