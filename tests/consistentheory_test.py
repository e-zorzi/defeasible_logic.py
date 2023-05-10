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


class TestConsistentTheory(unittest.TestCase):
    def test_algorithm_1(self):
        """
        facts: a,b

        r1: a => 1
        r2: b => 0
        r3: a => 1

        r1 < r2
        r2 < r3

        Should return 1
        """
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
        atoms = theory.evaluate([args])
        self.assertEqual(atoms[0], Atom(True))

    def test_algorithm_2(self):
        """
        facts: a,b

        r1: a => 1
        r2: b => 0
        r3: a => 1

        r1 < r2

        Should return undefined
        """
        rule1 = Rule([Proposition("a")], consequent=1)
        rule2 = Rule([Proposition("b")], consequent=0)
        rule3 = Rule([Proposition("b")], consequent=1)
        rules = [rule1, rule2, rule3]
        sup_rels = [
            SuperiorityRelation(rule1, rule2),
        ]
        theory = ConsistentTheory(rules, sup_rels)
        facts = [Fact("a"), Fact("b")]
        args = Arguments(facts, Atom(True))
        atoms = theory.evaluate([args])
        self.assertEqual(atoms[0], Atom())

    def test_algorithm_3(self):
        """
        facts: a,b

        r1: a => 1
        r2: b => 0
        r3: a => 1

        r2 < r1
        r2 < r3

        Should return 1
        """
        rule1 = Rule([Proposition("a")], consequent=1)
        rule2 = Rule([Proposition("b")], consequent=0)
        rule3 = Rule([Proposition("b")], consequent=1)
        rules = [rule1, rule2, rule3]
        sup_rels = [
            SuperiorityRelation(rule2, rule1),
            SuperiorityRelation(rule2, rule3),
        ]
        theory = ConsistentTheory(rules, sup_rels)
        facts = [Fact("a"), Fact("b")]
        args = Arguments(facts, Atom(True))
        atoms = theory.evaluate([args])
        self.assertEqual(atoms[0], Atom(True))

    def test_algorithm_4(self):
        """
        facts: a,b

        r1: a => 1
        r2: b => 0

        r1 < r2
        r2 < r1

        Should return undefined (both 1 and 0 in plus partial)
        """
        rule1 = Rule([Proposition("a")], consequent=1)
        rule2 = Rule([Proposition("b")], consequent=0)
        rules = [rule1, rule2]
        sup_rels = [
            SuperiorityRelation(rule1, rule2),
            SuperiorityRelation(rule2, rule1),
        ]
        theory = ConsistentTheory(rules, sup_rels)
        facts = [Fact("a"), Fact("b")]
        args = Arguments(facts, Atom(True))
        atoms = theory.evaluate([args])
        self.assertEqual(atoms[0], Atom())

    def test_algorithm_5(self):
        """
        facts: a,b

        r1: a => 1
        r2: b => 0

        r1 < r2

        Should return 0
        """

        rule1 = Rule([Proposition("a")], consequent=1)
        rule2 = Rule([Proposition("b")], consequent=0)
        rules = [rule1, rule2]
        sup_rels = [
            SuperiorityRelation(rule1, rule2),
        ]
        theory = ConsistentTheory(rules, sup_rels)
        facts = [Fact("a"), Fact("b")]
        args = Arguments(facts, Atom(True))
        atoms = theory.evaluate([args])
        self.assertEqual(atoms[0], Atom(False))

    def test_arguments_passing(self):
        """
        r1: a, b => 0
        r2:    c => 1
        r3:    d => 0

        r1 < r2
        """
        rule1 = Rule([Proposition("a"), Proposition("b")], consequent=0)
        rule2 = Rule(Proposition("c"), consequent=1)
        rule3 = Rule(Proposition("d"), consequent=0)
        rules = [rule1, rule2, rule3]
        sup_rels = [
            SuperiorityRelation(rule1, rule2),
        ]
        theory = ConsistentTheory(rules, sup_rels)
        facts1 = [Fact("a"), Fact("b")]  # Should create return 0
        facts2 = [Fact("a"), Fact("b"), Fact("c")]  # Should create return 1
        facts3 = [Fact("c"), Fact("d")]  # Should create return undefined

        args1 = Arguments(facts1, Atom(False))
        args2 = Arguments(facts2, Atom(True))
        args3 = Arguments(facts3, Atom())
        atoms = theory.evaluate([args1, args2, args3])
        acc = theory.accuracy_score([args1, args2, args3])
        # They all coincide
        self.assertEqual(acc, 1.0)
