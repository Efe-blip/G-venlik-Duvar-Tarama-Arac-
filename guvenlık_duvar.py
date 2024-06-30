#!/usr/bin/env Python

import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GUVENLIK DUVAR TESPITI")

print("hoşgeldiniz !")

site = input("Site adresi :")

os.system("wafw00f "+site)