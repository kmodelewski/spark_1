import time

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from io import BytesIO

from datetime import datetime
from zoneinfo import ZoneInfo

timestamp = datetime.now(ZoneInfo("Europe/Warsaw")).strftime("%Y-%m-%d %H:%M:%S")
print(f'timestamp {timestamp}')

url = "https://kpd.gddkia.gov.pl/index.php/pl/archiwalne-dane/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Znajdź wszystkie linki do plików .xlsx
links = soup.find_all("a", href=True)
xlsx_links = [link["href"] for link in links if link["href"].endswith(".xlsx")]
print(f"Znaleziono {len(xlsx_links)} plików .xlsx do pobrania.")
# print(f"Linki do plików .xlsx: {xlsx_links}")
rows_counter = 0

col_names = ['podmiot', 'klasa', 'typ', 'poczatek_utrudnienia', 'koniec_utrudnienia', 'data_wygasniecia', 'nr_drogi',
             'nazwa_ulicy', 'pikietaz_poczatkowy',
             'dlugosc_utrudnienia', 'kierunek', 'aktywne', 'dlugosc_geograficzna', 'szerokosc_geograficzna',
             'opis_utrdunienia', 'porada_dla_kierowcow']

# Pobierz każdy plik
for link in xlsx_links:

    print(f"link: {link}")
    filename = os.path.splitext(link.split("/")[-1])[0]  # extracts file name and leave only file name without extension
    file_url = link if link.startswith("http") else f"https://kpd.gddkia.gov.pl{link}"
    print(f"file url: {file_url}")

    try:
        file_data = requests.get(file_url).content
        df = pd.read_excel(BytesIO(file_data), skiprows=3, header=0, names=col_names)
        df['s3_ingest_timestamp'] = timestamp
        df.drop(df.index[:2], inplace=True)
        df.to_csv(f'/Volumes/transportation_dept/bronze/s3/kpd/csv/{filename}.csv', index=False)

        print(f"Wczytano plik: {filename} z {df.shape[0]} wierszami.")
        rows_counter += df.shape[0]
        print(f'sum of rows is {rows_counter}')


    except Exception as e:
        print(f"Błąd przy wczytywaniu pliku {filename}: {e}")

# time.sleep(1)  # Opóźnienie między żądaniami



