# Koneoppimisprojekti 2021
#### HSL Kaupunkipyörien asematilanne ennustaja

## Opetusdata
Opetusdatana käytetään vuoden 2020 HSL:n kaupunkipyörillä ajettujen matkojen avointa dataa.

Tietoa datasta: https://www.hsl.fi/hsl/avoin-data#kaupunkipyorilla-ajetut-matkat

Linkki datan lataamiseksi: https://dev.hsl.fi/citybikes/od-trips-2020/od-trips-2020.zip

Linkki kaupunkipyöräasemien dataan: https://hri.fi/data/fi/dataset/hsl-n-kaupunkipyoraasemat

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
