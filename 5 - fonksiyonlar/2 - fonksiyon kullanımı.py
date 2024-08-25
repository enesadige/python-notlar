import os; os.system("clear")
#pythonda fonksiyonlar

#fonksiyon oluşturmak için anahtar sözcük >> def
#daha sonra fonksiyona bir isim veriyoruz ve parantez koyarız 
#aslında c++ dilindeki fonksiyon kullanımına benzerdir
#parametre istersek ama parametre gelmezse diye burda da varsayılan değer atayabiliriz

#burda da geriye değer dönderecek fonksiyonlar oluştururuz fakat burada başına void ya da int gibi şeyler tanımlamamıza gerek yoktur
#bir fonksiyon içinde başka fonksiyonu kullanabiliyoruz

#help komutu fonksiyonun içine girilen bilgiyi ileride kodları inceleyecek kişi rahat anlasın diye ekrana yazdırır
#fonkç. içine '''ifadeler...''' kısmı koyarız
#daha sonra print(help(fonk._adı)) ile yazdırırız
#burada önemli kısım şudur kodların çıktısını vermeden önce help bilgisini verir sonra "q" ile kapatırız kodların çıktısını verir

#------------------------------------------------------------------------------------------------------------------------------------

#fonksiyon oluşturma ve parametre ve varsayılan değer oluşturma
def sayHello(girdi = "isimsiz"):
    print("hello " + girdi)


#fonksiyonu çağırma
sayHello("enes")

#varsayılan değer kontrolü
sayHello()

#değer döndüren fonksiyon

def func_two(girdi = "None"):
    return "döndürülen değer : " + girdi

print(func_two())


#bir fonksiyon içinde başka fonksiyonu kullanabiliyoruz
def yasHesapla(num):
    return 2024-num

#burada içine yollarız
def emekliligeKacYilKaldi(num, name):
    yas = yasHesapla(num)
    emeklilik = 65-yas
    
    if emeklilik >= 0 :
        print(f"sayın {name} emekliliğinize {emeklilik} yıl kaldı")

    else :
        print(f"sayın {name} emekliliğiniz gelmiştir")

emekliligeKacYilKaldi(70, "enes")
emekliligeKacYilKaldi(60, "erkam")


#help kullanımı
def helpKullanimi():
    '''
    DOCSTRİNG: burada fonksiyonun amacı yazar
    INPUT: girdi bilgisi yazar
    OUTPUT: çıktı bilgisi yazar
    '''
    

print(help(helpKullanimi))

#help kullanımı devamı 
list = [1,2,3]
print(help(list.append))