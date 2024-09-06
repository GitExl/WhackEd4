from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dehacked.target import Target


class BaseFieldType:

    def __init__(self, key: str, name: str, default: any, target: Target):
        self.key: str = key
        self.name: str = name
        self.default: any = default
        self.target: Target = target

        self.patch_key: Optional[str] = None
        self.group: Optional[str] = None

    def validate(self, value: any) -> bool:
        return True

    def transform_from_data(self, value: any) -> any:
        return value

    @classmethod
    def parse(cls, key: str, data: dict, target: Target):
        if 'name' not in data:
            raise RuntimeError(f'Field "{key}" is missing a "name" property.')
        if 'default' not in data:
            raise RuntimeError(f'Field "{key}" is missing a "default" property.')

        field = cls(key, data['name'], data['default'], target)

        if 'patch_key' in data:
            field.patch_key = str(data['patch_key'])
        if 'group' in data:
            field.group = str(data['group'])

        return field
