import itertools
from pprint import pprint


class AccDiff:
    def __init__(self):
        self.added_data = []
        self.removed_data = []
        self.changed_data = []

    def diff(self, db_data, or_data):
        adds = list(itertools.filterfalse(lambda x: x in db_data, or_data))
        rmds = list(itertools.filterfalse(lambda x: x in or_data, db_data))
        chgds = []
        for rmdi in reversed(range(len(rmds))):
            for addi in reversed(range(len(adds))):
                if adds[addi]["Acceptance_ID"] == rmds[rmdi]["Acceptance_ID"]:
                    chgds.append(adds[addi])
                    adds.pop(addi)
                    rmds.pop(rmdi)
        self.added_data = adds
        self.removed_data = rmds
        self.changed_data = chgds
        pprint(
            {
                "add": self.added_data,
                "change": self.changed_data,
                "remove": self.removed_data,
            }
        )

    def added(self):
        return self.added_data

    def removed(self):
        return self.removed_data

    def changed(self):
        return self.changed_data
