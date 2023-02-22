import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site está indisponível no momento.')
else:
    print('O site está disponível no momento')