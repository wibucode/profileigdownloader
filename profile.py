#!/usr/bin/python
# -*- coding: ascii -*-
# Copyright WibuCode 2020
import requests, os, sys
from bs4 import BeautifulSoup as bs
def profile():
	os.system("clear")
	print """

______           __ _ _      
| ___ \         / _(_) |     
| |_/ / __ ___ | |_ _| | ___ 
|  __/ '__/ _ \|  _| | |/ _ \

| |  | | | (_) | | | | |  __/ Instagram
\_|  |_|  \___/|_| |_|_|\___| Downloader
Author	: WibuCode
Github	: https://github.com/wibucode
	"""
	url = "https://instagram.com/"
	username = raw_input("Nama User Instagram: ")
	r = requests.get(url+username)
	soup = bs(r.text, "html.parser")
	meta = soup.find("meta", property="og:image").attrs["content"]
	download = requests.get(meta)
	download = download.content
	f = open(username+".jpg", "wb")
	f.write(download)
	f.close()
	print "\033[92mBerhasil \033[97mmendowonload profile -> "+username+".jpg\033[97m"
	ask = raw_input("lagi? y/n: ").lower()
	if ask == "y":
		profile()
	elif ask == "n":
		sys.exit()
	else:
		print "Pilih y/n?"
try:
	profile()
except KeyboardInterrupt:
	print "Ctrl + C auto exit"

