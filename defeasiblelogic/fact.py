# TODO maybe call it Statement (naming convenction when passed to activate rules)
# (Not only facts when dealing with non-consistent theories because rules may get
# passed other rules' results
class Fact:
    def __init__(self, name, value=True):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
