from __future__ import absolute_import
__author__ = 'jamiebrew'


class Ngram(object):
    """information about a unique string within a corpus"""

    def __init__(self, token):
        self.token = token
        self.count = 1
        self.after = []

    def __str__(self):
        return str({
            'after': self.after,
            'count': self.count
        })

    def __repr__(self):
        return str({
            'after': self.after,
            'count': self.count
        })

    def __len__(self):
        return len(self.token)

    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__
        return False

    # TODO: from collections import defaultdict; defaultdict(int)
    def add_after(self, token, reach):
        if len(self.after) < reach:
            self.after.append({})
        target_dict = self.after[reach - 1]
        if token in target_dict:
            target_dict[token] += 1
        else:
            target_dict[token] = 1
