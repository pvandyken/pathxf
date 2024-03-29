from __future__ import annotations

from typing import TypedDict

from typing_extensions import NotRequired, TypeAlias

class OutputSpec(TypedDict):
    bids: NotRequired[dict[str, str]]

class CompSpec(TypedDict):
    when: NotRequired[dict[str, list[str]]]
    map: NotRequired[dict[str, dict[str, str]]]
    bids: NotRequired[dict[str, str]]
    conditions: NotRequired[list[CompSpec]]
    out: NotRequired[str]


class MapSpec(TypedDict):
    root: str
    out: NotRequired[str]
    all: NotRequired[dict[str, str]]
    comps: NotRequired[dict[str, CompSpec | list[CompSpec] | str]]


class Spec(TypedDict):
    input: str
    output: str
    all: NotRequired[OutputSpec]
    maps: list[MapSpec]

