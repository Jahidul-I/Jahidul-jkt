W = '\033[97;1m'

R = '\033[91;1m'

G = '\033[92;1m'

Y = '\033[93;1m'

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'

import os

try:

	import requests

except ImportError:

	os.system("pip install requests")

try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")

import os

import sys

import time

import requests

import random

import platform

import base64

import subprocess

from concurrent.futures import ThreadPoolExecutor

import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess

try:

	import rich

except ImportError:

	os.system('pip install rich')

	time.sleep(1)

	try:

		import rich

	except ImportError:

		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from urllib.parse import quote

# UA LIST

#ugen2=open('frec.txt','r').read().splitlines()

#ugen=open('m.txt','r').read().splitlines()

ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']

ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; An
