"""
State sorting.
"""

from typing import List

from whacked4.dehacked.patch import Patch


class StateSortBase:
    """
    State sorting base class.
    """

    def __init__(self, patch: Patch):
        self.patch: Patch = patch

    def apply(self, state_indices: List[int]) -> List[int]:
        """
        Apply this sort to a list of state indices.

        :param state_indices:
        """
