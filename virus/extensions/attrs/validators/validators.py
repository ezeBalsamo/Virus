from __future__ import annotations

from typing import TypeVar

from attrs import Attribute

T = TypeVar("T")


def not_blank(_instance: object, attribute: Attribute[str], value: str) -> None:
    if value.strip() == "":
        raise ValueError(f"{attribute.name} must not be blank.")
