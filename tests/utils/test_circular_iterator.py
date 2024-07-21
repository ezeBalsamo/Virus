import pytest

from virus.utils import CircularIterator

pepe_sand = "Pepe Sand"
lautaro_acosta = "Lautaro Acosta"
diego_valeri = "Diego Valeri"


def test_no_items() -> None:
    with pytest.raises(StopIteration):
        CircularIterator.from_items([])


def test_one_item() -> None:
    circular_iterator = CircularIterator.from_items([pepe_sand])

    assert circular_iterator.current == pepe_sand
    assert next(circular_iterator) == pepe_sand
    assert circular_iterator.current == pepe_sand


def test_many_items() -> None:
    items = [pepe_sand, lautaro_acosta, diego_valeri]
    circular_iterator = CircularIterator.from_items(items)

    assert circular_iterator.current == pepe_sand

    assert next(circular_iterator) == lautaro_acosta
    assert circular_iterator.current == lautaro_acosta

    assert next(circular_iterator) == diego_valeri
    assert circular_iterator.current == diego_valeri

    assert next(circular_iterator) == pepe_sand
    assert circular_iterator.current == pepe_sand
