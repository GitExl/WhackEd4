"""
Contains all entry definition objects used by an engine's tables.
"""

import struct

from whacked4.dehacked.entry import Entry, Field, FieldType


class AmmoEntry(Entry):
    NAME = 'Ammo'
    FIELDS = {
        'maximum': Field('Max ammo', FieldType.INT),
        'clip':    Field('Per ammo', FieldType.INT),
    }


class ParEntry(Entry):
    NAME = 'Par'
    FIELDS = {
        'episode': Field('Episode', FieldType.INT),
        'map':     Field('Map',     FieldType.INT),
        'seconds': Field('Seconds', FieldType.INT),
    }


class SoundEntry(Entry):
    NAME = 'Sound'
    STRUCTURE = struct.Struct('<iiiiiiiii')
    FIELDS = {
        'namePointer':         Field('Offset',     FieldType.INT),
        'isSingular':          Field('Zero/One',   FieldType.INT),
        'priority':            Field('Value',      FieldType.INT),
        'linkPointer':         Field('Zero 1',     FieldType.INT),
        'linkPitch':           Field('Neg. One 1', FieldType.INT),
        'linkVolume':          Field('Neg. One 2', FieldType.INT),
        'internalDataPointer': Field('Zero 2',     FieldType.INT),
        'internalRefCount':    Field('Zero 3',     FieldType.INT),
        'internalLumpindex':   Field('Zero 4',     FieldType.INT),
    }


class StateEntry(Entry):
    NAME = 'Frame'
    STRUCTURE = struct.Struct('<iiiiiii')
    FIELDS = {
        'sprite':      Field('Sprite number',    FieldType.SPRITE),
        'spriteFrame': Field('Sprite subnumber', FieldType.INT),
        'duration':    Field('Duration',         FieldType.INT),
        'action':      Field('Action pointer',   FieldType.ACTION),
        'nextState':   Field('Next frame',       FieldType.STATE),
        'unused1':     Field('Unknown 1',        FieldType.INT),
        'unused2':     Field('Unknown 2',        FieldType.INT),
        'arg1':        Field('Args1',            FieldType.INT),
        'arg2':        Field('Args2',            FieldType.INT),
        'arg3':        Field('Args3',            FieldType.INT),
        'arg4':        Field('Args4',            FieldType.INT),
        'arg5':        Field('Args5',            FieldType.INT),
        'arg6':        Field('Args6',            FieldType.INT),
        'arg7':        Field('Args7',            FieldType.INT),
        'arg8':        Field('Args8',            FieldType.INT),
        'arg9':        Field('Args9',            FieldType.INT),
    }


class ThingEntry(Entry):
    NAME = 'Thing'
    STRUCTURE = struct.Struct('<iiiiiiiiiiiiiiiiiiiiiii')
    FIELDS = {
        'id':                   Field('ID #',                   FieldType.INT),
        'stateSpawn':           Field('Initial frame',          FieldType.INT),
        'health':               Field('Hit points',             FieldType.INT),
        'stateWalk':            Field('First moving frame',     FieldType.STATE),
        'soundAlert':           Field('Alert sound',            FieldType.SOUND),
        'reactionTime':         Field('Reaction time',          FieldType.INT),
        'soundAttack':          Field('Attack sound',           FieldType.SOUND),
        'statePain':            Field('Injury frame',           FieldType.STATE),
        'painChance':           Field('Pain chance',            FieldType.INT),
        'soundPain':            Field('Pain sound',             FieldType.SOUND),
        'stateMelee':           Field('Close attack frame',     FieldType.STATE),
        'stateAttack':          Field('Far attack frame',       FieldType.STATE),
        'stateDeath':           Field('Death frame',            FieldType.STATE),
        'stateExplode':         Field('Exploding frame',        FieldType.STATE),
        'soundDeath':           Field('Death sound',            FieldType.SOUND),
        'speed':                Field('Speed',                  FieldType.INT),
        'radius':               Field('Width',                  FieldType.INT),
        'height':               Field('Height',                 FieldType.INT),
        'mass':                 Field('Mass',                   FieldType.INT),
        'damage':               Field('Missile damage',         FieldType.INT),
        'soundActive':          Field('Action sound',           FieldType.SOUND),
        'flags':                Field('Bits',                   FieldType.FLAGS),
        'spawnId':              Field('SpawnID',                FieldType.INT),
        'game':                 Field('Game',                   FieldType.ENUM_GAME),
        'respawnTime':          Field('Respawn Time',           FieldType.INT),
        'renderStyle':          Field('Render Style',           FieldType.ENUM_RENDER_STYLE),
        'stateRaise':           Field('Respawn frame',          FieldType.STATE),
        'stateCrash':           Field('Crash frame',            FieldType.STATE),
        'stateFreeze':          Field('Ice death frame',        FieldType.STATE),
        'stateBurn':            Field('Burning death frame',    FieldType.STATE),
        'alpha':                Field('Alpha',                  FieldType.FLOAT),
        'decal':                Field('Decal',                  FieldType.STRING),
        'scale':                Field('Scale',                  FieldType.FLOAT),
        'damageFactor':         Field('DamageFactor',           FieldType.FLOAT),
        'gravity':              Field('Gravity',                FieldType.FLOAT),
        'gibHealth':            Field('Gib health',             FieldType.INT),
        'droppedItemId':        Field('Dropped item',           FieldType.INT),
        'pickupRadius':         Field('Pickup width',           FieldType.INT),
        'projectilePassHeight': Field('Projectile pass height', FieldType.INT),
        'fullbright':           Field('Fullbright',             FieldType.INT),
        'bloodId':              Field('Blood',                  FieldType.INT),
        'shadowOffset':         Field('Shadow offset',          FieldType.INT),
    }


class WeaponEntry(Entry):
    NAME = 'Weapon'
    STRUCTURE = struct.Struct('<iiiiii')
    FIELDS = {
        'ammoType':      Field('Ammo type',      FieldType.AMMO),
        'stateDeselect': Field('Deselect frame', FieldType.STATE),
        'stateSelect':   Field('Select frame',   FieldType.STATE),
        'stateBob':      Field('Bobbing frame',  FieldType.STATE),
        'stateFire':     Field('Shooting frame', FieldType.STATE),
        'stateMuzzle':   Field('Firing frame',   FieldType.STATE),
        'minAmmo':       Field('Min ammo',       FieldType.INT),
        'ammoUse':       Field('Ammo use',       FieldType.INT),
        'decal':         Field('Decal',          FieldType.STRING),
    }


class SpriteEntry(Entry):
    NAME = 'Sprite'
    STRUCTURE = None
    FIELDS = {
        'offset': Field('Offset', FieldType.INT),
    }
