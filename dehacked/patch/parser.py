from typing import List, Dict, Optional

from dehacked.patch.tokens import BaseToken, HeadingToken, SectionToken, AssignmentToken, TextToken, IncludeToken, \
    ParToken


Item = Dict[str, any]


class ParserError(RuntimeError):
    pass


class Parser:

    def __init__(self, tokens: List[BaseToken]):
        self._tokens: List[BaseToken] = tokens

        self._section_key: str = 'global'
        self._sections: Dict[str, Item] = {}
        self._item: Optional[Item] = {}

    def parse(self):
        for token in self._tokens:

            # New heading for a specific item.
            if isinstance(token, HeadingToken):
                self._emit_item()
                self._section_key = token.type
                self._item = {
                    'key': token.index,
                }
                if token.name is not None:
                    self._item['name'] = token.name

            # New section, create an item for general assignments.
            elif isinstance(token, SectionToken):
                self._emit_item()
                self._section_key = token.name
                self._item = {}

            # Assignment to current item.
            elif isinstance(token, AssignmentToken):
                if self._item is not None:
                    self._item[token.key] = token.value
                else:
                    raise ParserError(f'Assignment outside of a valid section on line {token.line}.')

            # Special text replacement, combined into strings section.
            elif isinstance(token, TextToken):
                self._emit_item()
                self._section_key = 'strings'
                self._item = {
                    token.old: token.new,
                }

            # Par time.
            elif isinstance(token, ParToken):
                self._emit_item()
                self._item = {
                    'map': token.map,
                    'seconds': token.seconds,
                }
                if token.episode is not None:
                    key = f'E{token.episode}M{token.map}'
                    self._item['episode'] = token.episode
                else:
                    key = f'MAP{token.map:>02}'
                self._item['key'] = key

            # Included files.
            elif isinstance(token, IncludeToken):
                self._emit_item()
                self._section_key = 'include'
                self._item = {
                    token.file: True
                }

            else:
                token_type = token.__class__.__name__
                raise ParserError(f'Unhandled token class "{token_type}" on line {token.line}.')

        self._emit_item()

    def get_sections(self) -> Dict[str, Item]:
        return self._sections

    def _emit_item(self):
        if self._item is None:
            return

        # Create new sections.
        if self._section_key not in self._sections:
            self._sections[self._section_key] = {}

        # Items with a key are added, others are merged.
        if 'key' in self._item:
            key = self._item['key']
            del self._item['key']
            self._sections[self._section_key][key] = self._item
        else:
            self._sections[self._section_key].update(self._item)

        self._item = None
