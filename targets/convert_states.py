import json
from strictyaml import as_document

with open('states.json', 'r') as f:
    d = json.load(f)

out = []
for state in d['states']:
    if not len(state):
        state['sprite'] = 0

    if 'action' in state:
        state['action'] = str(state['action'])

    if 'spriteFrame' in state:
        state['frame'] = state['spriteFrame']
        del state['spriteFrame']
    if 'nextState' in state:
        state['next'] = state['nextState']
        del state['nextState']

    if 'frame' in state:
        is_lit = 1 if state['frame'] & 0x8000 else 0
        if is_lit:
            state['is_lit'] = 1
            state['frame'] = state['frame'] - 0x8000

    out.append(state)

yaml = as_document(out)
print(yaml.as_yaml())
