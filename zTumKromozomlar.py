#sadece 1 tane kromozom bulunması için

import keyword
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from numpy.random import randn
import os
import time

# Google Haritalar API
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
rnd = np.random
rnd.seed(0)
myjsonfile = open("konum.json", "r", encoding='utf-8')
jsondata = myjsonfile.read()
obj = json.loads(jsondata)

kromozomListesi = []
mesafe = []
sifirsizMesafe = []
tabuList = []
siraNumarasi=[]
alfadegeri=0;
kromozomSayisi=0;
i = 0
a = 0
enKisaMesafe =0;
#####################################################################################
#fonksiyonlar
def Hesapla():
    print(obj[i]["ad"] +" "+"için en kısa işletme bulunmaya çalışılıyor")
    if 0.0 in sifirsizMesafe:
        sifirsizMesafe.remove(0.0)
        enKisaMesafe = min(sifirsizMesafe)
        enKisaIsletmeIndex = mesafe.index(enKisaMesafe)
        if obj[enKisaIsletmeIndex]["ad"] in tabuList:
            print(obj[enKisaIsletmeIndex]["ad"] +" "+"tabu listesinde olduğu için listeden atıldı")
            sifirsizMesafe.remove(enKisaMesafe)
            print("Buradasın1")
            Hesapla()
        else:
            print(obj[enKisaIsletmeIndex]["ad"] +" "+"tabu listesinde olmadığı için en kısa işletme olarak belirlendi")
            print("Buradasın2")
            siraNumarasi.clear()
            siraNumarasi.append(enKisaIsletmeIndex)
            return enKisaIsletmeIndex

    else:
        enKisaMesafe = min(sifirsizMesafe)
        enKisaIsletmeIndex = mesafe.index(enKisaMesafe)
        if obj[enKisaIsletmeIndex]["ad"] in tabuList:
            print(obj[enKisaIsletmeIndex]["ad"] +" "+"tabu listesinde olduğu için listeden atıldı")
            sifirsizMesafe.remove(enKisaMesafe)
            print("Buradasın3")
            Hesapla()
        else:
            print(obj[enKisaIsletmeIndex]["ad"] +" "+"tabu listesinde olmadığı için en kısa işletme olarak belirlendi")
            print("Buradasın4")
            siraNumarasi.clear()
            siraNumarasi.append(enKisaIsletmeIndex)
            return

######################################################################
while i < len(obj):
    for a in range(len(obj)):
        ilkKonum = (obj[i]["x"], obj[i]["y"])
        ikinciKonum = (obj[a]["x"], obj[a]["y"])
        x = geodesic(ilkKonum, ikinciKonum).km
        mesafe.append(x)
        sifirsizMesafe.append(x)
    Hesapla()
    yeniKarakter = siraNumarasi[0]
    print(obj[i]["ad"]+" "+ " için " +" "+ obj[yeniKarakter]["ad"] +" "+ "en Kısa İşletme olarak belirlendi")
    tabuList.append(obj[i]["ad"])
    print(obj[i]["ad"]+" "+ "tabu listesine eklendi" + " " + "tabu Listesi uzunluğu" + " " + str(len(tabuList)))
    a=0;
    i = yeniKarakter
    mesafe.clear()
    sifirsizMesafe.clear()
    print("Yeni Sorguya Geçildi")
    if len(tabuList) == len(obj)-1:
        tabuList.append(obj[yeniKarakter]["ad"])
        print("Uygun kromozom bulundu")
        print(tabuList)
        kromozomSayisi = kromozomSayisi +1;
        print("kromozom sayısı"+" "+ str(kromozomSayisi))
        a=0;
        alfadegeri = alfadegeri+1;
        i = alfadegeri;
        mesafe.clear()
        sifirsizMesafe.clear()
        yeniDosyaAdi= str(alfadegeri) + ".json"
        with open("./kromozomlar/"+ yeniDosyaAdi, 'w') as json_dosya:
            json.dump(tabuList, json_dosya ,ensure_ascii=False, indent=4)
            tabuList.clear()
    else:
        continue
print("Tamamlandı")