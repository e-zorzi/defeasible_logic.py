from typing import List, Set, Iterator, Union
from collections import defaultdict
from .rule import Rule


class SuperiorityRelation:
    def __init__(self, loser: Rule, winner: Rule) -> None:
        if not loser.has_opposite_consequent(winner):
            raise ValueError(
                "Cannot instantiate a Superiority Relation between two rules that have not opposite consequent"
            )
        self.loser = loser
        self.winner = winner

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, SuperiorityRelation):
            return False
        return self.winner == __value.winner and self.loser == __value.loser

    def __hash__(self) -> int:
        return hash((self.winner, self.loser))

    def __str__(self):
        return f"{str(self.loser)} < {str(self.winner)}"


class SuperiorityRelations:
    def __init__(
        self,
        superiority_relations: Union[
            Set[SuperiorityRelation], List[SuperiorityRelation]
        ],
    ) -> None:
        self.superiority_relations = superiority_relations

    @property
    def superiority_relations(self) -> Set[SuperiorityRelation]:
        return self.__superiority_relations

    @superiority_relations.setter
    def superiority_relations(self, value: List[SuperiorityRelation]) -> None:
        # We want a set for O(1) membership tests
        self.__superiority_relations = set(value)
        """
        Dict holding, for each rule, information about the
        rules that beat it in a set
        """
        losers = defaultdict(set)
        for sup_rel in value:
            loser = sup_rel.loser
            winner = sup_rel.winner
            losers[loser].add(winner)
        """
        Not ideal to mutate state but we need this information.
        If we don't put it here, but for example in __init__,
        then by changing superiority_relations of a SuperiorityRelations
        instance, the filed "losers" wouldn't be updated
        """
        self.losers = losers

    def get_winners_against(self, rule: Rule) -> Set[Rule]:
        return self.losers[rule]

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, SuperiorityRelations):
            return False
        return self.superiority_relations == __value.superiority_relations

    def __hash__(self) -> int:
        return hash((self.superiority_relations))

    def __iter__(self) -> Iterator[SuperiorityRelation]:
        return self.superiority_relations.__iter__()

    def __str__(self) -> str:
        sups = list(self.superiority_relations)
        if len(sups) == 0:
            return "{}"
        s = f"{str(sups[0])}"
        for i in range(1, len(sups)):
            s += f", {sups[i]}"
        # Left and right brackets
        return f"\u007b {s} \u007d"
