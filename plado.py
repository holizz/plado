
# coding: utf8

import re

class Plado:
    def __init__(self, input):
        if isinstance(input,list):
            self.clade = input
        elif isinstance(input,str):
            self.clade = self._parseString(input)
    def __str__(self):
        s = self.clade[0] + '┬' + self.clade[1][0] + '\n'
        for i in self.clade[2:-1]:
            s += ' '*len(self.clade[0]) + '├' + i[0] + '\n'
        s += ' '*len(self.clade[0]) + '└' + self.clade[-1][0]
        return s
    def _parseString(self, text):
        exp = '^(\*+)\s*(.*)$'
        starlist = [re.match(exp, l).groups() for l in text.split('\n')]
        numlist = map(lambda a: (len(a[0]),a[1]), starlist)
        clade = []
        for depth, name in numlist:
            self._appendToDepth(clade, depth-1, [name])
        return clade[0]
    def _appendToDepth(self, lst, depth, item):
        if depth == 0:
            lst.append(item)
        else:
            self._appendToDepth(lst[-1], depth-1, item)

