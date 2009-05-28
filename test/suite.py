
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
        abcl = ['A', ['B'], ['C']]
        abcs = ''' ┌B
A┤
 └C'''
        self.assertEqual(str(plado.Plado(abcl)), abcs)
        abcdl = ['A', ['B'], ['C'], ['D']]
        abcds = ''' ┌B
 ├C
A┤
 └D'''
        self.assertEqual(str(plado.Plado(abcdl)), abcds)

if __name__ == '__main__':
    unittest.main()
