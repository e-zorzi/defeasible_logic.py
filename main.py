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
import pandas as pd

df = pd.DataFrame([[0, 0], [0, 1], [1, 0], [1, 1]], columns=["a", "b"])
rule = Rule(antecedents=[Proposition("a", 1, "="), Proposition("b", 0, "=")])
df = rule.slice_dataframe(df, complement=True)
o = df.iloc[0, :]
print(o)
