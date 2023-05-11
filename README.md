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
    
Passing 1 to the consequent (or True) is a shortcut for passing Atom(True). Likewise for 0 and False, which are shortcuts for Atom(False). 

To evaluate, we call 'evaluate' and pass it a list of 'TaggedFacts'. TaggedFacts are themselves list of 'Facts' (that are used to evaluate a theory) and what we expect to get (this can be used to compute accuracy). We can also pass a list of Facts if we don't care about the accuracy

We do it like this:

    facts = [Fact("a"), Fact("b")]
    # If we pass 'facts', we expect to return True/1
    arg = TaggedFacts(facts, Atom(True))
    # The results will be checked against the tagged results in TaggedFacts
    # obviously we can pass more than one TaggedFact
    acc = theory.accuracy_score([arg]) # Result is 1.0

    # Here we don't care about computing the accuracy score
    atoms = theory.evaluate([facts]) # Result is [Atom(True)]
     
That is, we got a single '1' (for the first and only Arguments) as a result by evaluating the theory with facts 'a' and 'b', correctly.