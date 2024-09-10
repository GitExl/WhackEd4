from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BaseToken:
    line: int

@dataclass(frozen=True)
class HeadingToken(BaseToken):
    type: str
    index: int
    name: Optional[str] = None

    def __repr__(self):
        if self.name is not None:
            return f'HEADING: {self.type} {self.index}, "{self.name}"'
        return f'HEADING: {self.type}, {self.index}'

@dataclass(frozen=True)
class AssignmentToken(BaseToken):
    key: str
    value: str

    def __repr__(self):
        return f'ASSIGNMENT: {self.key} = {self.value}'

@dataclass(frozen=True)
class SectionToken(BaseToken):
    name: str

    def __repr__(self):
        return f'SECTION: {self.name}'

@dataclass(frozen=True)
class TextToken(BaseToken):
    old: str
    new: str

    def __repr__(self):
        return f'TEXT: "{self.old}" to "{self.new}"'

@dataclass(frozen=True)
class ParToken(BaseToken):
    seconds: int
    map: int
    episode: Optional[int] = None

    def __repr__(self):
        if self.episode is not None:
            return f'Par time: E{self.episode}M{self.map}, {self.seconds} seconds'
        return f'PAR: MAP{self.map:>02}, {self.seconds} seconds'

@dataclass(frozen=True)
class IncludeToken(BaseToken):
    file: str

    def __repr__(self):
        return f'INCLUDE: {self.file}'
