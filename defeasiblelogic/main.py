from defeasiblelogic.arguments import Arguments
from defeasiblelogic.atom import Atom
from defeasiblelogic.fact import Fact
from defeasiblelogic.proposition import Proposition
from defeasiblelogic.rule import Rule
from defeasiblelogic.superiorityrelation import SuperiorityRelation
from defeasiblelogic import ConsistentTheory


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
