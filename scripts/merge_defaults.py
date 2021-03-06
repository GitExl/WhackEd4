import sys
import json


def trim_items(items, default_item):
    for item in items:

        # Remove all values that are identical to the default values.
        remove_keys = []
        for key, value in item.items():
            if key == '_index':
                continue

            if value == default_item[key]:
                remove_keys.append(key)

        for key in remove_keys:
            del item[key]

    return items


def load_defaults(filename, default_thing, default_sound, default_weapon, default_ammo, default_state):
    with open(filename, 'r') as f:
        data = json.loads(f.read())

    if 'parent' in data:
        parent = data['parent']
        default_thing, default_sound, default_weapon, default_ammo, default_state = load_defaults('cfg/{}.json'.format(parent), default_thing, default_sound, default_weapon, default_ammo, default_state)

    default_thing.update(data['defaultThing'])
    default_sound.update(data['defaultSound'])
    default_weapon.update(data['defaultWeapon'])
    default_ammo.update(data['defaultAmmo'])
    default_state.update(data['defaultState'])

    return default_thing, default_sound, default_weapon, default_ammo, default_state


def process(filename):
    default_thing = {}
    default_sound = {}
    default_weapon = {}
    default_ammo = {}
    default_state = {}

    # Load defaults from any included files.
    default_thing, default_sound, default_weapon, default_ammo, default_state = load_defaults(filename, default_thing, default_sound, default_weapon, default_ammo, default_state)

    with open(filename, 'r') as f:
        data = json.loads(f.read())

    data['things'] = trim_items(data['things'], default_thing)
    data['sounds'] = trim_items(data['sounds'], default_sound)
    data['weapons'] = trim_items(data['weapons'], default_weapon)
    data['ammo'] = trim_items(data['ammo'], default_ammo)
    data['states'] = trim_items(data['states'], default_state)

    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent='\t'))


if len(sys.argv) != 2:
    print('Not enough arguments.')
else:
    process(sys.argv[1])
