from pathlib import Path
from typing import List, Tuple, Set

import yaml

from dehacked.target import Target, Feature


class TargetLoader:

    def __init__(self, base_path: Path):
        self.base_path: Path = base_path

    def load(self, target_id: str, options: Set[str]) -> Target:
        info, data = self._load_target_yaml(target_id)

        # Create initial target from info.
        target = Target(target_id, info['name'])
        target.patch_versions = set(info['patch_versions'])
        if 'features' in info:
            for feature in info['features']:
                target.features.add(Feature(feature))

        # Load optional data.
        if 'options' in info:
            for option_key, option_data in info['options'].items():
                if not option_data['required'] and option_key not in options:
                    continue
                option_info, option_data = self._load_option_yaml(option_key)
                self._merge_data(data, option_data)

                # Option features overwrite.
                if 'patch_versions' in option_info:
                    target.patch_versions = set(option_info['patch_versions'])

        # Copy Yaml data to the target.
        if 'strings' in data:
            target.strings.update(data['strings'])
        if 'cheats' in data:
            target.cheats.update(data['cheats'])
        if 'states_used' in data:
            target.states_used.update(data['states_used'])
        if 'codepointer_to_state' in data:
            target.codepointer_to_state.extend(data['codepointer_to_state'])
        if 'actions' in data:
            for action_key, action_data in data['actions'].items():
                target.add_action(action_key, action_data)
        if 'flags' in data:
            for flagset_key, flagset_data in data['flags'].items():
                target.add_flagset(flagset_key, flagset_data)
        if 'enums' in data:
            for enum_key, enum_data in data['enums'].items():
                target.add_enum(enum_key, enum_data)
        if 'schema' in data:
            for schema_key, schema_data in data['schema'].items():
                target.add_schema(schema_key, schema_data)
        if 'data' in data:
            for table_key, table_rows in data['data'].items():
                target.add_data(table_key, table_rows)

        target.validate()

        print(info)

        return target

    def _merge_data(self, root: dict, leaf: dict):
        for key, item in leaf.items():
            if key not in root:
                root[key] = item
            else:
                if type(item) is dict:
                    if type(root[key]) is not dict:
                        raise RuntimeError(
                            f'Cannot merge "{key}" dictionary data, root and leaf differ in type.')
                    self._merge_data(root[key], item)
                elif type(item) is list:
                    if type(root[key]) is not list:
                        raise RuntimeError(
                            f'Cannot merge "{key}" list data, root and leaf differ in type.')
                    root[key].extend(item)
                else:
                    root[key] = item

    def _clear_data(self, root: dict, keys: List[str]):
        if len(keys) > 1:
            part = keys.pop(0)
            self._clear_data(root[part], keys)
        elif len(keys) == 1 and keys[0] in root:
            del root[keys[0]]

    def _load_target_yaml(self, target_id: str) -> Tuple[dict, dict]:
        target_path = self.base_path / 'targets' / Path(target_id)

        info_file = target_path / Path('_target.yml')
        if not info_file.exists():
            raise RuntimeError(f'The target "{target_id}" does not exist.')

        with open(info_file, 'r', encoding='utf8') as f:
            info = yaml.load(f.read(), yaml.CSafeLoader)

        if 'extends' in info:
            base_info, data = self._load_target_yaml(info['extends'])
        else:
            data = {}

        if 'load' in info:
            yaml_files = [target_path / Path(f'{yaml_name}.yml') for yaml_name in info['load']]
            self._load_yamls_merged(data, yaml_files)

        return info, data

    def _load_option_yaml(self, option_id: str) -> Tuple[dict, dict]:
        option_path = self.base_path / 'options' / Path(option_id)

        info_file = option_path / Path('_option.yml')
        if not info_file.exists():
            raise RuntimeError(f'The option "{option_id}" does not exist.')

        with open(info_file, 'r', encoding='utf8') as f:
            info = yaml.load(f.read(), yaml.CSafeLoader)

        data = {}
        if 'load' in info:
            yaml_files = [option_path / Path(f'{yaml_name}.yml') for yaml_name in info['load']]
            self._load_yamls_merged(data, yaml_files)

        return info, data

    def _load_yamls_merged(self, data: dict, yaml_files):
        for file_path in yaml_files:
            if not file_path.exists():
                raise RuntimeError(f'The file "{file_path}" does not exist.')
            with open(file_path, 'r', encoding='utf8') as f:
                leaf = yaml.load(f.read(), yaml.CSafeLoader)

            # Clear values in existing data before merging in new data.
            if 'clear' in leaf:
                for clear_key in leaf['clear']:
                    self._clear_data(data, clear_key.split('.'))
                del leaf['clear']

            self._merge_data(data, leaf)
