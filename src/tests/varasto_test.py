import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virheellinen_varasto = Varasto(-1, -1)
        self.liian_suuri_alkusaldo = Varasto(1, 2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_varaston_oikein_virheellisella_tilavuudella(self):
        self.assertAlmostEqual(self.virheellinen_varasto.tilavuus, 0)

    def test_konstruktori_luo_varaston_oikein_virheellisella_alkusaldolla(self):
        self.assertAlmostEqual(self.virheellinen_varasto.saldo, 0)

    def test_konstruktori_luo_varaston_oikein_liian_suurella_alkusaldolla(self):
        self.assertAlmostEqual(self.liian_suuri_alkusaldo.saldo, 1)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivisen_maaran_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_suuren_maaran_lisays_ei_tayta_yli(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_maaran_ottaminen_ei_ota_mitaan(self):
        self.varasto.saldo = 1
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)
        self.assertAlmostEqual(self.varasto.saldo, 1)

    def test_kaiken_ottaminen_toimii_oikein(self):
        self.varasto.saldo = 1
        self.assertAlmostEqual(self.varasto.ota_varastosta(2), 1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test___str___palauttaa_oikean_arvon(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

