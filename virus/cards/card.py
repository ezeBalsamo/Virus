from attr import field
from attr import frozen
from attr.validators import in_

from ..colour import Colour
from ..extensions.attrs.validators import not_blank
from ..type import CardType


@frozen(kw_only=True)
class Card:
    name: str = field(validator=not_blank)
    colour: Colour = field(validator=in_(Colour))
    type: CardType = field(validator=in_(CardType))
