import orodja
import re
import requests
import os

### Vars
STEVILO_OBCIN = 212
html_filename = 'podatki_o_obcinah.html'
csv_filename = 'obcine.csv'


### Vzorec 

pattern = (
    r'class="text-size-h1">\s*Občina\s(?P<obcina>.*?)\s*</h1>'
    r'<a href="/obcine/sl/Region/Index/\d+">\s*Regija\s(?P<regija>.*?)\s*</a>'
    r'<li class="active">\s*Upravna enota\s(?P<UE>.*?)\s*</li>'
    r'>Površina km.*\s*?>(?P<povrsina>.*?)</td>'
    r'>Število prebivalcev.*\s*.*>(?P<prebivalstvo>.*?)</td>'
    r'>Skupni prirast.*\s*.*>(?P<prirast>.*?)</td>'
    r'>Stopnja delovne aktivnosti.*\s*.*>(?P<delovna_aktivnost>.*?)</td>'
    r'>Povprečna mesečna neto plača.*\s*.*>(?P<mesecna_neto_placa>.*?)</td>'
)

### Zajem podatkov

najdene_obcine = 0

for stran in range(STEVILO_OBCIN):
    url = f"https://www.stat.si/obcine/sl/Municip/Index/{stran + 1}" 
    datoteka = f'podatki_o_obcinah.html' 
    orodja.shrani_spletno_stran(url, datoteka)
    vsebina = orodja.vsebina_datoteke(datoteka)

    for zadetek in re.finditer(pattern, vsebina):
        # print(zadetek.groupdict())
        najdene_obcine += 1

print(najdene_obcine)

### Shrani zajem 

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'a', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

    