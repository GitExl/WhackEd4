from pathlib import Path
from typing import List, Tuple

import yaml

from dehacked.target import Target, Feature


def merge_data(root: dict, leaf: dict):
    for key, item in leaf.items():
        if key not in root:
            root[key] = item
        else:
            if type(item) is dict:
                if type(root[key]) is not dict:
                    raise RuntimeError(f'Cannot merge "{key}" dictionary data, root and leaf differ in type.')
                merge_data(root[key], item)
            elif type(item) is list:
                if type(root[key]) is not list:
                    raise RuntimeError(f'Cannot merge "{key}" list data, root and leaf differ in type.')
                root[key].extend(item)
            else:
                root[key] = item


def clear_data(root: dict, keys: List[str]):
    if len(keys) > 1:
        part = keys.pop(0)
        clear_data(root[part], keys)
    elif len(keys) == 1 and keys[0] in root:
        del root[keys[0]]


def load_yaml(target_id: str) -> Tuple[dict, dict]:
    target_path = Path('targets') / Path(target_id)

    info_file = target_path / Path('_target.yml')
    if not info_file.exists():
        raise RuntimeError(f'The target "{target_id}" does not exist.')

    with open(info_file, 'r', encoding='utf8') as f:
        info = yaml.load(f.read(), yaml.CSafeLoader)

    if 'extends' in info:
        base_info, data = load_yaml(info['extends'])
    else:
        data = {}

    for filename in info['load']:
        file_path = target_path / Path(f'{filename}.yml')
        with open(file_path, 'r', encoding='utf8') as f:
            leaf = yaml.load(f.read(), yaml.CSafeLoader)

        if 'clear' in leaf:
            for clear_key in leaf['clear']:
                clear_data(data, clear_key.split('.'))
            del leaf['clear']

        merge_data(data, leaf)

    return info, data


def load(target_id: str) -> Target:
    info, data = load_yaml(target_id)

    target = Target(target_id, info['name'])
    target.patch_versions = info['patch_versions']

    if 'features' in info:
        for feature in info['features']:
            target.features.add(Feature(feature))
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
            target.add_rows(table_key, table_rows)

    # TODO: data, track _index

    print(data)
    print(info)

    return target
