import urllib.request
import re
import webbrowser
class Aktualizuj():
    def __init__(self,wersja):
        self.reg=re.compile('\\r')
        self.reg2=re.compile("b'")
        self.wersja=wersja
        self.dzialaj()
    def dzialaj(self):
        strona = urllib.request.urlopen("http://magiel.boo.pl/wersje.txt")
        linie= str(strona.read()).split('\n')
        for i in range(len(linie)):
            dane=linie[i].split('\\n')
            for x in dane:
                self.reg.sub(' ',x)
                danedalej=x.split('|')
                for u in range(len(danedalej)):
                    if float(self.reg2.sub('',danedalej[0]))>self.wersja:
                        webbrowser.open("http://magiel.boo.pl/apnoz-aktualizacja.html")
                        return "jest dostępna nowa wersja! Otwieram witrynę z linkiem do pobrania!"
                    
