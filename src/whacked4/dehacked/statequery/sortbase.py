from typing import List

from whacked4.dehacked.patch import Patch


class StateSortBase:

    def __init__(self, patch: Patch):
        self.patch: Patch = patch

    def apply(self, state_indices: List[int]) -> List[int]:
        pass
