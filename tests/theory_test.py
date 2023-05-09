import unittest
from defeasiblelogic import (
    Rule,
    SuperiorityRelation,
    Arguments,
    Proposition,
    ConsistentTheory,
    Fact,
    Atom,
)


class TestTheory(unittest.TestCase):
    def test_algorithm(self):
        rule1 = Rule(Proposition("a"), consequent=1)
        rule2 = Rule(Proposition("b"), consequent=0)
        rule3 = Rule(Proposition("b"), consequent=1)
        rules = [rule1, rule2, rule3]
        sup_rels = [
            SuperiorityRelation(rule1, rule2),
            SuperiorityRelation(rule2, rule3),
        ]
        theory = ConsistentTheory(rules, sup_rels)
        facts = [Fact("a"), Fact("b")]
        args = Arguments(facts, Atom(True))
        theory.evaluate([args])
