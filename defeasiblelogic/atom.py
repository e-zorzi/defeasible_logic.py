class Atom:
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self.value

    def __eq__(self, __other: object) -> bool:
        if not isinstance(__other, Atom):
            return False
        return self.value == __other.value
