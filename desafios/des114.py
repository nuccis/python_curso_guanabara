#des114: Crie um código em python que teste se o site Pudim está cessível pelo computador usado
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[0;31mO site está fora do ar.\033[m')
else:
    print('\033[0;32mO site está acessível.\033[m')
    #print(site.read())