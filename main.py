#!/usr/bin/env python3
import requests
import re
import pyfiglet
import os
from colorama import Fore, init
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)

class DomainGrabber:

    def banner():
        os.system("cls||clear")
        __banner__ = pyfiglet.figlet_format("X - Grabber", font="slant", justify="center")
        print(red + __banner__)
        print(f"\t\t\t{red}[ {white}Created By X - MrG3P5 {red}]\n")
        print(f"{red}[{white}1{red}] {white}Domain Grabber By TLD")
        print(f"{red}[{white}2{red}] {white}Domain Grabber By Date")
        print("")

    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)

    def checkTLD(domain):
        req = requests.get("https://zoxh.com/tld").text
        all_tld = re.findall('/tld/(.*?)"', req)
        if domain in all_tld:
            return True
        else:
            return False
    
    def TLD(domain_tld):
        req = requests.get(f"https://zoxh.com/tld/{domain_tld}").text
        total_domain = int(re.findall(f'href="/tld/{domain_tld}/(.*?)"', req)[-2])

        for i in range(total_domain):
            i += 1
            try:
            
                req_grab = requests.get(f"https://zoxh.com/tld/{domain_tld}/{i}").text
                all_domain = "\n".join(re.findall('/i/(.*?)"', req)).strip("\r\n")
                total_domain = len(all_domain.split("\n"))
                open(f"result/tld_{domain_tld}.txt", "a").write(all_domain + "\n")
                print(f"{red}[{white}*{red}] {white}Grabbed {green}{total_domain} {white}Domain | Page {green}{i}")
            except:
                pass

    def ByDate(date1, date2):
        for this_date in DomainGrabber.daterange(date1, date2):
            tgl = str(this_date.year) + "-" + str(this_date.month).zfill(2) + "-" + str(this_date.day).zfill(2)
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
                    open("result/bydate.txt", "a").write("\n".join(all_domain))
                    print(f"{red}[{white}*{red}] {white}(Date: {green}{tgl} {white}| Page: {green}{y}{white}) Grabbed {green}{len(all_domain)} {white}Domain")
            except:
                pass


if __name__=="__main__":
    DomainGrabber.banner()
    choose = input(f"{red}[{white}?{red}] {white}Choose : ")
    if choose == "1":
        input_tld = input(f"{red}[{white}?{red}] {white}TLD (ex: id) : ")

        if DomainGrabber.checkTLD(input_tld):
            DomainGrabber.TLD(input_tld)
        else:
            exit(f"{red}[{yellow}!{red}] {white}Unknown Domain TLD")
    elif choose == "2":
        date1 = datetime.strptime(input(f"{red}[{white}?{red}] {white}From Date (ex: YYYY-mm-dd) : "), '%Y-%m-%d')
        date2 = datetime.strptime(input(f"{red}[{white}?{red}] {white}To Date (ex: YYYY-mm-dd) : "), '%Y-%m-%d')
        DomainGrabber.ByDate(date1, date2)
    else:
        exit(f"{red}[{yellow}!{red}] {white}Unknown Option")
