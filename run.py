from pathlib import Path

from dehacked.target_loader import TargetLoader

target_loader = TargetLoader(Path('.'), validate_jsonschema=True)
targets = target_loader.list()
target = target_loader.load(targets['mbf'], {'dehextra', 'mbf21', 'dsdhacked'})
