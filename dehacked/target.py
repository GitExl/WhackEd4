from enum import Enum
from typing import List, Dict, Set

from dehacked.action import Action
from dehacked.dehacked_enum import DehackedEnum
from dehacked.flagset import FlagSet, Flag
from dehacked.schema import Schema
from dehacked.table import Table


class Feature(Enum):
    CLASSIC_CODEPOINTERS = 'classic_codepointers'
    CLASSIC_STRINGS = 'classic_strings'
    CLASSIC_AMMO_TYPE = 'classic_ammo_type'
    CLASSIC_FLAGS = 'classic_flags'
    EXPANDABLE = 'expandable'


class TargetInfo:

    def __init__(self, id: str, name: str, description: str, patch_versions: Set[str]):
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.patch_versions: Set[str] = patch_versions

    @classmethod
    def parse(cls, id: str, data: dict):
        return TargetInfo(id, data['name'], data['description'], data['patch_versions'])


class Target:

    def __init__(self, target_id: str, name: str, description: str, patch_versions: Set[str]):
        self.id: str = target_id
        self.name: str = name
        self.description: str = description
        self.patch_versions: Set[str] = patch_versions

        self.features: Set[Feature] = set()
        self.tables: Dict[str, Table] = {}
        self.schemas: Dict[str, Schema] = {}

        self.strings: Dict[str, str] = {}
        self.cheats: Dict[str, str] = {}
        self.actions: Dict[str, Action] = {}
        self.flagsets: Dict[str, FlagSet] = {}
        self.enums: Dict[str, DehackedEnum] = {}

        self.states_used: Set[int] = set()
        self.codepointer_to_state: List[int] = []

    @classmethod
    def from_info(cls, target_info: TargetInfo):
        return cls(
            target_info.id,
            target_info.name,
            target_info.description,
            target_info.patch_versions
        )

    def add_data(self, data: dict):
        if 'features' in data:
            for feature in data['features']:
                self.features.add(Feature(feature))
        if 'strings' in data:
            self.strings.update(data['strings'])
        if 'cheats' in data:
            self.cheats.update(data['cheats'])
        if 'states_used' in data:
            self.states_used.update(data['states_used'])
        if 'codepointer_to_state' in data:
            self.codepointer_to_state.extend(data['codepointer_to_state'])
        if 'actions' in data:
            for action_key, action_data in data['actions'].items():
                self.add_action(action_key, action_data)
        if 'flags' in data:
            for flagset_key, flagset_data in data['flags'].items():
                self.add_flagset(flagset_key, flagset_data)
        if 'enums' in data:
            for enum_key, enum_data in data['enums'].items():
                self.add_enum(enum_key, enum_data)
        if 'schema' in data:
            for schema_key, schema_data in data['schema'].items():
                self.add_schema(schema_key, schema_data)
        if 'rows' in data:
            for table_key, table_rows in data['rows'].items():
                self.add_rows(table_key, table_rows)

    def add_enum(self, key: str, data: dict):
        if key not in self.enums:
            self.enums[key] = {}

        enum = self.enums[key]
        enum.update(data)

    def add_flagset(self, key: str, data: dict):
        if key not in self.flagsets:
            self.flagsets[key] = FlagSet(key)

        flagset = self.flagsets[key]
        for flag_key, flag_data in data.items():
            flagset.add_flag(Flag.parse(flag_key, flag_data))

    def add_action(self, key: str, data: dict):
        self.actions[key] = Action.parse(key, data)

    def add_schema(self, key: str, data: dict):
        if key not in self.schemas:
            self.schemas[key] = Schema(key, self)

        schema = self.schemas[key]
        for field_key, field_data in data.items():
            schema.add_field(field_key, field_data)

    def add_rows(self, key: str, rows: dict):
        if key not in self.schemas:
            raise RuntimeError(f'Cannot add rows for unknown schema "{key}".')
        if key not in self.tables:
            self.tables[key] = Table(key, self.schemas[key], self)

        table = self.tables[key]
        for row in rows:
            table.add_row(row)

    def validate(self) -> List[str]:
        errors: List[str] = []
        for table in self.tables.values():
            errors.extend(table.validate())
        return errors
