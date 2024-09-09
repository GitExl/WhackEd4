import re
from re import RegexFlag
from typing import List, Optional

from dehacked.patch.tokens import (BaseToken, TextToken, HeadingToken, SectionToken,
                                   AssignmentToken, ParToken, IncludeToken)


class Tokenizer:

    def __init__(self, text: str):
        self._pos: int = 0
        self._text: str = text
        self._tokens: List[BaseToken] = []
        self._unmatched: List[str] = []
        self._current_section: Optional[str] = None

        # Precompile regular expressions used for tokenizing.
        token_regexes = [
            (self._tokenize_text, r'^text (\d+)\s+(\d+)'),
            (self._tokenize_heading, r'^(thing|ammo|weapon|frame|sound|misc|sprite|cheat|pointer)\s+(\d+)(\s+\((.+)\))?'),
            (self._tokenize_section, r'^\[(.+)]'),
            (self._tokenize_assignment, r'^(.+?)\s*=\s*(.+)\s*$'),
            (self._tokenize_par, r'^par\s+(\d+)\s+(\d+)(?:\s+(\d+))?'),
            (self._tokenize_include, r'^include\s+(.+)'),
        ]
        self._regexes = []
        for regex in token_regexes:
            self._regexes.append(
                (regex[0], re.compile(regex[1], RegexFlag.IGNORECASE))
            )

    def tokenize(self):
        while 1:
            line = self._get_line()
            if line is None:
                break

            line = line.lstrip()

            # Skip empty and commented out lines.
            if line.startswith(('#', '//')):
                continue
            if len(line.rstrip()) == 0:
                continue

            # Skip header text.
            if line.startswith('Patch File for DeHackEd '):
                continue

            # Tokenize first matched regexp.
            for regexp in self._regexes:
                matched = regexp[1].match(line)
                if matched is not None:
                    regexp[0](matched)
                    break
            else:
                self._unmatched.append(line)

    def _tokenize_text(self, match: re.Match[str]):
        groups = match.groups()
        len_old = int(groups[0])
        len_new = int(groups[1])

        str_old = self._text[self._pos:self._pos + len_old]
        self._pos += len_old
        str_new = self._text[self._pos:self._pos + len_new]
        self._pos += len_new

        self._tokens.append(
            TextToken(
                old=str_old,
                new=str_new,
            )
        )

    def _tokenize_heading(self, match: re.Match[str]):
        groups = match.groups()
        heading_type = groups[0].lower()
        index = int(groups[1])
        if len(groups) == 4:
            name = groups[3]
        else:
            name = None

        self._tokens.append(
            HeadingToken(
                type=heading_type,
                index=index,
                name=name,
            )
        )

        self._current_section = heading_type

    def _tokenize_section(self, match: re.Match[str]):
        groups = match.groups()
        section = groups[0].lower()

        self._tokens.append(
            SectionToken(
                name=section,
            )
        )

        self._current_section = section

    def _tokenize_assignment(self, match: re.Match[str]):
        groups = match.groups()
        key = groups[0].lower()
        value = groups[1].rstrip()

        # Handle multiline strings.
        if self._current_section == 'strings' and value.endswith('\\'):
            lines: List[str] = [
                value[:-1]
            ]
            while 1:
                line = self._get_line()
                if line is None:
                    break
                line = line.strip()
                if line.endswith('\\'):
                    lines.append(line[:-1])
                else:
                    lines.append(line)
                    break
            value = ''.join(lines)

        self._tokens.append(
            AssignmentToken(
                key=key,
                value=value,
            )
        )

    def _tokenize_par(self, match: re.Match[str]):
        groups = match.groups()
        if len(groups) == 3:
            seconds = int(groups[1])
            map_index = int(groups[0])
            episode_index = None
        else:
            seconds = int(groups[2])
            map_index = int(groups[1])
            episode_index = int(groups[0])

        self._tokens.append(
            ParToken(
                seconds=seconds,
                map=map_index,
                episode=episode_index,
            )
        )

    def _tokenize_include(self, match: re.Match[str]):
        groups = match.groups()
        file = groups[0]

        self._tokens.append(
            IncludeToken(
                file=file,
            )
        )

    def _get_line(self) -> Optional[str]:
        if self._pos == -1:
            return None

        # Return text up until either the next newline, or end of file.
        index = self._text.find("\n", self._pos)
        if index == -1:
            text = self._text[self._pos:]
            self._pos = -1
        else:
            text = self._text[self._pos:index]
            self._pos += (index - self._pos) + 1

        return text

    def get_tokens(self) -> List[BaseToken]:
        return self._tokens

    def get_unmatched(self) -> List[str]:
        return self._unmatched
