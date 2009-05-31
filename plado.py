
# coding: utf8

import re

class Plado:
    def __init__(self, input):
        if isinstance(input,list):
            self.clade = input
        elif isinstance(input,str):
            self.clade = self._parseString(input)
    def __str__(self, cl=None, offset=0):
        if not cl:
            cl = self.clade
        s = cl[0]
        if len(cl) == 2:
            s += '─' + cl[1][0]
        elif len(cl) > 2:
            s += '┬' + cl[1][0] + '\n'
            for i in cl[2:-1]:
                s += ' '*offset + ' '*len(cl[0]) + '├' + self.__str__(i) + '\n'
            s += ' '*offset + ' '*len(cl[0]) + '└' + self.__str__(cl[-1],offset+len(cl[0])+1)
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

