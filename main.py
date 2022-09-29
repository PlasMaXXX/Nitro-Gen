import requests
import random
import string
from colorama import Fore
import time
from pystyle import Colors, Colorate

print(Colorate.Horizontal(Colors.white_to_blue,"""Gen Nitro.\n"""))
time.sleep(0.7)
num = int(input(f'{Fore.LIGHTBLUE_EX}Nitro Generate Number : \n'))
time.sleep(1)


with open("Nitro Link.txt", "w", encoding='utf-8') as file:
    print(Colorate.Horizontal(Colors.white_to_red,"""Generate Nitro !"""))
    time.sleep(0.7)

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.com/billing/promotions/{code}\n")

    print(f"{Fore.RED}Generated {num} link !\n")

with open("Nitro Link.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n")
        else:
            print(f"{Fore.LIGHTCYAN_EX}[+] , ", end = "")

print(Colorate.Horizontal(Colors.rainbow, ('''Succesfuly Generated''')))
