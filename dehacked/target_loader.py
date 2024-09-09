from pathlib import Path
from typing import List, Tuple, Set, Dict, Optional

import jsonschema
import yaml

from dehacked.target import Target, TargetInfo


class TargetLoader:

    def __init__(self, base_path: Path, validate_jsonschema=False, validate_target=True):
        self.base_path: Path = base_path
        self.validate_jsonschema: bool = validate_jsonschema
        self.validate_target: bool = validate_target

        if self.validate_jsonschema:
            self.jsonschemas: Dict[str, dict] = {
                'target_info': self._load_jsonschema('target_info'),
                'target_data': self._load_jsonschema('target_data'),
                'option_info': self._load_jsonschema('option_info'),
            }

    def list(self) -> Dict[str, TargetInfo]:
        targets = {}

        targets_dir = self.base_path / 'targets'
        for target_dir in targets_dir.iterdir():
            target_path = target_dir / '_target.yml'
            if not target_path.exists():
                continue
            data = self._load_yaml(target_path, 'target_info')

            target_id = target_dir.stem
            targets[target_id] = TargetInfo.parse(target_id, data)

        return targets

    def load(self, target_info: TargetInfo, options: Set[str]) -> Target:
        info, data = self._load_target_yaml(target_info.id)

        # Create initial target from info.
        target = Target.from_info(target_info)

        # Load optional data.
        if 'options' in info:
            for option_key, option_data in info['options'].items():
                if not option_data['required'] and option_key not in options:
                    continue
                option_info, option_data = self._load_option_yaml(option_key)
                self._merge_data(data, option_data)

                # Patch versions overwrite all previous versions.
                if 'patch_versions' in option_info:
                    target.patch_versions = set(option_info['patch_versions'])

        # Copy Yaml data to the target.
        target.add_data(data)

        errors = target.validate()
        if len(errors) > 0:
            for error in errors:
                print(error)
            raise RuntimeError('Target validation failed.')

        return target

    def _merge_data(self, root: dict, leaf: dict):
        for key, item in leaf.items():
            if key not in root:
                root[key] = item
            else:
                if isinstance(item, dict):
                    if not isinstance(root[key], dict):
                        raise RuntimeError(
                            f'Cannot merge "{key}" dictionary data, root and leaf differ in type.')
                    self._merge_data(root[key], item)
                elif isinstance(item, list):
                    if not isinstance(root[key], list):
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
        info = self._load_yaml(info_file, jsonschema_name='target_info')

        if 'extends' in info:
            _, data = self._load_target_yaml(info['extends'])
        else:
            data = {}

        if 'load' in info:
            yaml_files = [target_path / Path(f'{yaml_name}.yml') for yaml_name in info['load']]
            self._load_data_yamls(data, yaml_files)

        return info, data

    def _load_option_yaml(self, option_id: str) -> Tuple[dict, dict]:
        option_path = self.base_path / 'options' / Path(option_id)
        info_file = option_path / Path('_option.yml')
        info = self._load_yaml(info_file, jsonschema_name='option_info')

        data = {}
        if 'load' in info:
            yaml_files = [option_path / Path(f'{yaml_name}.yml') for yaml_name in info['load']]
            self._load_data_yamls(data, yaml_files)

        return info, data

    def _load_data_yamls(self, data: dict, yaml_files):
        for file_path in yaml_files:
            leaf = self._load_yaml(file_path, jsonschema_name='target_data')

            # Clear values in existing data before merging in new data.
            if 'clear' in leaf:
                for clear_key in leaf['clear']:
                    self._clear_data(data, clear_key.split('.'))
                del leaf['clear']

            self._merge_data(data, leaf)

    def _load_yaml(self, file: Path, jsonschema_name: Optional[str]=None) -> dict:
        if not file.exists():
            raise RuntimeError(f'The file "{file}" does not exist.')

        with open(file, 'r', encoding='utf8') as f:
            data = yaml.load(f.read(), yaml.CSafeLoader)

        if self.validate_jsonschema and jsonschema_name is not None:
            jsonschema.validate(instance=data, schema=self.jsonschemas[jsonschema_name])

        return data

    def _load_jsonschema(self, name: str) -> dict:
        file_path = self.base_path / 'schema' / f'{name}.yml'
        with open(file_path, 'r', encoding='utf8') as f:
            return yaml.load(f.read(), yaml.CSafeLoader)
