import os
import sys
import re
import requests


def pripravi_imenik(ime_datoteke):
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)


def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    try:
        print(f'Shranjujem {url} ...', end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')


STEVILO_OBCIN = 210


vzorec = re.compile(
    r'<a href="/obcine/en/Municip/Index/(?P<id>\d+?)">EN</a>.*?'
    r'class="text-size-h1">\s*Občina\s(?P<ime_obcine>.*?)\s*</h1>',
    flags=re.DOTALL
)


najdeno = 0

for stran in range(STEVILO_OBCIN):
    url = f"https://www.stat.si/obcine/sl/Municip/Index/{stran + 1}"
    datoteka = f'PROG_analiza_podatkov/podatki_obcine/obcina-{stran + 1}.html'
    shrani_spletno_stran(url, datoteka)
    with open(datoteka, encoding='utf-8') as file:
        vsebina = file.read()

    for zadetek in re.finditer(vzorec, vsebina):
        print(zadetek.groupdict())
        najdeno += 1

print(najdeno)