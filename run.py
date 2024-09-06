from pathlib import Path

from dehacked.target_loader import TargetLoader

target_loader = TargetLoader(Path('targets'))
target_loader.load('dehextra')
