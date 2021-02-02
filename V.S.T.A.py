import time, random, datetime, os, sys, webbrowser, urllib.request, requests, subprocess, colorama
from subprocess import call
from pyfiglet import Figlet
from colorama import Fore, Back, Style
font = Figlet(font="epic")
print(font.renderText('V.S.T.A'))
print('V.S.T.A - vovamod Small Text Assistant. Ver: 0.8.λ')
print("[INFO]", time.asctime(time.localtime(time.time()) ))
while True:
        def typingPrint(text):
        	for character in text:
        	    	sys.stdout.write(character)
        	    	sys.stdout.flush()
        	    	time.sleep(0.05)
        def fontPrint(text):
        	for character in text:
        	    	sys.stdout.write(character)
        	    	sys.stdout.flush()
        	    	time.sleep(0.0075)
        user=input(">> ")
        if user == ('help') or user == ('Help'):
                print('[INFO] Help commands: \n	Password - Creats password with max 128 characters in it \n	Codes - Showing all error codes types \n	Browser - Smaller and lightly usement of line inerface (uses your standard browser to work) \n	Wiki - All best wikis links and official Python discord server')
        elif user == ('password') or user == ('Password'):
                num = int(input('[INFO]Enter number of symbols to 128:'))
                pas = ''
                if num <= 128: 
                        for x in range(num):
                                pas = pas + random.choice(list('1234567890QWERTYASDFGHUIOPJKLZXCVBNMqwertyasdfghuiopjklzxcvbnm'))
                        print('[INFO]Your password is: ', pas)
                else:
                        print('[ERROR] CODE: 23')
        elif user == 'browser' or user == 'Browser':
        	    Int = 'https://'
        	    Inp=input('[INFO] URL:')
        	    webbrowser.open(Int + Inp,new = 0, autoraise = True)
        elif user == 'Codes'or user =='codes':
        	print('[INFO] Error code list: \n	404 - Command or file is not found \n	23 - Limit due max amount of character list')
        elif user == 'wiki' or user == 'Wiki':
        	print('[INFO] All best wikis and discord servers: \n	Python Wiki - https://wiki.python.org/moin/ \n	PyPI - https://pypi.org/project/wiki/ \n	GitLab - https://python-gitlab.readthedocs.io/en/stable/index.html \n	Python Official Discord - https://discord.com/invite/python')
        elif user == 'info' or user == 'Info':
        	typingPrint(Fore.GREEN + '    -----vovamod present-----\n')
        	fontPrint(Fore.GREEN + font.renderText('V.S.T.A.'))
        	typingPrint(Fore.GREEN + '-----V.S.T.A is a small program written on Python to show some features of what python is capable to do for new users and the people that want to write on it-----\n-----As a creator of this small assistant, I would appreciate any kind of help and recommendations for this small project-----\n-----In 2019 to 2020 i got an idea of making a full working assistant, but if I would try to do it, it could take all my time after that I decided to do a small version because of exams-----\n-----Thank you for using it!-----')
        	print(Style.RESET_ALL)
        elif user == 'stop': break
        else:
        	print(Fore.RED + '[ERROR]', Style.RESET_ALL+ 'CODE: 404')