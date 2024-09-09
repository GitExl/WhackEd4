from glob import glob
from pathlib import Path

from dehacked.patch.tokenizer import Tokenizer

# target_loader = TargetLoader(Path('.'), validate_jsonschema=True)
# targets = target_loader.list()
# target = target_loader.load(targets['mbf'], {'dehextra', 'mbf21', 'dsdhacked'})


for file_path in glob('test_idgames/*'):
    with open(file_path, 'r', encoding='latin1') as f:
        text = f.read()

    tokenizer = Tokenizer(text)
    tokenizer.tokenize()

    unmatched = tokenizer.get_unmatched()
    if len(unmatched) > 0:
        print(f'*** Unmatched lines in {file_path}:')
        for line in unmatched:
            print(line)
        print()
