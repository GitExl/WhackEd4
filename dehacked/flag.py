from typing import Dict, Optional


class Flag:

    def __init__(self, key: str, name: str):
        self.key: str = key
        self.name: str = name

        self.index: Optional[int] = None

    @classmethod
    def parse(cls, flagset_key: str, key: str, data: dict):
        """
        Creates a new Flag instance from a data dict.

        :param flagset_key: the key of the flagset this flag belongs to.
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


FlagSet = Dict[str, Flag]
