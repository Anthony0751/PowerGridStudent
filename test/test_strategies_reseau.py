
import unittest
import xmlrunner

from Terrain import Terrain, Case
from Reseau import Reseau
from StrategieReseau import StrategieReseauAuto

class TestStrategiesReseau(unittest.TestCase):

    def test_config_auto(self):
        r = Reseau()
        r.set_strategie(StrategieReseauAuto())

        # Simuler le contenu des terrains pour éviter les dépendances externes
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]
        r.configurer(t)

        # Valider le réseau configuré
        self.assertTrue(r.valider_reseau())
        self.assertTrue(r.valider_distribution(t))

        # Charger un second exemple de terrain simulé
        t.cases = [
            [Case.ENTREE, Case.CLIENT, Case.VIDE],
            [Case.VIDE, Case.VIDE, Case.CLIENT],
        ]
        r.configurer(t)

        # Valider le réseau pour le second terrain
        self.assertTrue(r.valider_reseau())
        self.assertTrue(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))


