import sqlite3
import time
import os
import io
import sys
from datetime import datetime

def liczba(a):
    if a =='1':
        return True
    if a =='2':
        return True
    if a =='3':
        return True
    if a =='4':
        return True
    if a =='5':
        return True
    if a =='6':
        return True
    if a =='7':
        return True
    if a =='8':
        return True
    if a =='9':
        return True
    if a =='0':
        return True
    return False

try:
    f = sqlite3.connect('c:/Users/jakub/Desktop/backend/projekt/src/payroll/db.sqlite3')
    v = f.cursor()
except:
    print('brak połączenia z bazą danych')


pl12=open(r"c:/Users/jakub/Desktop/backend/projekt/src/payroll/payroll/test.txt","r",encoding="utf-8")
q4=pl12.read()
#print(len(q4))
pl12.close()

a=""
b=0
c=0
c1=0
d=0
kod=''
nazwa=''
b13=list()
#data123=datetime.now()
#print(data123)
for x in q4:
    if liczba(x) and liczba(q4[c+1]) and liczba(q4[c+2]) and liczba(q4[c+3]) and liczba(q4[c+4]) and liczba(q4[c+5]):
        nazwa=''
        kod=''
        kod=q4[c:c+6]
        while True:
            if q4[c+d+7]=='\n':
                break
            else:
                nazwa+=q4[c+d+7]
            d+=1
            #if d == 2:
             #   break
        d=0
        b12="INSERT INTO payroll_app_list_of_profession (code,name_of_proffession) VALUES (?,?)"
        b13 = (kod,nazwa)
        v.execute(b12,b13)
        
        print ('kod  ---->',kod,'|| nazwa  ---> ',nazwa,'||  ---> ',q4[c:c+15])
        b+=1
    c+=1
print(b,len(q4)) 
f.commit()
f.close()   

# def SQL_Insert(dupa,c,c1,lista):
#     try:
#         c.execute(dupa,lista)
#     except sqlite3.Error as er:
#         czas = datetime.datetime.now()
#         b1=czas.hour
#         b2=czas.minute
#         b3=czas.second
#         b="&&&&&&&&&&&&&&&&&&-"
#         b+= str(czas.year)+ ":"+str(czas.month)+":"+str(czas.day)+"|"+str(b1)+ ":"+ str(b2)+":"+str(b3)
#         b+="-&&&&&&&&&&&&&&&&&&\n"
#         b+='SQLite error: %s' % (' '.join(er.args)) + "\n" + "class : " + str(er.__class__)+"\n"
#         b+='pytanie SQL:' + dupa + "\n"
#         q4=open("c:\python_prb\kadry\error.txt",'a')
#         q4.write(b)
#         q4.close()
#         return False
#     c1.commit()
#     return True