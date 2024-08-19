from tests.assertions import assert_expected_enum_values
from virus.type import CardType


def test_01_card_type() -> None:
    assert_expected_enum_values(CardType, {"Organ", "Virus", "Medicine", "Treatment"})
