#!/usr/bin/env python
#coding=utf8

"""
Contains all entry definition objects used by an engine's tables.
"""

from collections import OrderedDict
from whacked4.dehacked.entry import Entry
import struct


class AmmoEntry(Entry):
    NAME = 'Ammo'
    FIELDS = OrderedDict([
        ('maximum', 'Max ammo'),
        ('clip', 'Per ammo')
    ])


class ParEntry(Entry):
    NAME = 'Par'
    FIELDS = OrderedDict([
        ('episode', 'Episode'),
        ('map', 'Map'),
        ('seconds', 'Seconds')
    ])


class SoundEntry(Entry):
    NAME = 'Sound'
    STRUCTURE = struct.Struct('<iiiiiiiii')
    FIELDS = OrderedDict([
        ('namePointer', 'Offset'),
        ('isSingular', 'Zero/One'),
        ('priority', 'Value'),
        ('linkPointer', 'Zero 1'),
        ('linkPitch', 'Neg. One 1'),
        ('linkVolume', 'Neg. One 2'),
        ('internalDataPointer', 'Zero 2'),
        ('internalRefCount', 'Zero 3'),
        ('internalLumpindex', 'Zero 4')
    ])


class StateEntry(Entry):
    NAME = 'Frame'
    STRUCTURE = struct.Struct('<iiiiiii')
    FIELDS = OrderedDict([
        ('sprite', 'Sprite number'),
        ('spriteFrame', 'Sprite subnumber'),
        ('duration', 'Duration'),
        ('action', 'Action pointer'),
        ('nextState', 'Next frame'),
        ('unused1', 'Unknown 1'),
        ('unused2', 'Unknown 2'),
        ('arg1', 'Args1'),
        ('arg2', 'Args2'),
        ('arg3', 'Args3'),
        ('arg4', 'Args4'),
        ('arg5', 'Args5'),
        ('arg6', 'Args6'),
        ('arg7', 'Args7'),
        ('arg8', 'Args8'),
        ('arg9', 'Args9')
    ])
    SKIP = {'action'}


class ThingEntry(Entry):
    NAME = 'Thing'
    STRUCTURE = struct.Struct('<iiiiiiiiiiiiiiiiiiiiiii')
    FIELDS = OrderedDict([
        ('id', 'ID #'),
        ('stateSpawn', 'Initial frame'),
        ('health', 'Hit points'),
        ('stateWalk', 'First moving frame'),
        ('soundAlert', 'Alert sound'),
        ('reactionTime', 'Reaction time'),
        ('soundAttack', 'Attack sound'),
        ('statePain', 'Injury frame'),
        ('painChance', 'Pain chance'),
        ('soundPain', 'Pain sound'),
        ('stateMelee', 'Close attack frame'),
        ('stateAttack', 'Far attack frame'),
        ('stateDeath', 'Death frame'),
        ('stateExplode', 'Exploding frame'),
        ('soundDeath', 'Death sound'),
        ('speed', 'Speed'),
        ('radius', 'Width'),
        ('height', 'Height'),
        ('mass', 'Mass'),
        ('damage', 'Missile damage'),
        ('soundActive', 'Action sound'),
        ('flags', 'Bits'),
        ('spawnId', 'SpawnID'),
        ('game', 'Game'),
        ('respawnTime', 'Respawn Time'),
        ('renderStyle', 'Render Style'),
        ('stateRaise', 'Respawn frame'),
        ('stateCrash', 'Crash frame'),
        ('stateFreeze', 'Ice death frame'),
        ('stateBurn', 'Burning death frame'),
        ('alpha', 'Alpha'),
        ('decal', 'Decal'),
        ('scale', 'Scale'),
    ])
    FILTER = {
        'flags': 'filter_thing_flags'
    }


class WeaponEntry(Entry):
    NAME = 'Weapon'
    STRUCTURE = struct.Struct('<iiiiii')
    FIELDS = OrderedDict([
        ('ammoType', 'Ammo type'),
        ('stateDeselect', 'Deselect frame'),
        ('stateSelect', 'Select frame'),
        ('stateBob', 'Bobbing frame'),
        ('stateFire', 'Shooting frame'),
        ('stateMuzzle', 'Firing frame')
    ])


class SpriteEntry(Entry):
    NAME = 'Sprite'
    STRUCTURE = None
    FIELDS = OrderedDict([
        ('offset', 'Offset')
    ])
