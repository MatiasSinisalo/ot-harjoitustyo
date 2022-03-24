import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
  
    def test_kortin_arvo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_rahan_arvo_vahanee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_rahan_arvo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_metodi_ota_rahaa_palauttaa_true_jos_rahaa_tarpeeksi(self):
        self.assertEqual( self.maksukortti.ota_rahaa(5), True)
    
    def test_metodi_ota_rahaa_palauttaa_false_jos_rahaa_ei_ole_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(50), False)
    

    