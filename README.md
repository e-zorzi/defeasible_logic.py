# defeasible_logic.py
Simple package implementing defeasible logic

# Examples
## Example 1

The following theory:

    r1: a => 1
    r2: b => 0
    r3: a => 1

    r2 < r1
    r2 < r3

Can be written as:

    rule1 = Rule([Proposition("a")], consequent=1)
    rule2 = Rule([Proposition("b")], consequent=0)
    rule3 = Rule([Proposition("b")], consequent=1)
    rules = [rule1, rule2, rule3]
    sup_rels = [
        SuperiorityRelation(rule2, rule1),
        SuperiorityRelation(rule2, rule3),
    ]
    theory = ConsistentTheory(rules, sup_rels)
    
To evaluate, we call 'evaluate' and pass it a list of 'Arguments'. Arguments are themselves list of 'Facts' (that are used to evaluate a theory) and what we expect to get (this can be used to compute accuracy). A future version will support passing only Facts if you don't care about the accuracy computation. 

We do it like this:

    facts = [Fact("a"), Fact("b")]
    args = Arguments(facts, Atom(True))
    atoms = theory.evaluate([args])

which results in:

    atoms = [Atom(True)]

That is, we got a single '1' (for the first and only Arguments) as a result by evaluating the theory with facts 'a' and 'b', correctly.