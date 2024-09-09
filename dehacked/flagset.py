from typing import Dict, Optional


class Flag:

    def __init__(self, key: str, name: str):
        self.key: str = key
        self.name: str = name

        self.index: Optional[int] = None

    @classmethod
    def parse(cls, key: str, data: dict):
        """
        Creates a new Flag instance from a data dict.

        :param key: the flag's key.
        :param data: data to create the instance with.

        :return: a new Flag instance.
        """

        if 'name' not in data:
            name = key
        else:
            name = data['name']

        flag = cls(key, name)

        if 'index' in data:
            flag.index = int(data['index'])

        return flag


class FlagSet:

    def __init__(self, key: str):
        self.key = key

        self.flags: Dict[str, Flag] = {}
        self.flag_by_index: Dict[int, Flag] = {}

    def add_flag(self, flag: Flag):
        self.flags[flag.key] = flag

        if flag.index is not None:
            self.flag_by_index[flag.index] = flag
