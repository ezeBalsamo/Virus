import pytest

from virus.utils import CircularIterator

pepe_sand = "Pepe Sand"


def test_no_items() -> None:
    with pytest.raises(StopIteration):
        CircularIterator.from_items([])


def test_one_item() -> None:
    circular_iterator = CircularIterator.from_items([pepe_sand])

    assert circular_iterator.current == pepe_sand
    assert next(circular_iterator) == pepe_sand
    assert circular_iterator.current == pepe_sand
