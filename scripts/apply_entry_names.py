import json


FILENAME_IN = 'cfg/basetable_boom.json'
FILENAME_OUT = 'cfg/basetable_boom_new.json'


def add_names(names, items):
    for index, item in enumerate(items):
        item['_name'] = names[index]
    return items


def process(filename_in, filename_out):

    with open(filename_in, 'r') as f:
        data = json.loads(f.read())

    data['things'] = add_names(data['thingNames'], data['things'])
    del data['thingNames']

    data['sounds'] = add_names(data['soundNames'], data['sounds'])
    del data['soundNames']

    data['weapons'] = add_names(data['weaponNames'], data['weapons'])
    del data['weaponNames']

    data['ammo'] = add_names(data['ammoNames'], data['ammo'])
    del data['ammoNames']

    with open(filename_out, 'w') as f:
        f.write(json.dumps(data, indent='\t'))


process(FILENAME_IN, FILENAME_OUT)
