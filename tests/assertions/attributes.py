from collections.abc import Callable
from typing import Any

import pytest


def assert_attr_raises_not_blank(attr_name: str, closure: Callable[[str], Any]) -> None:
    for invalid_value in ["", " "]:
        with pytest.raises(ValueError, match=f"{attr_name} must not be blank."):
            closure(invalid_value)
