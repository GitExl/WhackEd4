from typing import List, Dict, Iterable, Sized, Optional

from whacked4.dehacked.entry import Entry
from whacked4.dehacked.table import Table


class StateQueryResult(Iterable, Sized):

    def __init__(self, state_table: Table, state_indices: List[int]):
        self.state_table: Table = state_table
        self.state_index_by_item_index: List[int] = state_indices.copy()
        self.state_index_set = set(state_indices)

        self.item_index_by_state_index: Dict[int, int] = {}
        for item_index, state_index in enumerate(state_indices):
            self.item_index_by_state_index[state_index] = item_index

        self.iter_index: int = 0

    def get_state_for_item_index(self, item_index: int) -> Optional[Entry]:
        if not len(self.state_index_by_item_index):
            return None

        return self.state_table[self.state_index_by_item_index[item_index]]

    def get_state_index_for_item_index(self, item_index: int) -> int:
        if not len(self.state_index_by_item_index):
            return -1

        return self.state_index_by_item_index[item_index]

    def get_item_index_for_state_index(self, state_index: int) -> int:
        if not len(self.item_index_by_state_index):
            return -1

        return self.item_index_by_state_index.get(state_index, -1)

    def contains_state_index(self, state_index: int) -> bool:
        return state_index in self.state_index_set

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index >= len(self.state_index_by_item_index):
            raise StopIteration

        state_index = self.state_index_by_item_index[self.iter_index]
        value = (
            self.iter_index,
            state_index,
            self.state_table[state_index]
        )
        self.iter_index += 1
        return value

    def __len__(self) -> int:
        return len(self.state_index_by_item_index)
