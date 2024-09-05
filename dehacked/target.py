from enum import Enum
from typing import List, Dict, Set

from dehacked.action import Action
from dehacked.dehacked_enum import DehackedEnum
from dehacked.flag import FlagSet, Flag
from dehacked.table import Table


class Feature(Enum):
    CLASSIC_CODEPOINTERS = 'classic_codepointers'
    CLASSIC_STRINGS = 'classic_strings'
    CLASSIC_AMMO_TYPE = 'classic_ammo_type'


class Target:

    def __init__(self, target_id: str, name: str):
        self.id: str = target_id
        self.name: str = name
        self.patch_versions: List[str] = []
        self.features: Set[Feature] = set()

        self.tables: Dict[str, Table] = {}

        self.strings: Dict[str, str] = {}
        self.cheats: Dict[str, str] = {}
        self.actions: Dict[str, Action] = {}
        self.flagsets: Dict[str, FlagSet] = {}
        self.enums: Dict[str, DehackedEnum] = {}

        self.states_used: Set[int] = set()
        self.codepointer_to_state: List[int] = []

    def add_enum(self, key: str, data: dict):
        if key not in self.enums:
            self.enums[key] = {}

        self.enums[key].update(data)

    def add_flagset(self, key: str, data: dict):
        if key not in self.flagsets:
            self.flagsets[key] = {}

        for flag_key, flag_data in data.items():
            self.flagsets[key][flag_key] = Flag.parse(key, flag_key, flag_data)

    def add_action(self, key: str, data: dict):
        self.actions[key] = Action.parse(key, data)

    def add_schema(self, key: str, data: dict):
        if key not in self.tables:
            self.tables[key] = Table(key, self)

        for field_key, field_data in data.items():
            self.tables[key].add_field(field_key, field_data)

    def add_rows(self, table_key: str, rows: list):
        if table_key not in self.tables:
            raise RuntimeError(f'Unknown table {table_key}, a schema must be defined for it.')

        table = self.tables[table_key]
        for row in rows:
            table.add_row(row)
