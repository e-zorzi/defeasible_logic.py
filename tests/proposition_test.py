import unittest
from defeasiblelogic import Proposition


class TestProposition(unittest.TestCase):
    def test_bad_init(self):
        # All wrong initialization, bad logic, ambiguous etc.
        with self.assertRaises(ValueError):
            Proposition("a", True, operator=">")
        with self.assertRaises(ValueError):
            Proposition("b", False, operator="<=")
        with self.assertRaises(ValueError):
            Proposition("c", [1, 2, 3], operator=">=")
        with self.assertRaises(ValueError):
            Proposition("d", [4], operator="<")
        with self.assertRaises(ValueError):
            Proposition("e", 4, operator="s=")

    def test_good_init(self):
        # When no value is passed, we assume value is True
        # if no tilde prefixes the name
        prop1 = Proposition("b")
        self.assertTrue(prop1.value)
        # Same if we pass True value and a tilde
        prop2 = Proposition("~b", True)
        self.assertTrue(prop2.value)
        # But if we pass no value and tilde prefixes the name
        # then we assume we wanted to pass False
        prop3 = Proposition("~e")
        self.assertFalse(prop3.value)
        self.assertEqual(prop3.name, "~e")
        # When passing a value, the assumed `False` value induced by
        # the tilde gets overridden
        prop4 = Proposition("~e", 10)
        self.assertEqual(prop4.value, 10)
        self.assertEqual(prop4.name, "~e")
