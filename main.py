#!/usr/bin/env python3
import requests
import pyfiglet
import os
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def banner():
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format("X - Grabber", font="slant", justify="center")
    print(__banner__)
    print(f"\t\t\t[ Created By X - MrG3P5 ]\n")

def Grab(tgl):
    try:
        req = requests.get(f"https://www.cubdomain.com/domains-registered-by-date/{tgl}/1", headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        })
        soup = BeautifulSoup(req.text, "html5lib")
        a = soup.find("ul", { "class": ["pagination-sm", "pagination", "mb-2"]})
        total_page = a.find_all("a", { "class": "page-link" })[-2].text
        
        for y in range(int(total_page)):
            y += 1
            req_2 = requests.get(f"https://www.cubdomain.com/domains-registered-by-date/{tgl}/{y}", headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
            })
            soups = BeautifulSoup(req_2.text, "html5lib")
            all_domain = re.findall('https://www.cubdomain.com/site/(.*?)"', req_2.text)
            open("result.txt", "a").write("\n".join(all_domain))
            print(f"[•] (Date: {tgl} | Page: {y}) Grabbed {len(all_domain)} Domain")
    except:
        pass

def main():
    banner()
    date1 = datetime.strptime(input("[?] From Date (ex: 2023-02-09) : "), '%Y-%m-%d')
    date2 = datetime.strptime(input("[?] To Date (ex: 2023-02-09) : "), '%Y-%m-%d')
    for this_date in daterange(date1, date2):
        tgl = str(this_date.year) + "-" + str(this_date.month).zfill(2) + "-" + str(this_date.day).zfill(2)
        Grab(tgl)
    print("[-] Done")

if __name__=="__main__":
    main()
