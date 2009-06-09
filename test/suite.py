
# coding: utf8

import unittest
import plado

example = ['Animalia', ['Choanoflagellata'], ['Metazoa', ['Symplama'], ['', ['Demospongiae'], ['', ['Calcarea'], ['Eumetazoa', ['Ctenophora'], ['Planulozoa', ['Cnidaria'], ['Bilateria', ['Protostomia'], ['Deuterostomia', ['Pterobranchia'], ['Echinodermata'], ['Cyrtotreta', ['Enteropneusta'], ['Chordata', ['Urochordata'], ['', ['Cephalochordata'], ['Vertebrata']]]]]]]]]]]]

class TestInput(unittest.TestCase):
    def runTest(self):
        input = '''* Animalia
** Choanoflagellata
** Metazoa
*** Symplama
***
**** Demospongiae
****
***** Calcarea
***** Eumetazoa
****** Ctenophora
****** Planulozoa
******* Cnidaria
******* Bilateria
******** Protostomia
******** Deuterostomia
********* Pterobranchia
********* Echinodermata
********* Cyrtotreta
********** Enteropneusta
********** Chordata
*********** Urochordata
***********
************ Cephalochordata
************ Vertebrata'''

        self.assertEqual(plado.Plado(input).clade, example)
        self.assertEqual(plado.Plado(example).clade, example)


class TestBasicOutput(unittest.TestCase):
    def runTest(self):
        l = ['A', ['B'], ['C']]
        s = '''A┬B
 └C'''
        self.assertEqual(str(plado.Plado(l)), s)
        l = ['A', ['B'], ['C'], ['D']]
        s = '''A┬B
 ├C
 └D'''
        self.assertEqual(str(plado.Plado(l)), s)
        l = ['A', ['B'], ['C'], ['D', 'E', 'F']]
        s = '''A┬B
 ├C
 └D┬E
   └F'''
        self.assertEqual(str(plado.Plado(l)), s)
        l = ['A', ['B'], ['C'], ['D', 'E']]
        s = '''A┬B
 ├C
 └D─E'''
        self.assertEqual(str(plado.Plado(l)), s)
        l = ['Armada', ['Bencao', 'Cocorinha', 'D', 'E'], ['Frente', ['Ginga', 'H', 'I']], ['J', 'K', 'L', 'M']]
        s = '''Armada┬Bencao┬Cocorinha
      │      ├D
      │      └E
      ├Frente─Ginga┬H
      │            └I
      └J┬K
        ├L
        └M'''
        self.assertEqual(str(plado.Plado(l)), s)
        l = ['Armada', ['Bencao', 'Cocorinha', 'D', 'E'], ['Frente', ['Ginga', 'H', 'I']], ['J', 'K', 'L', 'M']]
        s = ['Armada', ['Bencao', ['Cocorinha'], ['D'], ['E']], ['Frente', ['Ginga', ['H'], ['I']]], ['J', ['K'], ['L'], ['M']]]
        self.assertEqual(plado.Plado(l).clade, s)
        l = ['Armada', ['Bencao', 'Cocorinha', 'D', 'E'], ['Frente', ['Ginga', 'H', 'I']], ['J', 'K', 'L', 'M']]
        s = '''Armada┬Bencao┬Cocorinha
      │      ├────────D
      │      └────────E
      ├Frente─Ginga┬──H
      │            └──I
      └J┬─────────────K
        ├─────────────L
        └─────────────M'''
        self.assertEqual(plado.Plado(l).__str__(rjust=True), s)

if __name__ == '__main__':
    unittest.main()
