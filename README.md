# Koneoppimisprojekti 2021
#### HSL Kaupunkipyörien asematilanne ennustaja

## Opetusdata
Opetusdatana käytetään vuoden 2020 HSL:n kaupunkipyörillä ajettujen matkojen avointa dataa.

Tietoa datasta: https://www.hsl.fi/hsl/avoin-data#kaupunkipyorilla-ajetut-matkat

Linkki datan lataamiseksi: https://dev.hsl.fi/citybikes/od-trips-2020/od-trips-2020.zip

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
