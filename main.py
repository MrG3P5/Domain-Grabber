#!/usr/bin/env python3
import requests
import re
import sys
import os
import time
from colorama import Fore, init
from datetime import datetime, timedelta
from multiprocessing.dummy import Pool as ThreadPool

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

try:
    os.mkdir("Result")
except:
    pass

all_pages_link = []
init(autoreset=True)

def Banner():
    os.system("cls" if os.name == "nt" else "clear")
    __banner__ = f"""{Fore.LIGHTRED_EX}
  ⣴⣶⣤⡤⠦⣤⣀⣤⠆      ⣈⣭⣭⣿⣶⣿⣦⣼⣆⠄
   ⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤⠄⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦⠄
           ⠈⢿⣿⣟⠦⠄⣾⣿⣿⣷⠄⠄⠄⠄⠻⠿⢿⣿⣧⣄
            ⣸⣿⣿⢧ ⢻⠻⣿⣿⣷⣄⣀⠄⠢⣀⡀⠈⠙⠿
           ⢠⣿⣿⣿⠈  ⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀
   ⢠⣧⣶⣥⡤⢄⠄⣸⣿⣿   ⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿⠄
 ⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷   ⢊⣿⣿⡏⠄⠄⢸⣿⣿⡇⠄⢀⣠⣄⣾⠄     {Fore.LIGHTCYAN_EX}[ {Fore.WHITE}Domain Grabber With Thread {Fore.LIGHTCYAN_EX}]
{Fore.LIGHTRED_EX}⣠⣿⠿⠛  ⣿⣿⣷⠘⢿⣿⣦⡀ ⢸⢿⣿⣿⣄⠄⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄        {Fore.LIGHTCYAN_EX}[ {Fore.WHITE}Created By X-MrG3P5 {Fore.LIGHTCYAN_EX}]
{Fore.LIGHTRED_EX}⠙⠃    ⣼⣿⡟⠌ ⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿⠐⣿⣿⡇⠄⠛⠻⢷⣄
      ⢻⣿⣿⣄⠄  ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⠄⠫⢿⣿⡆    
       ⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃"""
    print(__banner__ + "\n")

def Menu():
    Banner()
    CubDomain()

def CubDomain_GetDomain(urls: str):
    try:
        req = requests.get(urls, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }, timeout=15).text

        all_domains = re.findall('<a href="https://www.cubdomain.com/site/(.*?)">', req)
        
        if len(all_domains) == 1:
            sys.stdout.write(f"\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTBLUE_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Failed Grabbed")
        else:
            sys.stdout.write(f"\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTBLUE_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Grabbed {Fore.LIGHTGREEN_EX}{len(all_domains)} {Fore.WHITE}Domain")
            open("Result/cubdomain_bydate.txt", "a").write("\n".join(all_domains))
    except:
        pass

def CubDomain_GetAllPages(date: str):
    global all_pages_link
    
    try:
        req = requests.get(f"https://www.cubdomain.com/domains-registered-by-date/{date}/1", headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }, timeout=15).text
        all_pages = re.findall('<a class="page-link" href="(.*?)">', req)[:-1]
        for j in all_pages:
            all_pages_link.append(j)
    except:
        pass

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def CubDomain():
    global all_pages_link

    date1 = datetime.strptime(input(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}?{Fore.LIGHTCYAN_EX}] {Fore.WHITE}From Date (ex: YYYY-mm-dd) : "), "%Y-%m-%d")
    date2 = datetime.strptime(input(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}?{Fore.LIGHTCYAN_EX}] {Fore.WHITE}To Date (ex: YYYY-mm-dd) : "), "%Y-%m-%d")
    date_arr = [ f"{str(this_date.year)}-{str(this_date.month).zfill(2)}-{str(this_date.day).zfill(2)}" for this_date in daterange(date1, date2) ]

    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Grabbing All Pages")

    start_time = time.time()

    pool = ThreadPool(100)
    pool.map(CubDomain_GetAllPages, date_arr)
    pool.close()
    pool.join()

    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Grabbing Domain From {Fore.LIGHTGREEN_EX}{len(all_pages_link)} {Fore.WHITE}Pages")

    pools = ThreadPool(100)
    pools.map(CubDomain_GetDomain, all_pages_link)
    pools.close()
    pools.join()

    end_time = time.time()

    print(f"\n\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Done Grabbing {Fore.LIGHTGREEN_EX}{len(open('Result/cubdomain_bydate.txt', 'r').readlines())} {Fore.WHITE}Domain")
    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Time Taken {Fore.LIGHTGREEN_EX}{str(end_time - start_time).split('.')[0]} {Fore.WHITE}Sec")

if __name__ == "__main__":
    Menu()
