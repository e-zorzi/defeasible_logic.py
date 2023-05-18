import unittest
from defeasiblelogic import (
    Rule,
    SuperiorityRelation,
    TaggedFacts,
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
        atoms = theory.evaluate([facts])
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
        arg = TaggedFacts(facts, Atom(True))
        # Test List[Arguments] passing
        atoms = theory.evaluate([arg])
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
        atoms = theory.evaluate([facts])
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
        atoms = theory.evaluate([facts])
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
        arg = TaggedFacts(facts, Atom(True))
        atoms = theory.evaluate([arg])
        self.assertEqual(atoms[0], Atom(False))

    # Correctly computes the accuracy of a single argument
    def test_algorithm_6(self):
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
        arg = TaggedFacts(facts, Atom(False))
        self.assertEqual(theory.accuracy_score(arg), 1.0)

    # Nontheless, ConsistenTheory fails if passed a list of facts to the
    # accuracy_score
    def test_algorithm_7(self):
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
        with self.assertRaises(ValueError):
            theory.accuracy_score([facts])

    def test_algorithm_strict(self):
        """
        facts: a,b

        r1: a -> 1
        r2: b => 0

        Should return 1
        """

        rule1 = Rule([Proposition("a")], consequent=1, rule_type="strict")
        rule2 = Rule([Proposition("b")], consequent=0)
        rules = [rule1, rule2]
        sup_rels = []
        theory = ConsistentTheory(rules, sup_rels)
        facts = [Fact("a"), Fact("b")]
        atoms = theory.evaluate([facts])
        self.assertEqual(atoms[0], Atom(True))

        """Should also return the same with superiority relation (it doesn't apply to strict rules)"""
        sup_rels = [SuperiorityRelation(rule1, rule2)]
        theory2 = ConsistentTheory(rules, sup_rels)

        atoms2 = theory2.evaluate([facts])
        self.assertEqual(atoms2[0], Atom(True))

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

        arg1 = TaggedFacts(facts1, Atom(False))
        arg2 = TaggedFacts(facts2, Atom(True))
        arg3 = TaggedFacts(facts3, Atom())
        atoms = theory.evaluate([arg1, arg2, arg3])
        acc = theory.accuracy_score([arg1, arg2, arg3])
        # They all coincide
        self.assertEqual(acc, 1.0)
