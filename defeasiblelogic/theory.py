from typing import List, Set, Optional
from .rule import Rule
from .superiorityrelation import SuperiorityRelation, SuperiorityRelations
from .arguments import Arguments
from .atom import Atom
from .fact import Fact


class Theory:
    def __init__(
        self, rules: List[Rule], superiority_relations: List[SuperiorityRelation]
    ) -> None:
        self.rules = rules
        self.superiority_relations = superiority_relations

    @property
    def superiority_relations(self) -> SuperiorityRelations:
        return self._superiority_relations

    @superiority_relations.setter
    def superiority_relations(self, value: List[SuperiorityRelation]) -> None:
        self._superiority_relations = SuperiorityRelations(value)

    def evaluate(self, args: List[Arguments]) -> List[Atom]:
        atoms = []
        for arg in args:
            atoms.append(self._evaluate_arguments(arg.facts))
        return atoms

    def accuracy_score(self, args: List[Arguments]) -> float:
        counter = 0
        for arg in args:
            res = self._evaluate_arguments(arg.facts)
            if res == arg.result:
                counter += 1
        return counter / len(args)

    def _evaluate_arguments(self, facts: List[Fact]) -> Atom:
        raise NotImplementedError(
            "Evaluation of arguments for general theory has not been implemented yet"
        )
