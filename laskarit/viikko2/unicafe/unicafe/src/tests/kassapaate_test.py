import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1200)
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
    
    def test_syo_maukkaasti_kateisella_muokkaa_rahaa_oikein_tasarahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")

    def test_syo_maukkaasti_kateisella_muokkaa_rahaa_oikein_ei_tasarahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
 
    def test_syo_maukkaasti_kateisella_ei_muokkaa_rahaa_oikein_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_syo_maukkaasti_kateisella_ei_muokkaa_myytyjen_lounaiden_maaraa_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_syo_maukkaasti_kateisella_muokkaa_myytyjen_lounaiden_maaraa_kun_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        
    def test_syo_maukkaasti_kateisella_palauttaa_rahaa_oikein_ei_tasarahalla(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(460)), "60")
    
    def test_syo_maukkaasti_kateisella_palauttaa_rahaa_oikein_tasarahalla(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(400)), "0")
    
    def test_syo_maukkaasti_kateisella_palauttaa_rahaa_oikein_kun_raha_ei_riita(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(100)), "100")
    
    def test_syo_edullisesti_kortilla_veloittaa_oikein_tasarahalla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_syo_edullisesti_kortilla_veloittaa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 9.6")
   
    def test_syo_edullisesti_kortilla_kasvattaa_edullisten_maaraa_kun_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_kasvata_edullisten_maaraa_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100))
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_kortilla_ei_muuta_kortin_arvoa_kun_kun_raha_ei_riita(self):
        testiKortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(testiKortti)
        self.assertEqual(testiKortti.saldo, 100)

    def test_syo_edullisesti_kortilla_palauttaa_true_jos_raha_riittaa(self):
         self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortilla_palauttaa_false_jos_raha_ei_riita(self):
         self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100)), False)

    def test_syo_edullisesti_kortilla_ei_muuta_kassan_arvoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kortilla_veloittaa_oikein_tasarahalla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) 
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_syo_maukkaasti_kortilla_veloittaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 8.0")

    def test_syo_maukkaasti_kortilla_kasvattaa_maukkaiden_maaraa_kun_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_kasvata_maukkaiden_maaraa_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100))
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_ei_muuta_kortin_arvoa_kun_kun_raha_ei_riita(self):
        testiKortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(testiKortti)
        self.assertEqual(testiKortti.saldo, 100)

    def test_syo_maukkaasti_kortilla_palauttaa_true_jos_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_palauttaa_false_jos_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100)), False)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassan_arvoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)