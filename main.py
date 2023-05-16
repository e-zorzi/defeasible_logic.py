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

best_name = "odor"
best_l_ant = [0.0, 1.0, 3.0]
best_gini_l = 0.00
rule = Rule(
    antecedents=[Proposition(best_name, best_l_ant, operator="=")],
    consequent=0,
    rule_type=("strict" if best_gini_l == 0 else "defeasible"),
)
rule2 = Rule(
    antecedents=[Proposition("a")],
    consequent=0,
    rule_type=("strict" if best_gini_l == 0 else "defeasible"),
)

rule.add_antecedent(rule2.antecedents)
print(rule)
