#!/usr/bin/env python3
import requests
import re
import sys
import os
import string
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
    menus = f"""
{Fore.LIGHTRED_EX}[{Fore.WHITE}1{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber By Date
{Fore.LIGHTRED_EX}[{Fore.WHITE}2{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber By KeyWord
{Fore.LIGHTRED_EX}[{Fore.WHITE}3{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber By TLD (azstats.org)
{Fore.LIGHTRED_EX}[{Fore.WHITE}4{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber By TLD (pagesinventory.com)
{Fore.LIGHTRED_EX}[{Fore.WHITE}5{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber By TLD (topsitessearch.com)
{Fore.LIGHTRED_EX}[{Fore.WHITE}6{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber Domain Random (www.topmillion.net)
{Fore.LIGHTRED_EX}[{Fore.WHITE}7{Fore.LIGHTRED_EX}] {Fore.WHITE}Grabber By Date (www.dubdomain.com)\n"""
    print(menus)
    choose = int(input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}Choose : "))

    if choose == 1:
        CubDomain()
    elif choose == 2:
        input_list = [ j.strip("\n\r") for j in open(input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}KeyWord List : "), "r", encoding="utf-8").readlines() ]

        for x in input_list:
            GrabberByKw(x)
    elif choose == 3:
        inp_tld = input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}TLD Domain (ex: com) : ")
        list_url = GenerateTldLink(inp_tld)
        
        start_time = time.time()
        
        pool = ThreadPool(20)
        pool.map(GrabTld, list_url)
        pool.close()
        pool.join()
        
        end_time = time.time()

        print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Time Taken {Fore.LIGHTGREEN_EX}{str(end_time - start_time).split('.')[0]} {Fore.WHITE}Sec")
    elif choose == 4:
        inp_tld = input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}TLD Domain (ex: com) : ")
        list_url = GenerateTLD2(inp_tld)
        
        start_time = time.time()
        
        pool = ThreadPool(20)
        pool.map(GrabTld2, list_url)
        pool.close()
        pool.join()
        
        end_time = time.time()

        print(f"\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Time Taken {Fore.LIGHTGREEN_EX}{str(end_time - start_time).split('.')[0]} {Fore.WHITE}Sec")
    elif choose == 5:
        inp_tld = input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}TLD Domain (ex: com) : ")
        inp_page = int(input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}Total Page (ex: 100) : "))
        list_url = GeneratePageTopSite(inp_tld, inp_page)
        
        start_time = time.time()
        
        pool = ThreadPool(20)
        pool.map(GrabTopSite, list_url)
        pool.close()
        pool.join()
        
        end_time = time.time()

        print(f"\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Time Taken {Fore.LIGHTGREEN_EX}{str(end_time - start_time).split('.')[0]} {Fore.WHITE}Sec")
    elif choose == 6:
        list_url = getTopMilionPageUrl()
        
        start_time = time.time()
        
        pool = ThreadPool(20)
        pool.map(grabTopMilionPageUrl, list_url)
        pool.close()
        pool.join()
        
        end_time = time.time()

        print(f"\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Time Taken {Fore.LIGHTGREEN_EX}{str(end_time - start_time).split('.')[0]} {Fore.WHITE}Sec")
    else:
        exit(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}!{Fore.LIGHTRED_EX}] {Fore.LIGHTYELLOW_EX}Aborted.")

def getTopMilionPageUrl():
    try:
        req = requests.get("https://www.topmillion.net/pages/websites/", headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

        LastPage = re.findall(r'/pages/websites/page/(.*?)/', req.text)[-1]
        arr = []
        for page in range(1, int(LastPage) + 1):
            arr.append(f"https://www.topmillion.net/pages/websites/page/{str(page)}/")
            
        return arr
    except:
        return []

def grabTopMilionPageUrl(url):
    try:
        page = url.split("/")[-2]
        req = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

        domains = [j.replace("?", "").replace("https://", "").replace("http://", "") for j in re.findall(r'http://s.wordpress.com/mshots/v1/(.*?)?w=400', req.text)]
        
        if len(domains) != 0:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}{len(domains)} {Fore.WHITE}Domain Grabbed From Page {page}!")
            
            for domain in domains:
                open("Result/Random-Domain.txt", "a").write(domain + "\n")
        else:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Domain Grabbed From Page {page}!")
    except:
        sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Domain Grabbed From Page {page}!")

def GrabTopSite(url):
    try:
        page = url.split("/")[-1]
        req = requests.get(url, timeout=10)
        domains = re.findall(r'domain=(.*?)"', req.text)
        
        if len(domains) == 0:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Domain Grabbed From Page {page}!")
        else:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}{len(domains)} {Fore.WHITE}Domain Grabbed From Page {page}!")
            
            for domain in domains:
                open("Result/grab_tld.txt", "a").write(domain + "\n")
    except:
        sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Domain Grabbed From Page {page}!")

def GeneratePageTopSite(tld, totalPage):
    try:
        arr = []
        
        for i in range(1, totalPage + 1):
            arr.append(f"https://www.topsitessearch.com/domains/.{tld}/{i}")
        
        return arr
    except:
        return []

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

def GenerateTLD2(tld):
    try:
        arr = []
        
        for x in string.ascii_lowercase:
            arr.append(f"https://www.pagesinventory.com/tld/{tld}/{x}.html")
        
        return arr
    except:
        return []

def GrabTld2(url):
    try:
        req = requests.get(url, timeout=5)
        domains = re.findall(r'href="/domain/(.*?).html"', req.text)
        
        if len(domains) != 0:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}{len(domains)} {Fore.WHITE}Grabbed!")
            for domain in domains:
                open("Result/grab_tld.txt", "a").write(domain + "\n")
        else:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Grabbed!")
    except:
        sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Grabbed!")

def GrabTld(url):
    try:
        req = requests.get(url, timeout=5)
        domains = re.findall(r'href="/site/(.*?)/"', req.text)
        
        if len(domains) != 0:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}{len(domains)} {Fore.WHITE}Grabbed!")
            for domain in domains:
                open("Result/grab_tld.txt", "a").write(domain + "\n")
        else:
            sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Grabbed!")
    except:
        sys.stdout.write(f"\n{Fore.WHITE}---> {Fore.LIGHTBLUE_EX}0 {Fore.WHITE}Grabbed!")

def GenerateTldLink(tld):
    try:
        arr = []
        
        for x in range(1, 101):
            arr.append(f"https://azstats.org/top/domain-zone/{tld}/{x}")

        return arr
    except:
        return []

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def CubDomain():
    global all_pages_link

    date1 = datetime.strptime(input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}From Date (ex: YYYY-mm-dd) : "), "%Y-%m-%d")
    date2 = datetime.strptime(input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}?{Fore.LIGHTRED_EX}] {Fore.WHITE}To Date (ex: YYYY-mm-dd) : "), "%Y-%m-%d")
    date_arr = [ f"{str(this_date.year)}-{str(this_date.month).zfill(2)}-{str(this_date.day).zfill(2)}" for this_date in daterange(date1, date2) ]

    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Grabbing All Pages")

    start_time = time.time()

    pool = ThreadPool(20)
    pool.map(CubDomain_GetAllPages, date_arr)
    pool.close()
    pool.join()

    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Grabbing Domain From {Fore.LIGHTGREEN_EX}{len(all_pages_link)} {Fore.WHITE}Pages")

    pools = ThreadPool(20)
    pools.map(CubDomain_GetDomain, all_pages_link)
    pools.close()
    pools.join()

    end_time = time.time()

    print(f"\n\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Done Grabbing {Fore.LIGHTGREEN_EX}{len(open('Result/cubdomain_bydate.txt', 'r').readlines())} {Fore.WHITE}Domain")
    print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}-{Fore.LIGHTCYAN_EX}] {Fore.WHITE}Time Taken {Fore.LIGHTGREEN_EX}{str(end_time - start_time).split('.')[0]} {Fore.WHITE}Sec")

def GrabberByKw(kw):
    req = requests.get("https://iqwhois.com/search/" + kw, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }).text
    all_domain = re.findall('class="conn-domain-name-class">(.*?)</span>', req)
    
    if len(all_domain) != 0:
        sys.stdout.write(f"\n{Fore.WHITE}---> Keyword : {Fore.LIGHTBLUE_EX}{kw} {Fore.WHITE}-- Got {Fore.LIGHTGREEN_EX}{len(all_domain)} {Fore.WHITE}Domain")
        open("Result/domain_keyword.txt", "a").write("\n".join(all_domain) + "\n")
    else:
        print(req)
        sys.stdout.write(f"\n{Fore.WHITE}---> Keyword : {Fore.LIGHTBLUE_EX}{kw} {Fore.WHITE}-- {Fore.LIGHTRED_EX}Bad Keyword")

if __name__ == "__main__":
    Menu()
