## Analiza ekonomskega stanja slovenskih občin

Analiziral bom določene aspekte ekonomskega stanja 210* slovenskih občin na [spletni strani Statističnega urada Republike Slovenije](https://www.stat.si/obcine) za leto 2019.

> *V Sloveniji od leta 2011 obstaja 212 občin. Zadnji novonastali sta občina Ankaran in občina Mirna, ki sta iz te analize izvzeti.

### Zajem podatkov
Za vsako občino bom zajel naslednje podatke:
* ime občine
* regija in upravna enota
* površina, število prebivalcev in skupni prirast prebivalstva
* stopnja delovno aktivnega prebivalstva
* neto plača na prebivalca

### Delovne hipoteze
* Ali obstaja korelacija med povprečno neto plačo in letnim prirastom?
* Kje se pojavljajo skrajni primeri stopnje delovno aktivnega prebivalstva?
* Kakšni so prihodki glede na regijo in upravno enoto?

### Priprava podatkov
V repozitoriju se v mapi `podatki_obcine` nahajajo .html datoteke spletne strani posamezne občine. Navedeni podatki so bili s spleta naloženi z datoteko `prenesi_obcine.py`, nato pa obdelani in shranjeni s pomočjo datoteke `obdelava.py`. Surova oblika podatkov se sedaj nahaja v repozitoriju kot CSV datoteka pod imenom `obcine.csv`, ki vsebuje vse zgoraj navedene zajete podatke za 210 slovenskih občin.
