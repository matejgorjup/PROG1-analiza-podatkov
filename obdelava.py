import re
import csv

STEVILO_OBCIN = 210

vzorec_obcine = re.compile(
    r'<a href="\/obcine\/en\/Municip\/Index\/(?P<id>\d+?)">EN<\/a>.*?'
    r'class="text-size-h1">\s*Občina\s(?P<ime_obcine>.*?)\s*<\/h1>.*?'
    r'<a href="\/obcine\/sl\/Region\/Index\/\d+">\s*Regija\s(?P<regija>.*?)\s*<\/a>.*?'
    r'<li class="active">\s*Upravna enota\s(?P<UE>.*?)\s*<\/li>.*?'
    r'>Površina km.*?data-num">(?P<povrsina>.*?)<\/td>.*?'
    r'>Število prebivalcev.*?data-num">(?P<prebivalci>.*?)<\/td>.*?'
    r'>Skupni prirast.*?data-num">(?P<prirast>.*?)<\/td>.*?'
    r'>Stopnja delovne aktivnosti.*?data-num">(?P<delovna_aktivnost>.*?)<\/td>.*?'
    r'>Povprečna mesečna neto plača.*?data-num">(?P<placa>.*?)<\/td>',
    flags=re.DOTALL
)

def izlusci_podatke(besedilo):
    obcina = vzorec_obcine.search(besedilo).groupdict()
    obcina['id'] = int(obcina['id'])
    obcina['povrsina'] = int(obcina['povrsina'].replace('.', ''))
    obcina['prebivalci'] = int(float(obcina['prebivalci'].replace('.', '').replace(',', '.')))
    obcina['prirast'] = float(obcina['prirast'].replace(',', '.'))
    obcina['delovna_aktivnost'] = float(obcina['delovna_aktivnost'].replace(',', '.'))
    obcina['placa'] = float(obcina['placa'].replace('.', '').replace(',', '.'))

    return obcina

obcine = []
for i in range(STEVILO_OBCIN):
    ime_datoteke = f'/podatki_obcine/obcina-{i + 1}.html'
    with open(ime_datoteke, encoding='utf-8') as datoteka:
        obcine.append(izlusci_podatke(datoteka.read()))

print(obcine)

polja = ['id',
'ime_obcine', 
'regija',
'UE',
'povrsina',
'prebivalci',
'prirast',
'delovna_aktivnost',
'placa']

with open('PROG_analiza_podatkov/obcine.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=polja)
    writer.writeheader()
    for obcina in obcine:
        writer.writerow(obcina)