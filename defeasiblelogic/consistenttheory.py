from typing import List, Set

from .util import util
from .taggedfacts import TaggedFacts
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
        # Create dict of facts with names
        facts_dict = util.facts_list_to_dict(facts)
        yea, nay = set(), set()
        for rule in self.rules:
            activated, atom = rule.activate(facts_dict)
            if activated and rule.rule_type == "defeasible":
                if atom.value:
                    yea.add(rule)
                else:
                    nay.add(rule)
            elif activated and rule.rule_type == "strict":
                if atom.value:
                    return Atom(True)
                else:
                    return Atom(False)
        if len(yea) == len(nay) and len(yea) == 0:
            return Atom()
        elif len(nay) == 0 and len(yea) > 0:
            return Atom(True)
        elif len(yea) == 0 and len(nay) > 0:
            return Atom(False)
        else:
            """
            Must break the tie. Check negative rules first to see
            whether they all are beaten by other positive rules.
            Then do the same for positive rules.
            """
            nay_all_lose = True
            for oppo in nay:
                winners = self.superiority_relations.get_winners_against(oppo)
                if len(winners.intersection(yea)) == 0:
                    nay_all_lose = False
                    break
            yea_all_lose = True
            for oppo in yea:
                winners = self.superiority_relations.get_winners_against(oppo)
                if len(winners.intersection(nay)) == 0:
                    yea_all_lose = False
                    break
            """
            Case where ALL 'nay' AND ALL 'yea' rules lose: the result would be
            that both True and False are put into +partial but we treat this as undefined 
            """
            if nay_all_lose and yea_all_lose:
                return Atom()
            if nay_all_lose:
                return Atom(True)
            if yea_all_lose:
                return Atom(False)
            # There are 'remaining' non-losers rules both for nay and yea
            return Atom()
