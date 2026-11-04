"""IRAC memo schema for the retrieval library."""

from __future__ import annotations

from typing import TypedDict


class Irac(TypedDict):
    folder: str
    slug: str
    title: str
    owner: str
    related: str
    issue: str
    facts: str
    rule: str
    application: str
    held: str
    copilot: str
