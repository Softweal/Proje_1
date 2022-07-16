import pandas as pd
import numpy 
from pandas import ExcelWriter

a =numpy.arange(2)
w=ExcelWriter('list.xlsx')
df_list =[]

ders = input("Ders Adı: ")
for i in a:
    ad= input("Öğrenci Adı: ")
    soyad=input("Öğrenci Soyadı: ")
    no = input("Öğrenci No: ")
    puan = int(input("Öğrenci Puanı: "))

    def harf(puan):
        if puan >= 85 and puan <=100:
            return 'A-Geçti'
        elif puan >=65 and puan <=84:
            return 'B-Geçti'
        elif puan >=50 and puan<=64:
            return 'C-Geçti'
        else:
            return 'F-Kaldı'  
    
    sonuc=harf(puan)

    df = pd.DataFrame({'Ad': [ad],
                     'Soyad': [soyad],
                     'No': [no],
                     'Puan':[puan],
                     'Sonuç':[sonuc]})
    df_list.append(df)
for i, df in enumerate(df_list):    
    df.to_excel(w,sheet_name='Sheet'+ str(i))
w.save() 