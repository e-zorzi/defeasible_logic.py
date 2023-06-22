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

rule1 = Rule([Proposition("a5", 0.0)], consequent=1, rule_type="strict")
rule2 = Rule([Proposition("a2", 2.0)], consequent=0)
rule3 = Rule([Proposition("a1", 2.0)], consequent=0)
rule4 = Rule(
    [Proposition("a1", 2.0), Proposition("a2", 2.0)], consequent=1, rule_type="strict"
)
rules = [
    rule4,
    rule1,
    rule3,
    rule2,
]
sup_rels = [SuperiorityRelation(rule2, rule4)]
theory = ConsistentTheory(rules, SuperiorityRelations(sup_rels))
print(theory)
facts = [
    Fact("a1", 2.0),
    Fact("a2", 2.0),
    Fact("a3", 0.0),
    Fact("a4", 0.0),
    Fact("a5", 1.0),
    Fact("a6", 1.0),
]

atoms = theory.evaluate(TaggedFacts(facts, Atom(True)))
print(atoms[0])
