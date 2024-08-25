import os; os.system("clear")
#pythonda fonksiyon parametreleri

#buradaki parametre kullanımı c++ dilindekine benzerdir
#aşağıdaki ilk örnekte n ile name değişkenleri ayrı bellek adreslerinde tutulur

#listelerde ise parametre olarak valuetype yerine referans bir tür gönderiyoruz
#yani ilk örnekte bellekte hem n hem name ayrı ayrı saklanırken burada öyle bi şey yok
#yani şunu deriz orjinal listenin adresini göndericem onun değerlerini güncelle

#bu şekilde listelerde atama yapmak yerine valuedeki gibi listenin bir kopyasını yapmak istersek
#slicing yani parçalama işlemi yapmamız gerekiyo

#şimdi diğer bir önemli kısım şu biz bi fonksiyonu örneğin iki parametreli tanımlarsak varsayılan değer ile bir parametre yollanınca hata vermesini engelleyebiliyoduk
#fakat 3 parametre yollanınca hata vermesini engelleyemiyoduk
#bunun çözümü şudur def fonk.adı(*params) yazarsak biz kaç parametre girersek o kadar parametreli olur
#basit örneği aşağıda ileride detaylı incelenecektir
#burada *... yapınca girilen parametreyi tuple olarak alır

#şimdi şunu düşünelim *... ile parametre gönderirken biz hep int veri göndermiyeceğiz
#mesela yaş isim gibi şeyler göndericez bunun içinde normalde dictionary kullanırdık
#bunu da parametre başına "**" koyarak yaparız

#------------------------------------------------------------------------------------------------------------------------------------

#bir örnek
def changeName(n):
    n = "ada"

name = "yigit"
changeName(name)
print(name)

#aynısını listeler üstünde yapma
def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir", "bolu"]
change(sehirler)
print(sehirler)

#bir örnek listenin parametre olmasını anlaman için
#burada ikiside artık pointer oldu
n = sehirler
n[0] = "değiştirildi"
print(sehirler)

#slicing işlemi
n = sehirler[:] #kopyalama işlemi slicing ile
n[0] = "ikinci değişiklik"
print(n)
print(sehirler)

#listeleri value şeklinde fonksiyona atma
def parcalama(n):
    n[0] = "parcalama fonk. çalıştı"
    print(n)

parcalama(sehirler[:])
print(sehirler)

#parametre için *params örneği
#aslında en temelde *... şeklinde girince bir tuple olarak parametreyi alır
def add(*params):
    return sum((params))

print(add(1,2,3,4))
print(add(1,2,3,4,5))

#dictionary gibi parametre yollama
#dictionary gelecek demek için iki "*" ekleriz
def displayUser(**args):
    for key,value in args.items():
        print(f"{key} is {value}", end = " ")
    print()

displayUser(name = "enes", age = 21, city = "ankara")
displayUser(name = "erkam", age = 23, city = "zonguldak", phone = "iphone")
displayUser(name = "onur", age = 22, city = "izmir", phone = "iphone", email = "...")
