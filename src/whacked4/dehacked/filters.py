#!/usr/bin/env python
#coding=utf8

"""
This module contains functions used by a Dehacked table entry to filter certain values when reading or writing
them.
"""

import math
import re


def filter_thing_flags_read(value, table):
    """
    Filters a thing's flags value.

    Extended patches can use mnemonics for flag names, separated by plus signs.

    @raise LookupError: if the value contains an unknown mnemonic.
        """

    if value.isdigit():
        return value

    items = re.split(r"[,+| \t\f\r]+", value)
    out = 0

    for item in items:
        item = item.strip()

        # Find the index of the flag mnemonic and convert it to a flag value.
        flag = table.flags.get(item)
        if flag is None:
            raise LookupError('Ignoring unknown thing flag {}.'.format(item))
        bit = int(math.pow(2, flag['index']))
        out += bit

    return out


def filter_thing_flags_write(value, table):
    """
    Returns a thing flags value as a string of mnemonics.
    """

    bit = 1
    out = []

    for _ in range(0, 32):
        if (value & bit) == 0:
            bit *= 2
            continue

        for key, flag in table.flags.iteritems():
            if int(math.pow(2, flag['index'])) == bit:
                out.append(key)
                break

        bit *= 2

    if len(out) == 0:
        return 0
    else:
        return '+'.join(out)
