from typing import List, Optional, Union, Set
from .rule import Rule
from .superiorityrelation import SuperiorityRelation, SuperiorityRelations
from .taggedfacts import TaggedFacts
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
    def rules(self) -> Set[Rule]:
        return self.__rules

    @rules.setter
    def rules(self, value: List[Rule]) -> None:
        # Clean self string
        # self.__theory_string = "" #Add back if use string caching
        self.__rules = set(value)

    def remove_rule(self, rule: Rule, inplace: bool = False) -> Optional["Theory"]:
        try:
            self.__rules.remove(rule)
        except KeyError:
            pass
        if not inplace:
            return self

    def add_rule(self, rule: Rule, inplace: bool = False) -> Optional["Theory"]:
        # self.__theory_string = "" #Add back if use string caching
        self.rules.add(rule)
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

    def evaluate(self, facts: Union[List[List[Fact]], List[TaggedFacts]]) -> List[Atom]:
        if not isinstance(facts, list):
            # Fail safe when only one List[Fact] or TaggedFacts gets passed
            facts = [facts]
        atoms = []
        for arg in facts:
            try:
                # If args is a list of TaggedFacts
                f = arg.facts
                atoms.append(self._evaluate_arguments(f))
            except:
                # If args is a list of Fact
                atoms.append(self._evaluate_arguments(arg))
        return atoms

    def accuracy_score(self, args: List[TaggedFacts]) -> float:
        if not isinstance(args, list):
            # Fail safe when only one TaggedFacts gets passed
            args = [args]
        counter = 0
        for arg in args:
            if not isinstance(arg, TaggedFacts):
                raise ValueError("Called accuracy_score not on Arguments")
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
