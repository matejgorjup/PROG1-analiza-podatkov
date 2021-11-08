import re
import requests
import orodja

STEVILO_OBCIN = 210

blok = re.compile(
    r'<div class="jumbotron ">'
    r'<a href="/obcine/sl/Municip/GroupedAll/',
    flags=re.DOTALL
)

vzorec_obcine = re.compile(
    r'<a href="/obcine/en/Municip/Index/(?P<id>\d+?)">EN</a>.*?'
    r'class="text-size-h1">\s*Občina\s(?P<ime_obcine>.*?)\s*</h1>.*?'
    r'<a href="/obcine/sl/Region/Index/\d+">\s*Regija\s(?P<regija>.*?)\s*</a>.*?'
    r'<li class="active">\s*Upravna enota\s(?P<UE>.*?)\s*</li>.*?'
    r'>Površina km.*\s*?>(?P<povrsina>.*?)</td>.*?'
    r'>Število prebivalcev.*\s*.*>(?P<prebivalstvo>.*?)</td>.*?'
    r'>Skupni prirast.*\s*.*>(?P<prirast>.*?)</td>.*?'
    r'>Stopnja delovne aktivnosti.*\s*.*>(?P<delovna_aktivnost>.*?)</td>.*?'
    r'>Povprečna mesečna neto plača.*\s*.*>(?P<placa>.*?)</td>.*?',
    flags=re.DOTALL
)

def izlusci_podatke(blok):
    obcina = vzorec_obcine.search(blok).groupdict()
    obcina['id'] = int(obcina['id'])
    obcina['povrsina'] = int(obcina['povrsina'].replace('.', ''))
    #obcina['prebivalstvo'] = int(float(obcina['prebivalstvo'].replace('.', '').replace(',', '.')))
    obcina['prirast'] = float(obcina['prirast'].replace(',', '.'))
    obcina['delovna_aktivnost'] = float(obcina['delovna_aktivnost'].replace(',', '.'))
    #obcina['placa'] = float(obcina['placa'].replace('.', '').replace(',', '.'))

    return obcina


#def obcine_iz_datotek(stevilo_obcin):
#    for i in range(stevilo_obcin):
#        ime_datoteke = f'/podatki_obcine/obcina-{i + 1}.html'
#        vsebina = orodja.vsebina_datoteke(ime_datoteke)
#        yield izloci_podatke_obcin(vzorec_obcine.finditer(vsebina))

obcine = []
for i in range(STEVILO_OBCIN):
    ime_datoteke = f'/podatki_obcine/obcina-{i + 1}.html'
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    obcine.append(izlusci_podatke(vsebina))

#if podatki_vrstica.search(vrst) == None:
#        return
#    else:
#        seznam_gesel = ['premozenje', 'zadnja_sprememba', 'zadnja_sprememba_procenti', 'letna_sprememba', 'letna_sprememba_procenti']
#        podatki_vrstice = podatki_vrstica.search(vrst).groupdict()
#        for geslo in seznam_gesel:
#            podatki_vrstice[geslo] = spremeni(podatki_vrstice[geslo])
#        return podatki_vrstice

polja = ['ID'
'Občina',
'Regija',
'Upravna enota',
'Površina',
'Število prebivalcev', 
'Skupni prirast prebivalstva', 
'Stopnja delovno aktivnega prebivalstva', 
'Neto plača na prebivalca']

orodja.zapisi_json(obcine, polja, '/PROG_analiza_podatkov/obdelani-podatki/obcine.json')
orodja.zapisi_csv(obcine, polja, '/PROG_analiza_podatkov/obdelani-podatki/obcine.csv')