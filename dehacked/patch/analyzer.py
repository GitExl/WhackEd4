from typing import Dict, Set, Tuple

from dehacked.target import Feature
from dehacked.target_info import OptionInfo, TargetInfo, BaseInfo

PatchKeyInfo = Dict[str, Set[str]]


class Analyzer:

    def __init__(self, target_info: Dict[str, TargetInfo], option_info: Dict[str, OptionInfo]):
        self.target_info: Dict[str, TargetInfo] = target_info
        self.option_info: Dict[str, OptionInfo] = option_info

        self.patch_keys: Dict[str, PatchKeyInfo] = {}

        self._add_info(target_info, 'target')
        self._add_info(option_info, 'option')

    def get_valid_targets(self, patch_data: dict) -> Tuple[Set[str], Set[str]]:
        global_data = patch_data.get('global', None)
        if global_data is None:
            return set(), set()

        doom_version = global_data.get('doom version', None)

        # Detect some required features.
        required_features = set()
        if 'codeptr' in patch_data:
            required_features.add(Feature.EXTENDED_CODEPOINTERS.value)
        if 'strings' in patch_data:
            required_features.add(Feature.EXTENDED_STRINGS.value)

        # Test all options.
        valid_options = set()
        for option_key, option in self.option_info.items():

            # Options must support the doom version.
            if doom_version is not None and len(option.patch_versions) > 0 and doom_version not in option.patch_versions:
                print(f'Disallow option {option_key} because its doom version is not compatible.')
                continue

            # Options must support all required features.
            option_features = set(option.data.get('features', []))
            if len(option_features) > 0 and required_features.issubset(option_features):
                print(f'Disallow option {option_key} because option features are not a subset of required features.')
                continue

            valid_options.add(option_key)

        # Test all targets.
        valid_targets = set()
        for target_key, target in self.target_info.items():

            # All features must be supported.
            target_features = set(target.data.get('features', []))
            if not required_features.issubset(target_features):
                print(f'Disallow target {target_key} because required features are not a subset of target features.')
                continue

            # One of the target's options must support the doom version, or the target itself must.
            if not valid_options.issubset(target.options.keys()):
                if doom_version is not None and doom_version not in target.patch_versions:
                    print(f'Disallow target {target_key} because its doom version is not compatible and none of its options are compatible.')
                    continue

            valid_targets.add(target_key)

        return valid_targets, valid_options

    def _add_info(self, info: Dict[str, BaseInfo], type: str):
        for target_key, target in info.items():
            if 'schema' not in target.data:
                continue

            schemas = target.data['schema']
            for schema_key, schema_fields in schemas.items():
                self._add_schema(schema_fields, type, target_key)

    def _add_schema(self, schema_fields: dict, type: str, key: str):
        for field_key, field_data in schema_fields.items():
            if 'patch_key' not in field_data:
                continue

            patch_key = field_data['patch_key']
            if patch_key not in self.patch_keys:
                self.patch_keys[patch_key] = {
                    type: set(key)
                }

            if type not in self.patch_keys[patch_key]:
                self.patch_keys[patch_key][type] = set(key)
            else:
                self.patch_keys[patch_key][type].add(key)
