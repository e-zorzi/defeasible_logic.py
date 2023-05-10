from typing import List, Set, Optional
from .rule import Rule
from .superiorityrelation import SuperiorityRelation, SuperiorityRelations
from .arguments import Arguments
from .atom import Atom
from .fact import Fact


class Theory:
    def __init__(
        self, rules: List[Rule], superiority_relations: List[SuperiorityRelation]
    ) -> None:
        # self.__theory_string = "" #Not necessary as it's already defaulted in the setters below
        self.rules = rules
        self.superiority_relations = superiority_relations

    @property
    def rules(self) -> List[Rule]:
        return self.__rules

    @rules.setter
    def rules(self, value: List[Rule]) -> None:
        # Clean self string
        # self.__theory_string = "" #Add back if use string caching
        self.__rules = value

    def add_rule(self, rule: Rule, inplace: bool = False) -> Optional["Theory"]:
        # self.__theory_string = "" #Add back if use string caching
        self.rules.append(rule)
        if not inplace:
            return self

    def add_rules(self, rules: List[Rule], inplace: bool = False) -> Optional["Theory"]:
        for rule in rules:
            # Put inplace=True so it doesn't waste time returning self each time
            self.add_rule(rule, True)
        if not inplace:
            return self

    @property
    def superiority_relations(self) -> SuperiorityRelations:
        return self.__superiority_relations

    @superiority_relations.setter
    def superiority_relations(self, value: List[SuperiorityRelation]) -> None:
        # Clean self string
        # self.__theory_string = "" #Add back if use string caching
        self.__superiority_relations = SuperiorityRelations(value)

    def evaluate(self, args: List[Arguments]) -> List[Atom]:
        atoms = []
        for arg in args:
            atoms.append(self._evaluate_arguments(arg.facts))
        return atoms

    def accuracy_score(self, args: List[Arguments]) -> float:
        counter = 0
        for arg in args:
            res = self._evaluate_arguments(arg.facts)
            if res == arg.result:
                counter += 1
        return counter / len(args)

    def _evaluate_arguments(self, facts: List[Fact]) -> Atom:
        raise NotImplementedError(
            "Evaluation of arguments for general theory has not been implemented yet"
        )

    def __str__(self):
        st = ""
        counter = 1
        namemap = dict()
        for r in self.rules:
            st += f"r{counter}: {str(r)}\n"
            namemap.update({str(r): counter})
            counter += 1
        st += "===\n"
        for s in self.superiority_relations:
            count_1 = namemap[str(s.loser)]
            count_2 = namemap[str(s.winner)]
            st += f"r{count_1} < r{count_2}\n"
        st += "==="
        return st
        """With caching
        # Cache the string
        if self.__theory_string == "":
            st = ""
            counter = 1
            namemap = dict()
            for r in self.rules:
                st += f"r{counter}: {str(r)}\n"
                namemap.update({str(r): counter})
                counter += 1
            st += "===\n"
            for s in self.superiority_relations:
                count_1 = namemap[str(s[0])]
                count_2 = namemap[str(s[1])]
                st += f"r{count_1} < r{count_2}\n"
            st += "==="
            self.__theory_string = st
        return self.__theory_string
        """
