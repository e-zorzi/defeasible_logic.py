import unittest
from defeasiblelogic import (
    Rule,
    Proposition,
    ConsistentTheory,
    Fact,
    Atom,
)


class TestRule(unittest.TestCase):
    def test_evaluation(self):
        propositions = [Proposition("a"), Proposition("b", 4, operator="<=")]
        rule = Rule(antecedents=propositions, consequent=1)

        activated, atom = rule.activate([Fact("a")])
        self.assertFalse(activated)
        self.assertEqual(atom, Atom())

        activated, atom = rule.activate([Fact("b", 4)])
        self.assertFalse(activated)
        self.assertEqual(atom, Atom())

        activated, atom = rule.activate([Fact("a"), Fact("b", 4)])
        self.assertTrue(activated)
        self.assertEqual(atom, Atom(True))

        activated, atom = rule.activate([Fact("b", 4), Fact("b", 5), Fact("a")])
        self.assertTrue(activated)
        self.assertEqual(atom, Atom(True))

        facts4 = [Fact("a"), Fact("b", 5)]
        activated, atom = rule.activate(facts4)
        self.assertFalse(activated)
        self.assertEqual(atom, Atom())

        # New rule, opposite consequent
        rule2 = Rule(antecedents=propositions, consequent=0)

        activated, atom = rule2.activate([Fact("a"), Fact("b", 4)])
        self.assertTrue(activated)
        self.assertEqual(atom, Atom(False))
