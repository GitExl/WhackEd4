from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BaseToken:
    pass

@dataclass(frozen=True)
class HeadingToken(BaseToken):
    type: str
    index: int
    name: Optional[str] = None

    def __repr__(self):
        if self.name is not None:
            return f'Heading: {self.type} {self.index}, "{self.name}"'
        return f'Heading: {self.type}, {self.index}'

@dataclass(frozen=True)
class AssignmentToken(BaseToken):
    key: str
    value: str

    def __repr__(self):
        return f'Assignment: {self.key} = {self.value}'

@dataclass(frozen=True)
class SectionToken(BaseToken):
    name: str

    def __repr__(self):
        return f'Section: {self.name}'

@dataclass(frozen=True)
class TextToken(BaseToken):
    old: str
    new: str

    def __repr__(self):
        return f'Old: {self.old}\nNew: {self.new}'

@dataclass(frozen=True)
class ParToken(BaseToken):
    seconds: int
    map: int
    episode: Optional[int] = None

    def __repr__(self):
        if self.episode is not None:
            return f'Par time: E{self.episode}M{self.map}, {self.seconds} seconds'
        return f'Par time: MAP{self.map:>02}, {self.seconds} seconds'

@dataclass(frozen=True)
class IncludeToken(BaseToken):
    file: str

    def __repr__(self):
        return f'Include: {self.file}'
