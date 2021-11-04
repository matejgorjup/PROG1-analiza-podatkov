import re
import requests
import orodja

STEVILO_OBCIN = 210

blok = re.compile(
    r'<div class="jumbotron ">'
    r'<a href="/obcine/sl/Municip/GroupedAll/210">',
    flags=re.DOTALL
)

vzorec_obcine = re.compile(
    r'class="text-size-h1">\s*Občina\s(?P<ime_obcine>.*?)\s*</h1>'
    r'<a href="/obcine/sl/Region/Index/\d+">\s*Regija\s(?P<regija>.*?)\s*</a>'
    r'<li class="active">\s*Upravna enota\s(?P<UE>.*?)\s*</li>'
    r'>Površina km.*\s*?>(?P<povrsina>.*?)</td>'
    r'>Število prebivalcev.*\s*.*>(?P<prebivalstvo>.*?)</td>'
    r'>Skupni prirast.*\s*.*>(?P<prirast>.*?)</td>'
    r'>Stopnja delovne aktivnosti.*\s*.*>(?P<delovna_aktivnost>.*?)</td>'
    r'>Povprečna mesečna neto plača.*\s*.*>(?P<mesecna_neto_placa>.*?)</td>',
    re.DOTALL
)

def izloci_podatke_obcin(blok):
    obcina = vzorec_obcine.search(blok).groupdict()
    #obcina['ime'] =
    #obcina[] =
    #obcina[] =    
    #obcina[] =
    return obcina


def obcine_iz_datotek(stevilo_obcin):
    for i in range(stevilo_obcin):
        ime_datoteke = f'/podatki_obcine/obcina-{i + 1}.html'
        vsebina = orodja.vsebina_datoteke(ime_datoteke)
        yield izloci_podatke_obcin(vzorec_obcine.finditer(vsebina))

obcine = []
for obcina in obcine_iz_datotek(STEVILO_OBCIN):
        obcine.append[obcina]

obcine.sort(key=lambda obcina: obcina['ime_obcine'])

polja = ['Občina',
'Regija',
'Upravna enota',
'Površina',
'Število prebivalcev', 
'Skupni prirast prebivalstva', 
'Stopnja delovno aktivnega prebivalstva', 
'Neto plača na prebivalca']

orodja.zapisi_json(obcine, polja, '/PROG_analiza_podatkov/obdelani-podatki/obcine.json')
orodja.zapisi_csv(obcine, polja, '/PROG_analiza_podatkov/obdelani-podatki/obcine.csv')