import orodja
import re

STEVILO_OBCIN = 210

vzorec = re.compile(
    r'class="text-size-h1">\s*Občina\s(?P<ime_obcine>.*?)\s*</h1>.*?',
    flags=re.DOTALL
)

najdeno = 0

for stran in range(STEVILO_OBCIN):
    url = f"https://www.stat.si/obcine/sl/Municip/Index/{stran + 1}"
    datoteka = f'PROG_analiza_podatkov/podatki_obcine/obcina-{stran + 1}.html'
    orodja.shrani_spletno_stran(url, datoteka)
    vsebina = orodja.vsebina_datoteke(datoteka)

    for zadetek in re.finditer(vzorec, vsebina):
        print(zadetek.groupdict())
        najdeno += 1
    
print(najdeno)