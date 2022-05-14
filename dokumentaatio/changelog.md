# Viikko 7  
Käyttäjä voi tallentaa taulukon .json tiedostoon ja avata tallentamansa taulukon.   
Testit tarkistavat raahaamalla ruutujen valitsemisen.  



# Viikko 6  

Taulukon ruutujen tiedot ja kaaviot tallentuvat test.json tiedostoon.  

Käyttäjä voi asettaa kaaviolle otsikot.  

Testit kattavat ruutujen ja kaavioiden tallentamisen tiedostoon.  


# Viikko 5  

Käyttäjä voi luoda lisäämästään tiedosta piirakkakaavion  

Käyttäjä voi laskea valitsemistaan arvoista summan ja keskiarvon 

testit kattavat piirakkakaavion luomisen ja raahauksen.

testit kattavat summan ja keskiarvon laskemisen

# Viikko 4  

Käyttäjä voi luoda lisäämästään tiedosta pylväskaavion:  
1. syötä tietoa taulukon sarakkeeseen tai riviin  
2. valitse tieto painamalla SHIFT ja raahaamalla hiirtä  
3. klikkaa "aseta kaavion x arvo"  
4. toista sama, mutta paina "aseta kaavion y arvo"  
5. paina "lisaa uusi pylvaskaavio"  

Käyttäjä voi raahata pylväskaavioita ruudukossa  

Käyttäjä voi poistaa pylväskaavion klikkaamalla kaaviota jonka hän haluaa poistaa ja painamalla DELETE  

Testit tarkistavat matplotlib_graphs moduulin toiminnallisuudesta pylvaskaavion luomisen ja kaavion raahaamisen  

# Viikko 3  
- sovelluksessa on toimiva spreadsheet tyylinen käyttöliittymä, missä käyttäjä voi muokata ruutujen arvoja klikkaamalla haluamaansa ruutua ja syöttämällä tekstiä.  
- GridDisplay luokka huolehtii ruudukon piirtämisestä, kun sille annetaan Tkinter Canvas olio  
- Testit tarkistavat että clikkaukset rekisteröityvät oikein GridDisplay luokkaan  
