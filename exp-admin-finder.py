#coding: utf-8
from urllib import request
print('''
▓█████       ▄▄▄             █████▒     
▓█   ▀      ▒████▄         ▓██   ▒      
▒███        ▒██  ▀█▄       ▒████ ░      
▒▓█  ▄      ░██▄▄▄▄██      ░▓█▒  ░      
░▒████▒ ██▓  ▓█   ▓██▒ ██▓ ░▒█░     ██▓ 
░░ ▒░ ░ ▒▓▒  ▒▒   ▓▒█░ ▒▓▒  ▒ ░     ▒▓▒ 
 ░ ░  ░ ░▒    ▒   ▒▒ ░ ░▒   ░       ░▒  
   ░    ░     ░   ▒    ░    ░ ░     ░   
   ░  ░  ░        ░  ░  ░            ░  
         ░              ░            ░  


[+] EXP - Admin Finder
[+] https://breaksec.wordpress.com/
[+] By: EXPL01T3R - http://caveiratech.com
'''
)
def login():
    wordlist = open(input('Digite o caminho da Wordlist\nEx.:C:\wordlist\wordlist.txt: '))
    site = input('Digite o site\nEx.:www.site.com: ')
    while True:
        tempwl = wordlist.readline()
        templink = ('http://'+site+'/'+tempwl)
        resp = 0
        try:
            resp = request.urlopen(templink).status
            if resp == 200:
                print('Possível Pagina: {link}{ln}' .format(link=templink, ln=50*'-'))
        except:
            continue
login()
