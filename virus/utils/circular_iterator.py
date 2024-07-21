from collections.abc import Iterator
from itertools import cycle
from typing import Self

import attr.setters
from attr import define
from attr import field


@define
class CircularIterator[T]:
    iterator: Iterator[T] = field(on_setattr=attr.setters.frozen)
    current: T = field(init=False)

    @classmethod
    def from_items(cls, items: list[T]) -> Self:
        return cls(iterator=cycle(items))

    def update_current(self) -> None:
        self.current = next(self.iterator)

    def __attrs_post_init__(self) -> None:
        self.update_current()

    def __next__(self) -> T:
        self.update_current()
        return self.current
