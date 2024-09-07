from virus.cards import Card
from virus.colour import Colour
from virus.type import CardType

from .assertions import assert_attr_raises_not_blank


def test_01_name_must_not_be_blank() -> None:
    assert_attr_raises_not_blank(
        "name",
        lambda invalid_name: Card(
            name=invalid_name, colour=Colour.BLUE, type=CardType.ORGAN
        ),
    )


def test_02_instance_creation_and_accessing() -> None:
    card = Card(name="Brain", colour=Colour.BLUE, type=CardType.ORGAN)
    assert card.name == "Brain"
    assert card.colour == Colour.BLUE
    assert card.type == CardType.ORGAN
