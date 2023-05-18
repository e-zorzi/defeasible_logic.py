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

rule1 = Rule([Proposition("a")], consequent=1, rule_type="strict")
rule2 = Rule([Proposition("b")], consequent=0)
rules = [rule1, rule2]
sup_rels = []
theory = ConsistentTheory(rules, sup_rels)
facts = [Fact("a"), Fact("b")]
atoms = theory.evaluate([facts])
