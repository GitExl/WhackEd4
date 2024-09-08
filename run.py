from pathlib import Path

from dehacked.target_loader import TargetLoader

target_loader = TargetLoader(Path('.'))
target_loader.load('mbf', {'dehextra', 'mbf21', 'dsdhacked'})
