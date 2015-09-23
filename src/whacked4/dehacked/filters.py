#!/usr/bin/env python
#coding=utf8

"""
This module contains functions used by a Dehacked table entry to filter certain values when reading or writing
them.
"""

import math
import re


def filter_thing_flags_read(value, table, extended):
    """
    Filters a thing's flags value.

    Extended patches can use mnemonics for flag names, separated by plus signs.

    @raise LookupError: if the value contains an unknown mnemonic.
    """

    value = str(value)

    out = set()
    items = re.split(r"[,+| \t\f\r]+", value)
    for item in items:
        item = item.strip()

        # Flag is any number of bits.
        if item.isdigit():
            mnemonics = get_thing_flag_mnemonics(int(item), table)
            out.update(mnemonics)

        # Flag is a mnemonic.
        else:
            if not extended:
                raise LookupError('Encountered thing flag mnemonic {} in a non-extended patch.'.format(item))

            flag = table.flags.get(item)
            if flag is None:
                raise LookupError('Ignoring unknown thing flag {}.'.format(item))

            if 'alias' in flag:
                item = flag['alias']
                flag = table.flags.get(flag['alias'])
                if flag is None:
                    raise LookupError('Ignoring unknown thing flag alias {}.'.format(item))

            out.add(item)

    return out


def get_thing_flag_mnemonics(bits, table):
    out = set()

    for bit in range(0, 32):
        bitval = int(math.pow(2, bit))
        if (bits & bitval) == 0:
            continue

        for mnemonic, flag in table.flags.iteritems():
            if 'index' in flag and flag['index'] == bit:
                out.add(mnemonic)
                break

    return out


def filter_thing_flags_write(value, table, extended):
    """
    Returns a thing flags value as a string of mnemonics.
    """

    if extended:
        return filter_thing_flags_write_extended(value, table)
    else:
        return filter_thing_flags_write_vanilla(value, table)


def filter_thing_flags_write_vanilla(value, table):
    """
    Returns a thing flags value as a 32 bit integer bitfield.
    """

    bits = 0

    for mnemonic in value:
        flag = table.flags.get(mnemonic)
        if 'index' not in flag:
            raise LookupError('Cannot write non-bitfield thing flag {} into a non-extended patch.'.format(mnemonic))

        bits |= int(math.pow(2, flag['index']))

    return bits


def filter_thing_flags_write_extended(value, table):
    """
    Returns a thing flags value as a string of extended engine mnemonics.
    """

    out = []

    for mnemonic in value:
        if mnemonic not in table.flags:
            raise LookupError('Unknown thing flag mnemonic {}.'.format(mnemonic))

        out.append(mnemonic)

    if len(out) == 0:
        return 0

    return '+'.join(out)
