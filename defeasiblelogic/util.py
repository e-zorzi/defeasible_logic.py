from typing import List
from collections import defaultdict
from .fact import Fact


class util:
    @staticmethod
    def facts_list_to_dict(facts: List[Fact]):
        facts_dict = defaultdict(list)
        for f in facts:
            facts_dict[f.name].append(f)
        return facts_dict
