## Analiza ekonomskega stanja slovenskih občin

Analiziral bom določene aspekte ekonomskega stanja 210* slovenskih občin na [spletni strani Statističnega urada Republike Slovenije](https://www.stat.si/obcine) za leto 2019.

> *V Sloveniji od leta 2011 obstaja 212 občin. Zadnji novonastali sta občina Ankaran in občina Mirna, ki sta iz te analize izvzeti.

### Zajem podatkov
Za vsako občino sem zajel naslednje podatke:
 * ime občine
 * regija in upravna enota
 * površina, število prebivalcev in skupni prirast prebivalstva 
 * stopnja delovno aktivnega prebivalstva
 * neto plača na prebivalca
 * letni prihodek podjetij
 * povprečna starost avtomobilov na dan 31. december za to leto

### Delovne hipoteze
Pred začetkom sem si postavil nekaj hipotez na katera bom poskusil odgovoriti poleg drugih zanimivih opažanj, ki jih utegnem najti ob analizi:
 * Obstaja korelacija med povprečno neto plačo in delovno aktivnostjo.
 * Najnižji neto mesečni dohodki so prisotni v pomurski regiji ter jugovzhodni Sloveniji.
 * Regije so precej centralizirane na svoje mestne občine z vidika neto plače in prilivov podjetij.
 * Starost avtomobilov je skladna s povprečnim dohodkom prebivalca posamezne regije.

### Priprava podatkov
V repozitoriju se v mapi `podatki_obcine` nahajajo .html datoteke spletne strani posamezne občine. Navedeni podatki so bili s spleta naloženi z datoteko `prenesi_obcine.py`, nato pa obdelani in shranjeni s pomočjo datoteke `obdelava.py`. Surova oblika podatkov se sedaj nahaja v repozitoriju kot CSV datoteka pod imenom `obcine.csv`, ki vsebuje vse zgoraj navedene zajete podatke za 210 slovenskih občin.
