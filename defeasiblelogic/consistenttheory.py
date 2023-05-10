from typing import List, Set
from .arguments import Arguments
from .atom import Atom
from .rule import Rule
from .superiorityrelation import SuperiorityRelation
from .theory import Theory
from .fact import Fact


class ConsistentTheory(Theory):
    """A theory whose rules only evaluate to True or False"""

    def __init__(
        self, rules: List[Rule], superiority_relations: List[SuperiorityRelation]
    ) -> None:
        super().__init__(rules, superiority_relations)

    def _evaluate_arguments(self, facts: List[Fact]) -> Atom:
        yea, nay = set(), set()
        for rule in self.rules:
            atom = rule.activate(facts)
            if atom.value is not None:
                if atom.value:
                    yea.add(rule)
                else:
                    nay.add(rule)
        if len(yea) == len(nay) and len(yea) == 0:
            return Atom()
        elif len(nay) == 0 and len(yea) > 0:
            return Atom(True)
        elif len(yea) == 0 and len(nay) > 0:
            return Atom(False)
        else:
            # Must break the tie. Check positive rules first
            all_lose = True
            for oppo in nay:
                winners = self.superiority_relations.get_winners_against(oppo)
                if len(winners.intersection(yea)) == 0:
                    all_lose = False
                    break
            if all_lose:
                return Atom(True)
            all_lose = True
            for oppo in yea:
                winners = self.superiority_relations.get_winners_against(oppo)
                if len(winners.intersection(nay)) == 0:
                    all_lose = False
                    break
            if all_lose:
                return Atom(False)
            return Atom()
