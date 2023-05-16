from defeasiblelogic.taggedfacts import TaggedFacts
from defeasiblelogic.atom import Atom
from defeasiblelogic.fact import Fact
from defeasiblelogic.proposition import Proposition
from defeasiblelogic.rule import Rule
from defeasiblelogic.superiorityrelation import (
    SuperiorityRelation,
    SuperiorityRelations,
)
from defeasiblelogic.consistenttheory import ConsistentTheory


a = Rule(Proposition("a", 3), consequent=0, rule_type="defeater")
b = Rule(Proposition("a", 3), consequent=1, rule_type="defeasible")

c = Rule(Proposition("a", 3), consequent=0, rule_type="defeater")
a == c
print(a.__hash__())
print(c.__hash__())

sup1 = SuperiorityRelation(a, b)
sup2 = SuperiorityRelation(b, c)
sups = SuperiorityRelations([sup1, sup2])
print(c.to_str_def())
