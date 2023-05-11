from typing import List, Set, Iterator
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

    def __str__(self):
        return f"{str(self.rule_loser)} < {str(self.rule_winner)}"


class SuperiorityRelations:
    def __init__(self, superiority_relations: List[SuperiorityRelation]) -> None:
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

    def __iter__(self) -> Iterator[SuperiorityRelation]:
        return self.superiority_relations.__iter__()
