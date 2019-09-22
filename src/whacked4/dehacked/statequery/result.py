from typing import List

from whacked4.dehacked.entry import Entry
from whacked4.dehacked.table import Table


class StateFilterResult:

    def __init__(self, state_table: Table, state_indices: List[int]):
        self.state_table: Table = state_table
        self.state_indices: List[int] = state_indices

    def get_state_for_item_index(self, index: int) -> Entry:
        return self.state_table[self.state_indices[index]]
