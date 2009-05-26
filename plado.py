
import re

class Plado:
    def __init__(self, input):
        self.clade = self._parseString(input)
    def __str__(self):
        s = str(self.clade)
        return s
    def _parseString(self, text):
        exp = '^(\*+)\s*(.*)$'
        starlist = [re.match(exp, l).groups() for l in text.split('\n')]
        numlist = map(lambda a: (len(a[0]),a[1]), starlist)
        clade = [numlist.pop(0)[1]]
        for depth, name in numlist:
            self._appendToDepth(clade, depth-2, [name])
        return clade
    def _appendToDepth(self, lst, depth, item):
        if depth == 0:
            lst.append(item)
        else:
            self._appendToDepth(lst[-1], depth-1, item)

