
import unittest
import plado

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

        output = ['Animalia', ['Choanoflagellata'], ['Metazoa', ['Symplama'], ['', ['Demospongiae'], ['', ['Calcarea'], ['Eumetazoa', ['Ctenophora'], ['Planulozoa', ['Cnidaria'], ['Bilateria', ['Protostomia'], ['Deuterostomia', ['Pterobranchia'], ['Echinodermata'], ['Cyrtotreta', ['Enteropneusta'], ['Chordata', ['Urochordata'], ['', ['Cephalochordata'], ['Vertebrata']]]]]]]]]]]]

        self.assertEqual(plado.Plado(input).clade, output)

if __name__ == '__main__':
    unittest.main()
