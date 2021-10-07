import sqlite3
import time
import os
import io
import sys
from datetime import datetime

try:
    f = sqlite3.connect('c:/Users/mkuma/Desktop/django/payroll/payroll-1.0/db.sqlite3')
    v = f.cursor()
except:
    print('brak połączenia z bazą danych')


pl12=open(r"c:/Users/mkuma/Desktop/django/payroll/payroll-1.0/panstwa.txt","r",encoding="utf-8")
q4=pl12.read()
print("Ilość znaków w pliku",len(q4))
pl12.close()

d=True
nazwa_pl =''
nazwa_en =''
for x in q4:
    if x == '-':
        d=False        
    else:
        if d:
            nazwa_en+=x
    if x=='\n':
        d=True
        print("EN --->",nazwa_en,"PL--->",nazwa_pl) 
        b12="INSERT INTO payroll_app_countries (en,pl) VALUES (?,?)"
        b13 = (nazwa_en,nazwa_pl)
        v.execute(b12,b13)
        nazwa_pl =''
        nazwa_en ='' 
    else:
        if d==False:
            if x!='-':
                nazwa_pl+=x 

print(len(q4)) 
f.commit()
f.close()   

