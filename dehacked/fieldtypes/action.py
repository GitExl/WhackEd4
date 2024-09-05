from dehacked.fieldtypes.base import BaseFieldType


class ActionFieldType(BaseFieldType):

    def validate(self, value: any) -> bool:
        if type(value) != str:
            return False
        return value in self.target.actions
