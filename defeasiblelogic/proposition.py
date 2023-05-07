import operator


class Proposition:
    def __init__(self, name, value, operator="="):
        self.name = name
        self.operator_string = operator
        self.operator = map_operator(operator)
        if (
            operator != "="
            and operator != "!="
            and (isinstance(value, list) or value in [True, False])
        ):
            raise
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
        raise
