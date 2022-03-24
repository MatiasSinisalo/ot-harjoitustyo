import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_uuden_luokan_rahamaaara_oikea(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_uuden_luokan_edulliset_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_uuden_luokan_maukkaat_maara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_muokkaa_rahaa_oikein_tasarahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")

    def test_syo_edullisesti_kateisella_muokkaa_rahaa_oikein_ei_tasarahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
 
    def test_syo_edullisesti_kateisella_ei_muokkaa_rahaa_oikein_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_syo_edullisesti_kateisella_ei_muokkaa_myytyjen_lounaiden_maaraa_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(str(self.kassapaate.edulliset), "0")
    
    def test_syo_edullisesti_kateisella_muokkaa_myytyjen_lounaiden_maaraa_kun_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        
    def test_syo_edullisesti_kateisella_palauttaa_rahaa_oikein_ei_tasarahalla(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(260)), "20")
    
    def test_syo_edullisesti_kateisella_palauttaa_rahaa_oikein_tasarahalla(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(240)), "0")
    
    def test_syo_edullisesti_kateisella_palauttaa_rahaa_oikein_kun_raha_ei_riita(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(100)), "100")
    
    
    
       

