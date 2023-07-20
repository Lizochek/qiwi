from datetime import datetime as dt
import requests
import xml.etree.ElementTree as ET


def iso_formate(code):
    c = code.split(" ")
    code_new = c[1]
    iso_code = "./Valute[NumCode='" + str(code_new) + "']/Value"
    return (iso_code)


def formate_d(date):
    # функция для преобразования даты в нужный формат д/м/год
    d = dt.strptime(date, "%Y-%m-%d")
    day = int(d.day)
    if (day < 10) and (day != 0):
        day = str(day)
        day = "0" + day
    month = str(d.month)
    year = str(d.year)
    new_date = str(day + "/" + month + "/" + year)
    return (new_date)


def list_of_exchange(date, code):
    # функция для вывода списка валют
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date
    try:
        r = requests.get(url, timeout=1)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP error")
        print(errh.args[0])

    exchange_list = float(
        ET.fromstring(requests.get(url).text)
        .find(code)
        .text.replace(",", "."))
    print("USD (Доллар США):", exchange_list)


if __name__ == '__main__':
    date = "2022-10-08"
    code = "ISO 840"
    new_d = formate_d(date)
    new_code = iso_formate(code)
    list_of_exchange(new_d, new_code)
