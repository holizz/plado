
import re

class Plado:
    def __init__(self, input):
        if isinstance(input,list):
            self.clade = self._normaliseList(input)
        elif isinstance(input,str):
            self.clade = self._parseString(input.strip())
    def __str__(self, cl=None, offset='', rjust=None):
        stack = [(cl,offset,rjust)]
        revstack = []
        s = ''
        while True:
            while len(revstack) > 0:
                stack.append(revstack.pop())
            if len(stack) == 0:
                return s
            stuck = stack.pop()
            if isinstance(stuck,tuple):
                cl, offset, rjust = stuck
            elif isinstance(stuck,str):
                s += stuck
                continue

            if not cl:
                cl = self.clade
            if rjust == True:
                rjust = self._widestLine(cl)
            rjust = rjust if isinstance(rjust,int) else 0
            os = offset + ' '*len(cl[0])
            revstack.append(cl[0])
            if len(cl) == 1:
                s = '─'*(rjust - len(offset) - len(s)) + s
            elif len(cl) == 2:
                revstack.append('─')
                revstack.append((cl[1],os+' ',rjust))
            elif len(cl) > 2:
                revstack.append('┬')
                revstack.append((cl[1],os+'│',rjust))
                revstack.append('\n')
                for i in cl[2:-1]:
                    revstack.append(offset + ' '*len(cl[0]) + '├')
                    revstack.append((i,os+'│',rjust))
                    revstack.append('\n')
                revstack.append(offset + ' '*len(cl[0]) + '└')
                revstack.append((cl[-1],os+' ',rjust))
    def _parseString(self, text):
        exp = '^(\*+)\s*(.*)$'
        starlist = [re.match(exp, l).groups() for l in text.split('\n')]
        numlist = map(lambda a: (len(a[0]),a[1]), starlist)
        clade = []
        for depth, name in numlist:
            self._appendToDepth(clade, depth-1, [name])
        return clade[0]
    def _normaliseList(self, lst):
        if not isinstance(lst[0],str):
            raise Exception('clade names must be strings')
        newlst = [lst[0]]
        for item in lst[1:]:
            if isinstance(item,list):
                newlst.append(self._normaliseList(item))
            else:
                newlst.append([item])
        return newlst
    def _appendToDepth(self, lst, depth, item):
        while True:
            if depth == 0:
                lst.append(item)
                return
            else:
                lst = lst[-1]
                depth -= 1
    def _widestLine(self, lst):
        return max([len(l) for l in str(self).split("\n")])

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print(Plado(open(sys.argv[1]).read()).__str__(rjust=True))
    else:
        print("Usage: python3 plado.py input-file")
