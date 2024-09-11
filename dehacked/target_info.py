from typing import Set, Dict


class TargetInfoOption:

    def __init__(self, key: str, is_required: bool):
        self.key: str = key
        self.required: bool = is_required

    @classmethod
    def parse(cls, key: str, data: dict):
        return cls(key, data['required'])


class BaseInfo:

    def __init__(self, key: str, name: str, description: str):
        self.key: str = key
        self.name: str = name
        self.description: str = description

        self.patch_versions: Set[str] = set()
        self.data: dict = {}

    def add_data(self, data: dict):
        self.data.update(data)

    @classmethod
    def parse(cls, key: str, data: dict):
        info = cls(key, data['name'], data['description'])
        if 'patch_versions' in data:
            info.patch_versions.update(data['patch_versions'])
        return info


class TargetInfo(BaseInfo):

    def __init__(self, key: str, name: str, description: str):
        super().__init__(key, name, description)

        self.options: Dict[str, TargetInfoOption] = {}

    @classmethod
    def parse(cls, key: str, data: dict):
        info = super().parse(key, data)
        if 'options' in data:
            for option_key, option_data in data['options'].items():
                info.options[option_key] = TargetInfoOption.parse(option_key, option_data)
        return info


class OptionInfo(BaseInfo):
    pass
