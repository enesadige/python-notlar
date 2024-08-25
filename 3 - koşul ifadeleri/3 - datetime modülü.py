#python dilinde datetime modülü

#aslında bu şu anın konusu değil ama if-else bloğu ile bir kullanım örneği göstermek için bu kısım oluştu
#daha sonra bu modülü detaylı araştır
#örnek aşağıda

#---------------------------------------------------------------------------------------------------------------------

import datetime

#tarih bilgisi alma
tarih = input("aracınızın trafiğe çıkış tarihi (gün/ay/yıl) şeklinde giriniz :")
#bilgiyi bölüp listeleme
tarih_iki= tarih.split("/")
#bilgiyi bir datetime nesnesine dönüştürme
trafige_cikis = datetime.datetime(int(tarih_iki[2]),int(tarih_iki[1]),int(tarih_iki[0]))
#şimdiki tarihi alma
simdi = datetime.datetime.now()

#farkın gün olarak alımı için .days
fark = (simdi - trafige_cikis).days

#koşul ifadeleri
if fark <= 365 :
    print("1.yıl bakımı\n")
elif fark >= 365 and fark <= 365*2:
    print("2.yıl bakımı\n")
elif fark >= 365*2 and fark <= 365*3:
    print("3.yıl bakımı\n")
elif fark >= 365*3 :
    print("acil servis\n")
else : 
    print("hata.. hata kodu : 502")
