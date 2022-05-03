# Arkkitehtuuri kuvaus


## Luokkarakenne:  

![uml class graph-Page-1 drawio](https://user-images.githubusercontent.com/50097749/166499396-05e39188-35c1-46cc-9bf5-adc2b07ceeee.png)


## Sovelluksen logiikka


### SpreadSheetApp
- Sovelluksen pääluokka
- Vastaa sovelluksen alustuksesta
- Vastaa sovelluksen tilan tallentamisesta oikeassa muodossa, sekä sovelluksen tilan palautuksesta jos tallennustiedosto on olemassa. 


### GridDisplay
- Vastaa taulukon ruutujen piirtämisestä ja valitsemisesta
- tarjoaa valittujen ruutujen summan ja keskiarvojen laskemisen
- GridDisplay.cellGridValues säilöö taulukon ruutujen arvot hajautustauluun
- GridDisplay.cell_grid_number_by_text_id yhdistää tkinter kirjaston luoman teksti id:n taulukon ruudun numeroon
- Ruudun teksti viittaa tällöin GridDisplay.cellGridValuesin arvoihin 

![references](https://user-images.githubusercontent.com/50097749/166494880-d342eed2-6e5d-445d-8e88-d4d00dee9879.png)

- Tallennettaessa GridDisplay luokan GridDisplay.cellGridValues tallennetaan testi.json tiedostoon.


### ChartManager  
- Toimii rajapintana matplotlib kirjaston tarjoamien kaavioiden piirämiselle ja luomiselle
- Pitää kirjaa sovelluksessa olevista tauluista.
- Vastaa taulujen poistamisesta ja liikuttamisesta.

### CanvasConfigView
- Vastaa sovelluksen oikean palkin UI:n toiminnallisuuden toteutuksesta
- Sisältää kaksi alaluokkaa: 
  #### CanvasChartCreatorView
  - Vastaa sovelluksen taulukoiden luomisen UI:n toiminnalliuuden toteutuksesta

  #### CanvasChartCalculationsView
  - Vastaa sovelluksen laskutoimituksien UI:n toteutuksesta





