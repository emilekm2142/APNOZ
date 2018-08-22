import re
import codecs
import datetime
from collections import Counter
class GenerateReport():
    
    def __init__ (self,text):
        self.lines=[]
   
  
        self.uwagi=[]
        self.p=re.compile("\s?\S[0-9][0-9]?\s?")
        p=re.compile("\s?\S[0-9][0-9]?")
        self.lines_enters=text.split("\n")
        for i in range(len(self.lines_enters)):
            if self.lines_enters[i]=="" or self.lines_enters[i]=="\n" or self.lines_enters[i]=="Marta" or self.lines_enters[i]=="- brak" or self.lines_enters[i]=="-brak" or 'pow.' in self.lines_enters[i]:
                pass
            elif 'klasa:' in self.lines_enters[i]:
                self.klasa=self.lines_enters[i].split(':')
                self.klasa=self.klasa[1]
            else:
                self.lines.append(self.lines_enters[i])
        self.html_header()
        self.table_header()
        for element in range(len(self.lines)):
            self.uwagi=[]
            aktualelement=0
            if "Lp." in self.lines[element]:
                
                aktualelement=element+1
                nazwisko=self.lines[aktualelement]
                print(nazwisko)
                aktualelement+=3
                uwaga=p.sub(" ",str(self.lines[aktualelement]))
                uwaga=uwaga.strip()
                self.uwagi.append(uwaga)
                self.file.write('<tr><td>'+nazwisko+'</td><td>')
                while True:
                    #sprawdzanie czy to koniec ucznia
                    if 'Suma punktów' not in self.lines[aktualelement+5]:
                        aktualelement+=6
                        uwaga=self.p.sub("",str(self.lines[aktualelement]))
                        uwaga=uwaga.strip()
                        self.uwagi.append(uwaga)

                        
                    else:
                        color=''
                        self.byleuwagi=[]
                        c = Counter(self.uwagi)
                        for i in range(len(self.uwagi)):
                            if self.uwagi[i] not in self.byleuwagi:
                                ilosc=c[self.uwagi[i]]
                                self.byleuwagi.append(self.uwagi[i])
                                if 'niew' in self.uwagi[i]:color='red'
                                elif 'samow' in self.uwagi[i]:color='red'
                                elif 'jedze' in self.uwagi[i]:color='red'
                                elif 'brak' in self.uwagi[i]:color='red'
                                elif 'arogancja' in self.uwagi[i]:color='red'
                                elif 'arogancja' in self.uwagi[i]:color='red'
                                elif 'stonowanych' in self.uwagi[i]:color='red'
                                elif 'żucie' in self.uwagi[i]:color='red'
                                elif 'oszustwo' in self.uwagi[i]:color='red'
                                elif 'makijażu' in self.uwagi[i]:color='red'
                                elif 'niszczenie' in self.uwagi[i]:color='red'
                                elif 'Brak' in self.uwagi[i]:color='red'
                                elif 'wulgarn' in self.uwagi[i]:color='red'
                                else:color='green'
                                if ilosc>=5 and color=='green': self.file.write('<span class="green">Ustna pochwała wychowawcy za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=10 and color=='green': self.file.write('<span class="green">Pisemna pochwała wychowawcy za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=15 and color=='green': self.file.write('<span class="green">Pisemna pochwała dyrektora za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=20 and color=='green': self.file.write('<span class="green">Nagroda rzeczowa dyrektora za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=5 and color=='red': self.file.write('<span class="red">Ustne upomnienie wychowawcy za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=10 and color=='red': self.file.write('<span class="red">Rozmowa z pedagogiem za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=15 and color=='red': self.file.write('<span class="red">Pisemna nagana wychowawcy za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=20 and color=='red': self.file.write('<span class="red">Pisemna nagana dyrektora za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=25 and color=='red': self.file.write('<span class="red">Pisemna nagana dyrektora z możliwością przeniesienia do innej klasy za '+self.uwagi[i]+"</span><br>")
                                if ilosc>=30 and color=='red': self.file.write('<span class="red">Usunięcie ze szkoły ;( '+self.uwagi[i]+"</span><br>")
                                self.file.write('<span class="'+color+'">'+self.uwagi[i]+'  x'+str(ilosc)+"</span><br>")
                        print (self.uwagi) 
                        self.file.write('</td>')
                        break
    def html_header(self):
            filename='Raport '+str(datetime.date.today())+' dla '+self.klasa+".html"
            self.file = codecs.open(filename, "w", "utf-8")
            self.file.write('<!DOCTYPE html><html><head><meta charset="UTF-8">')
            self.file.write('<style>body{;font-size:17px;font-family:Verdana, Sans-Serif; margin:auto;width:700px;}')
            self.file.write('thead td{color:rgba(0,0,190,0.8);border-bottom:3px solid rgba(0,0,255,0.5);font-size:22px;} tr:hover{background-color:rgba(100,100,255,0.1);}td{padding-left:25px;padding-right:25pxpadding-top:40px;padding-bottom:40px;border-bottom:1px solid rgba(0,0,255,0.2);}.red{color:rgba(255,0,0,0.8);}.green{color:rgba(0,255,0,0.8)}</style>')

            self.file.write('</head><body> '+ filename+ ' wygenerowane APNOZEM 2.2')
    def table_header(self):
            self.file.write('<table><thead><tr><td>Uczeń</td><td>Uwagi</td></tr></thead>')
            
                            
      
