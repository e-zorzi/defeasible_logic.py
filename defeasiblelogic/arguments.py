from typing import List
from .fact import Fact
from .atom import Atom


class Arguments:
    def __init__(self, facts: List[Fact], result: Atom) -> None:
        self.facts = facts
        self.result = result
