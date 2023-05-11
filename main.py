from defeasiblelogic.taggedfacts import TaggedFacts
from defeasiblelogic.atom import Atom
from defeasiblelogic.fact import Fact
from defeasiblelogic.proposition import Proposition
from defeasiblelogic.rule import Rule
from defeasiblelogic.superiorityrelation import SuperiorityRelation
from defeasiblelogic.consistenttheory import ConsistentTheory


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

args1 = TaggedFacts(facts1, Atom(False))
args2 = TaggedFacts(facts2, Atom(True))
args3 = TaggedFacts(facts3, Atom())
atoms = theory.evaluate([args1, args2, args3])
for atom in atoms:
    print(atom)
acc = theory.accuracy_score([args1, args2, args3])
print(acc)
