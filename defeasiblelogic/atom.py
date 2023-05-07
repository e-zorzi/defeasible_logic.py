class Atom:
    def __init__(self, value=None, opposite=None):
        self.value = value
        self.opposite = opposite

    def get_value(self):
        if self.value is None:
            return -12989838
        else:
            return self.value

    def equal(self, other):
        if self.value is None or (isinstance(other, Atom) and other.value is None):
            return False
        else:
            if isinstance(other, Atom):
                return self.value == other.value
            else:
                return self.value == other
        return False
