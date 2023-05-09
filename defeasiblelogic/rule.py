from typing import Optional
from .atom import Atom
from .arguments import Arguments


class Rule:
    def __init__(self, antecedents=[], consequent=1, rule_type="defeasible"):
        self.antecedents = antecedents
        self.consequent = consequent
        self.rule_type = rule_type

    def evaluate(self, arguments: Arguments) -> bool:
        for proposition in self.antecedents:
            proposition_value = False
            for arg in arguments:
                proposition_value |= proposition.evaluate(arg)
                if proposition_value:
                    break
            if not proposition_value:
                return False
        return True

    def add_antecedent(self, *ants):
        for ant in ants:
            self.antecedents.append(ant)

    def activate(self, arguments: Arguments) -> Optional[Atom]:
        if self.evaluate(arguments):
            # Atom for which 1 and 0 are opposites
            return Atom(value=self.consequent == 1, opposite=self.consequent == 0)
        else:
            # Generic (None) atom
            return None

    def slice_dataframe(self, df, complement=False):
        tmp = df.copy()
        for prop in self.antecedents:
            f = get_filtering_function(prop)
            mask = tmp.apply(f, axis=1)
            if complement:
                mask = ~mask
            tmp = tmp[mask == True]
        return tmp

    def has_opposite_consequent(self, __other: object):
        """TODO only works if rules have consequent 1 or 0"""
        if not isinstance(__other, Rule):
            return False
        if self.consequent == 1 or self.consequent == 0:
            return (self.consequent - __other.consequent) ** 2 == 1
        else:
            return False

    def __str__(self):
        arrow = (
            "=>"
            if self.rule_type == "defeasible"
            else "->"
            if self.rule_type == "strict"
            else "~>"
        )
        if len(self.antecedents) == 0:
            return f"{arrow} {self.consequent}"
        else:
            str_antecedents = f"{str(self.antecedents[0])}"
            for i in range(1, len(self.antecedents)):
                str_antecedents += f", {str(self.antecedents[1])}"
            return f"{str_antecedents} {arrow} {self.consequent}"


def get_filtering_function(proposition):
    if proposition.operator_string == "=":
        if isinstance(proposition.value, list):
            return lambda x: x[proposition.name] in (proposition.value)
        else:
            return lambda x: x[proposition.name] == proposition.value
    elif proposition.operator_string == "!=":
        if isinstance(proposition.value, list):
            return lambda x: x[proposition.name] not in proposition.value
        else:
            return lambda x: x[proposition.name] != proposition.value
    elif proposition.operator_string == ">":
        return lambda x: x[proposition.name] > proposition.value
    elif proposition.operator_string == ">=":
        return lambda x: x[proposition.name] >= proposition.value
    elif proposition.operator_string == "<":
        return lambda x: x[proposition.name] < proposition.value
    elif proposition.operator_string == "<=":
        return lambda x: x[proposition.name] <= proposition.value
    else:
        raise
