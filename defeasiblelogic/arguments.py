from typing import List
import warnings
from .fact import Fact
from .atom import Atom


class Arguments:
    def __init__(self, facts: List[Fact], result: Atom) -> None:
        if result.value is None:
            warnings.warn(
                "Be careful instantiating an Arguments object with undefined result (result.value is None)"
            )
        self.facts = facts
        self.result = result
