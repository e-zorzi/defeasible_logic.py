from typing import List, Union, Tuple, Callable
from .atom import Atom
from .arguments import Arguments
from .fact import Fact
from .proposition import Proposition


class Rule:
    def __init__(
        self,
        antecedents: Union[Proposition, List[Proposition], None] = None,
        consequent=1,
        rule_type="defeasible",
    ):
        if antecedents is None:
            self.antecedents = list()
        elif isinstance(antecedents, Proposition):
            self.antecedents = [antecedents]
        else:
            self.antecedents = antecedents
        self.consequent = consequent
        self.rule_type = rule_type

    # TODO think of passing either facts or argument
    def evaluate(self, facts: List[Fact]) -> bool:
        for proposition in self.antecedents:
            proposition_value = False
            for arg in facts:
                if proposition.evaluate(arg):
                    proposition_value = True
                    break
            if not proposition_value:
                return False
        return True

    def add_antecedent(self, *ants):
        for ant in ants:
            self.antecedents.append(ant)

    # TODO check this interface
    def activate(self, arguments: Arguments) -> Tuple[bool, Atom]:
        if self.evaluate(arguments):
            # Activated and return result as Atom
            return True, Atom(value=self.consequent == 1)
        else:
            # Not activated; advisable to never use the second a
            # rgument in this case
            return False, Atom()

    def slice_dataframe(self, df, complement=False):
        tmp = df.copy()
        for prop in self.antecedents:
            f = get_filtering_function(prop)
            mask = tmp.apply(f, axis=1)
            if complement:
                mask = ~mask
            tmp = tmp[mask == True]
        return tmp

    def has_opposite_consequent(self, __other: object) -> bool:
        """TODO only works if rules have consequent 1 or 0"""
        if not isinstance(__other, Rule):
            return False
        if self.consequent == 1 or self.consequent == 0:
            return (self.consequent - __other.consequent) ** 2 == 1
        else:
            return False

    def __str__(self) -> str:
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


def get_filtering_function(proposition: Proposition) -> Callable:
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
