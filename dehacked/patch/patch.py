from typing import Dict

from dehacked.table import Table
from dehacked.target import Target


class Patch:

    def __init__(self, target: Target):
        self.target: Target = target
        self.tables: Dict[str, Table] = target.tables.copy()
