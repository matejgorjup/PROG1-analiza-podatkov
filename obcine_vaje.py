import csv
import os
import re
import requests

STEVILO_OBCIN = 210
download_directory = 'podatki obcine'
download_filename = 'obcine.html'
csv_filename = 'macke.csv'


def download_url_to_string(url):
    try:
        page_content = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Prišlo je do napake v omrežju")
        return None
    return page_content.text


def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'a', encoding='utf-8') as out:
        out.write(text)
    return None


def read_file_to_string(directory, filename):
    with open(os.path.join(directory, filename), encoding="utf-8") as vhodna: #za hkratno odpiranje in mape in fila
        return vhodna.read()


def page_to_ads(page_content):
    pattern = r'class="text-size-h1">(.*?)<td colspan="3" class="td-data text-center">'
    regexp = re.compile(pattern, re.DOTALL)

    return re.findall(regexp, page_content)


def get_dict_from_ad_block(block):
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
    regexp = re.compile(pattern, re.DOTALL)
    najdeno = re.search(regexp, block)
    if najdeno:
        return najdeno.groupdict()
    return None


def write_csv(fieldnames, rows, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


###########################################

def main(redownload=True, reparse=True):
    
    for stran in range(STEVILO_OBCIN):
        url = f"https://www.stat.si/obcine/sl/Municip/Index/{stran + 1}" 
        spletna_stran = download_url_to_string(url)
        save_string_to_file(spletna_stran, download_directory, download_filename)
        
    vsebina = read_file_to_string(download_directory, download_filename)
    
    podatki_obcin = page_to_ads(vsebina)

    print(podatki_obcin)

    seznam_podatkov = [
        get_dict_from_ad_block(oglas) for oglas in podatki_obcin
    ]
    print(seznam_podatkov)

    fieldnames = [kljuc for kljuc in seznam_podatkov[0]]
    write_csv(fieldnames, seznam_podatkov, download_directory, csv_filename)


if __name__ == '__main__':
    main()