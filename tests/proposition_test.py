import unittest
from defeasiblelogic import Proposition, Rule


class TestProposition(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Proposition("a", True, operator=">")
        with self.assertRaises(ValueError):
            Proposition("b", False, operator="<=")
        with self.assertRaises(ValueError):
            Proposition("c", [1, 2, 3], operator=">=")
        with self.assertRaises(ValueError):
            Proposition("d", [4], operator="<")
        with self.assertRaises(ValueError):
            Proposition("e", 4, operator="u=")
