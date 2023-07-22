import requests
from bs4 import BeautifulSoup
import datetime
import csv


url = 'https://www.banki.ru/products/currency/cb/'
currency_name = {'Российский рубль': 1}
currency_short_name = {'RUB': 1}
cnt = {'Российский рубль': 1}
diff = {'Российский рубль': 0}

def parse():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    currency_rows = soup.find_all('tr', {'data-test': 'currency-table-row'})
    names = [row['data-currency-name'] for row in currency_rows]
    rates = [row.find_all('td')[3].text for row in currency_rows]
    currencies = [row['data-currency-code'] for row in currency_rows]
    tmp = [row.find_all('td')[1].text for row in currency_rows]
    differ = [row.find_all('td')[4].text for row in currency_rows]

    for i in range(len(rates)):
        currency_name[names[i]] = float(rates[i])
        currency_short_name[currencies[i]] = float(rates[i])
        cnt[names[i]] = int(tmp[i])
        differ[i] = differ[i].replace("\t", "").replace("\n", "").replace(",", ".")
        diff[names[i]] = float(differ[i])

def convert(first_currency, second_currency, count):
    first_val = None
    second_val = None

    for key, value in currency_name.items():
        if key == first_currency:
            first_val = value
        if key == second_currency:
            second_val = value

    if first_val and second_val:
        return round(((count * first_val) * cnt[second_currency]) / cnt[first_currency] / second_val, 2)
    else:
        return 0

def get_current_date():
    current_datetime = datetime.datetime.now()

    formatted_date = current_datetime.strftime("%d-%m-%Y")
    formatted_time = current_datetime.strftime("%H:%M")

    return formatted_date, formatted_time

def export_csv():
    with open('file.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Название валюты', 'Текущий курс в рублях', 'Изменение'])

        for key, value in currency_name.items():
            writer.writerow([key, value, diff[key]])