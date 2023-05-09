from typing import List, Set, Optional
from .rule import Rule
from .superiorityrelation import SuperiorityRelation, SuperiorityRelations
from .arguments import Arguments
from .atom import Atom


class Theory:
    def __init__(
        self, rules: List[Rule], superiority_relations: List[SuperiorityRelation]
    ) -> None:
        self.rules = rules
        self.superiority_relations = superiority_relations

    @property
    def superiority_relations(self) -> SuperiorityRelations:
        return self.superiority_relations

    @superiority_relations.setter
    def superiority_relations(self, value: List[SuperiorityRelation]) -> None:
        self.superiority_relations = SuperiorityRelations(value)

    def evaluate(self, args: List[Arguments]) -> List[Atom]:
        atoms = []
        for arg in args:
            atoms.append(self._evaluate_arguments(arg))
        return atoms

    def evaluate_arguments(self, args: Arguments) -> Atom:
        raise NotImplementedError(
            "Evaluation of arguments for general theory has not been implemented yet"
        )
