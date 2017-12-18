#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import colorama
from colorama import Fore, Back, Style
import demjson
import urllib.request, urllib.parse
import hashlib
import json
import time
from datetime import *
import math

args = sys.argv

try:
	name = args[1]
except IndexError:
	name = 'I_am_4a'

colorama.init(autoreset=True)

def getPlayerData(playerName):
	prefix = "[" + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "PDG for Minecraft" + Style.RESET_ALL + "] "
	print(prefix + "Preparing connection...")
	params = {
		"mode": "player",
		"type": "all",
		"id": playerName,
		"key": "a4162477c69df3171c0469854443f072"
	}
	p = urllib.parse.urlencode(params)
	url = "http://mcid.ml/api.v4.php?" + p
	print(prefix + "Connection ready.")
	print(prefix + "Starting connection...")
	with urllib.request.urlopen(url) as res:
		json = res.read().decode("utf-8")
		arr = demjson.decode(json)
		if arr['success'] == True:
			print(prefix + "Data get is complete.")
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + '----- ' + playerName + u'\'s Player data -----' + Style.RESET_ALL)
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "Player's name: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + arr['response']['name'] + Style.RESET_ALL)
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "Player's UUID: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + arr['response']['uuid'] + Style.RESET_ALL)
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "Player's name history: " + Style.RESET_ALL)
			cnt = 0
			for i in arr['response']['nameHistory']:
				cnt = cnt + 1
				if cnt == 1:
					print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "- " + str(cnt) + "(Original): " + Style.BRIGHT + Fore.LIGHTGREEN_EX + i['name'] + Style.RESET_ALL)
				elif len(arr['response']['nameHistory']) == cnt:
					print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "- " + str(cnt) + "(Latest): " + Style.BRIGHT + Fore.LIGHTGREEN_EX + i['name'] + Style.RESET_ALL)
				else:
					print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "- " + str(cnt) + ": " + Style.BRIGHT + Fore.LIGHTGREEN_EX + i['name'] + Style.RESET_ALL)
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "Tateshiki Server! status: " + Style.RESET_ALL)
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "- Verified: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['verified']) + Style.RESET_ALL)
			if arr['response']['ts-stat']['status'] != None:
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "- Status: " + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Block(Break / Place): " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['break']) + " / " + str(arr['response']['ts-stat']['status']['place']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Click(Right / Left): " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['click_r']) + " / " + str(arr['response']['ts-stat']['status']['click_l']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Server(Connect / Disconnect): " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['connect']) + " / " + str(arr['response']['ts-stat']['status']['disconnect']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Chat: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['chat']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Command: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['command']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Craft: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['craft']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Death: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['death']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Shoot Projectile: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['shoot']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Sneak: " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['sneak']) + Style.RESET_ALL)
				print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "-- Playtime(Second): " + Style.BRIGHT + Fore.LIGHTGREEN_EX + str(arr['response']['ts-stat']['status']['sneak']) + Style.RESET_ALL)
			print(prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "\n" + prefix + Style.BRIGHT + Fore.LIGHTCYAN_EX + "by " + Style.BRIGHT + Fore.LIGHTGREEN_EX + arr['apiStat']['title'] + Style.RESET_ALL)

getPlayerData(name)
print raw_input("Please input something key to exit.")