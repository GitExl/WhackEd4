from __future__ import annotations

from dehacked.fieldtypes.action import ActionFieldType
from dehacked.fieldtypes.base import BaseFieldType
from dehacked.fieldtypes.bool import BoolFieldType
from dehacked.fieldtypes.enum import EnumFieldType
from dehacked.fieldtypes.fixedpoint import FixedPointFieldType
from dehacked.fieldtypes.flags import FlagsFieldType
from dehacked.fieldtypes.integer import Int32FieldType, Uint32FieldType, ByteFieldType, UbyteFieldType
from dehacked.fieldtypes.reference import ReferenceFieldType
from dehacked.fieldtypes.string import StringFieldType

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dehacked.target import Target


def create(key: str, data: dict, target: Target) -> BaseFieldType:
    type_str = data['type']

    if type_str == 'int32':
        cls = Int32FieldType
    elif type_str == 'uint32':
        cls = Uint32FieldType
    elif type_str == 'byte':
        cls = ByteFieldType
    elif type_str == 'ubyte':
        cls = UbyteFieldType
    elif type_str == 'string':
        cls = StringFieldType
    elif type_str == 'fixed':
        cls = FixedPointFieldType
    elif type_str == 'bool':
        cls = BoolFieldType
    elif type_str == 'action':
        cls = ActionFieldType
    elif type_str == 'enum':
        cls = EnumFieldType
    elif type_str == 'flags':
        cls = FlagsFieldType
    elif type_str == 'reference':
        cls = ReferenceFieldType
    else:
        raise RuntimeError(f'Unknown field type {type_str}.')

    return cls.parse(key, data, target)
