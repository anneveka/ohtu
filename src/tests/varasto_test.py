import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_pienempaa_kuin_nolla(self):
        varasto2 = Varasto(-1)
        self.assertAlmostEqual(varasto2.tilavuus, 0)

    def test_alkusaldo_nolla(self):
        varasto2 = Varasto(-1, -1)
        self.assertAlmostEqual(varasto2.saldo, 0)

    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otetaan_kaikki(self):
        self.varasto.lisaa_varastoon(8)
        kaikki = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(kaikki, 8)

    def test_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_tuloste(self):
        self.varasto.lisaa_varastoon(8)
        vastaus = str(self.varasto)

        self.assertAlmostEqual(vastaus, "saldo = 8, vielä tilaa 2")
