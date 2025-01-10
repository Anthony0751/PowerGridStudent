
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        
        t = Terrain()
        t.charger([
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ])
        self.assertEqual(t.cases, [
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ])

        
        # Vérifications des cases
        self.assertEqual(t.cases[0][0], Case.ENTREE)
        self.assertEqual(t.cases[1][0], Case.CLIENT)
        self.assertEqual(t.cases[1][1], Case.CLIENT)
        self.assertEqual(t.cases[1][2], Case.CLIENT)
        self.assertEqual(t.cases[0][1], Case.VIDE)
        self.assertEqual(t.cases[0][2], Case.VIDE)

    def test_accesseur(self):
        # Définir manuellement les cases du terrain
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        # Utilisation de l'accesseur pour vérifier les valeurs
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))


