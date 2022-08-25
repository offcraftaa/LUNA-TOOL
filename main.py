import requests
import pyfiglet
import phonenumbers
import os, sys

from phonenumbers import carrier, geocoder, timezone
from colorama import *

def get_info_by_ip(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print("\n==================================================")
        data = {
            '[IP]': response.get('query'),
            '[CITY]': response.get('city'),
            '[REGION]': response.get('regionName'),
            '[COUNTRY]': response.get('country'),
            '[TIMEZONE]': response.get('timezone'),

        }

        for k, v in data.items():
            print(f'{k} : {v}')
    except requests.exceptions.ConnectionError:
        print('[!] Пожалуйста, проверьте ваше интернет соединение...')

def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    init()

    while True:
        print("\n" * 100)
        print(pyfiglet.figlet_format("Luna Tool", justify='center', width=110))
        print(Style.BRIGHT + Fore.GREEN + "Выберите дейсвие: \n\n[01] Number Info \n[02] Ip info")
        func = input("\nВыбор: ")

        if func == "01":
            number = phonenumbers.parse(number=input("\nВведите номер: "))
            carrier = carrier.name_for_number(number, 'ru')
            region = geocoder.description_for_number(number, 'ru')
            timezone = timezone.time_zones_for_number(number)
            valid = phonenumbers.is_valid_number(number)

            print("\nУспешно выполнено! \n==================================================")
            print(" \nNumber: " + str(number) + "\nTimezone: " + str(timezone) + "\nOperator: " + str(
                carrier) + "\nRegion: " + str(region) + "\nValid: " + str(valid))
            print("\n==================================================")

        elif func == "02":
            ip = str(input('Enter the ip: '))
            get_info_by_ip(ip)

        input('Press Enter...')
        clear_screen()
