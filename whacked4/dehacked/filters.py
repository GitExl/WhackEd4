#!/usr/bin/env python
#coding=utf8

"""
This module contains functions used by a Dehacked table entry to filter certain values when reading or writing
them.
"""

import math


def filter_thing_flags_read(value, table):
    """
    Filters a thing's flags value.
    
    Extended patches can use mnemonics for flag names, separated by plus signs.
    
    @raise LookupError: if the value contains an unknown mnemonic.
    """ 
    
    if value.find('+') == -1 and value.isalpha() == False:
        return value
    
    items = value.split('+')
    out = 0
    
    for item in items:
        item = item.strip()
        
        # Find the index of the flag mnemonic and convert it to a flag value.
        bit = -1
        for i in range(len(table.flags)):
            if table.flags.keys()[i] == item:
                bit = int(math.pow(2, i))
                
        if bit == -1:
            raise LookupError('Cannot find thing flag {}'.format(item))
        
        out += bit
        
    return out
    
    
def filter_thing_flags_write(value, table):
    """
    Returns a thing flags value as a string of mnemonics. 
    """
    
    bit = 1
    out = []
    
    for index in range(len(table.flags)):
        if value & bit > 0:
            out.append(table.flags.keys()[index])
        
        bit *= 2
        
    if len(out) == 0:
        return 0
    else:
        return '+'.join(out)