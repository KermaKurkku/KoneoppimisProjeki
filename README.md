# Koneoppimisprojekti 2021

### HSL Kaupunkipyörien asematilanne ennustaja

## Käyttöohje
### Asennus
1. Lataa tiedostot koneellesi
2. Siirry projektikansioon
3. Asenna riippuvuudet komennolla:
```bash
pip install -r requirements.txt
```
### Mallin luonti
Jos projektissa ei ole aiemmin tallennettuja malleja, täytyy käyttö aloittaa mallin luonnista.

```
Valinta  Toiminto       
1        Algoritmin opetus
2        Validointi     
3        Käytä ohjelmaa 
0        Lopeta ohjelma 
```
Valitse ```1``` Algoritmin opetus. Ohjelma kysyy luodaanko uusi malli

```
Haluatko luoda uuden mallin? k/e
```
Vastaa ```k```

Mallin rakentaminen kestää tovin. Kun ohjelma kertoo mallista olevan valmiina 100%, on malli valmis.

Tämän jälkeen vastaamalla kysymykseen uuden mallin luonnista ```e``` pääset takaisin päävalikkoon.

Valmiit asemien mallit tallentuvat pakattuina models kansioon ja valmiit kuvaajat plots kansioon.

### Validointi
```
Valinta  Toiminto       
1        Algoritmin opetus
2        Validointi     
3        Käytä ohjelmaa 
0        Lopeta ohjelma 
```
Valitse ```2``` Validointi

Ohjelma suorittaa validoinnin ja kertoo tuloksen

### Ennusteiden hakeminen
```
Valinta  Toiminto       
1        Algoritmin opetus
2        Validointi     
3        Käytä ohjelmaa 
0        Lopeta ohjelma 
```
Valitse ```3``` Käytä ohjelmaa

Ohjelma pyytää syöttämään aseman, jolle ennustus näytetään. 
HUOM aseman nimi pitää kirjoittaa täsmälleen oikei. 
Listan asemista saat kirjoittamalla help.

Tämän jälkeen ohjelma pyytää antamaan viikonpäivää vastaavan avaimen. 
```
Avain    Viikonpäivä    
0        maanantai      
1        tiistai        
2        keskiviikko    
3        torstai        
4        perjantai      
5        lauantai       
6        sunnuntai      
```
Valitse haluamasi viikonpäivä.

Ohjelma kertoo tunneittain aseman pyörätilanteen, suhteessa viikon alkutilanteeseen.


## Opetusdata
Opetusdatana käytetään vuoden 2020 HSL:n kaupunkipyörillä ajettujen matkojen avointa dataa.

Tietoa datasta: https://www.hsl.fi/hsl/avoin-data#kaupunkipyorilla-ajetut-matkat

Linkki datan lataamiseksi: https://dev.hsl.fi/citybikes/od-trips-2020/od-trips-2020.zip

Linkki kaupunkipyöräasemien dataan: https://opendata.arcgis.com/datasets/726277c507ef4914b0aec3cbcfcbfafc_0.csv

## Devausohjeita
Kehitys tapahtuu virtuaaliympäristössä

Virtuaaliympäristön luonti
```bash
virtualenv -p python3 .envs/envname
```
envname=projektin nimi

Virtuaaliympäristön käynnistämiseksi 

```bash
cd .envs/envname
source bin/activate
```

Virtuaaliympäristön sulkemiseksi

```bash
deactivate
```

### Vaaditut ulkopuoliset kirjastot

Vaaditut kirjastot löytyvät tiedostosta requirements.txt

```bash
pip install -r requirements.txt
```

## Datan tekeminen

Lataa data HSL netisivuilta.

Datan saa muokattua sovellukselle sopivaan muotoon ajamalla convert_data skripti.

```bash
./convert_data.sh /path/to/data
```

Scripti luo sovelluksen kansioon Data kansion johon se sijoittaa station_data.csv tiedoston.

Lataa asemien data hri sivuilta

Lista asemista saa ajamalla get_stations skripti

```bash
./get_stations.sh /path/to/data
```

Skripti luo kansion Data jos sitä ei ole vielä luotu ja sijoittaa sinne stations.csv tiedoston
