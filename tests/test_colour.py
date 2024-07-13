from virus import Colour

from .assertions import assert_expected_enum_values


def test_colours() -> None:
    assert_expected_enum_values(Colour, {"Red", "Blue", "Yellow", "Green"})
