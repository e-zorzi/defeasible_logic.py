import operator
from typing import Union, List


class Proposition:
    def __init__(
        self,
        name: str,
        value: Union[int, bool, List[int], List[bool], None] = None,
        operator: str = "=",
    ) -> None:
        self.name = name
        if value is None:
            if name.startswith("~"):
                value = False
            else:
                value = True
        self.operator_string = operator
        self.operator = map_operator(operator)
        if (
            operator != "="
            and operator != "!="
            and (isinstance(value, list) or isinstance(value, bool))
        ):
            raise ValueError(
                "Used wrong operator (only '=' and '!=' allowed) for list or boolean value"
            )
        else:
            if isinstance(value, list) and len(value) == 1:
                self.value = value[0]
            else:
                self.value = value

    def evaluate(self, arg):
        if arg.get_name() != self.name:
            return False
        # Multiple values (operator is '=')
        if isinstance(self.value, list):
            return int(arg.get_value()) in self.value
        else:
            return self.operator(int(arg.get_value()), int(self.value))
        return False

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Proposition):
            return False
        return (
            self.name == __value.name
            and self.operator == __value.operator
            and self.value == __value.value
        )

    def __hash__(self) -> int:
        if isinstance(self.value, list) or isinstance(self.value, set):
            return hash((self.name, self.operator, frozenset(self.value)))
        return hash((self.name, self.operator, self.value))

    def __str__(self):
        if isinstance(self.value, list):
            if len(self.value) == 1:
                values_string = str(self.value[0])
            else:
                values_string = str(self.value)
            return f"{self.name} {self.operator_string} {values_string}"
        else:
            if self.value == 1 or self.value == True:
                if self.operator_string == "=":
                    return f"{self.name}"
                else:
                    return f"~{self.name}"
            elif self.value == 0 or self.value == False:
                if self.operator_string == "=":
                    return f"~{self.name}"
                else:
                    return f"{self.name}"
            values_string = str(self.value)
            return f"{self.name} {self.operator_string} {values_string}"


def map_operator(op_string):
    if op_string == "=":
        return operator.eq
    elif op_string == "!=":
        return operator.ne
    elif op_string == "<":
        return operator.lt
    elif op_string == "<=":
        return operator.le
    elif op_string == ">":
        return operator.gt
    elif op_string == ">=":
        return operator.ge
    else:
        raise ValueError("Wrong type of operator")
