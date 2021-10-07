import psycopg2
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

def SQL_Insert(polecenie,c,conn,lista,m=0):
    try:
        c.execute(polecenie,lista)
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
        conn.close()
        sys.exit()
    if m==0:
        conn.commit()
    return True


try:
    conn = psycopg2.connect(host='10.0.0.102', database='kadry_gui',user= 'janusz',password='zaq1@WSX2048')    
    custor = conn.cursor()
    print('jest OK !!!!!!!!!!!!!!!!!!!!!!!!')
except psycopg2.DatabaseError as e:
    print(e)
    print(e.__class__)
    sys.exit()


pl12=open(r"c:/python_prb/proby/test.txt","r",encoding="utf-8")
q4=pl12.read()
print(len(q4))
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
        b12="INSERT INTO stanowiska (kod,nazwa) VALUES (%s,%s)"
        b13 = (kod,nazwa)
        SQL_Insert(b12,custor,conn,b13)
        print ('kod  ---->',kod,'|| nazwa  ---> ',nazwa,'||  ---> ',q4[c:c+15])
        b+=1
    c+=1
print(b) 
conn.close()   

