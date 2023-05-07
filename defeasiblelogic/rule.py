from .atom import Atom


class Rule:
    def __init__(self, antecedents=[], consequent=1, rule_type="defeasible"):
        self.antecedents = antecedents
        self.consequent = consequent
        self.rule_type = rule_type

    def evaluate(self, arguments):
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

    def activate(self, arguments):
        if self.evaluate(arguments):
            # Atom for which 1 and 0 are opposites
            return Atom(value=self.consequent, opposite=(self.consequent - 1) ** 2)
        else:
            # Generic (None) atom
            Atom()

    def slice_dataframe(self, df, complement=False):
        tmp = df.copy()
        for prop in self.antecedents:
            f = get_filtering_function(prop)
            mask = tmp.apply(f, axis=1)
            if complement:
                mask = ~mask
            tmp = tmp[mask == True]
        return tmp

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
