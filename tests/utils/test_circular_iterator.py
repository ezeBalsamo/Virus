import pytest

from virus.utils import CircularIterator


def test_no_items() -> None:
    with pytest.raises(StopIteration):
        CircularIterator.from_items([])
