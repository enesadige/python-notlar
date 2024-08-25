#pythonda match-case

#aslında bu eğitimde yok ama ben araştırıp ekledim
#python dilinde normalde c++ dilindeki switch-case yapısı yok fakat bir güncelleme ile buna benzer bir komut eklendi
#aynı c++daki gibi bir girdi yazar girdinin değerine göre caseler yazarız
#eğer hiç bir case'i sağlamıyosa diye c++daki default seçeneği yerine case _: yazarız 

#sadece bir değer değil örneğin bir liste ile de eşleştirilebilir 
#ve birden çok case için bir ifadeyi kullanmak istersek " | " kullanırız aşağıda örneği var
#4 örnek verildi en sondaki örnek önemli

#---------------------------------------------------------------------------------------------------------------------

#örnek 1;
x = int(input("x değerini giriniz : "))

match x:
    case 1:
        print("sayı 1'dir")
    case 2:
        print("sayı 2'dir")
    case _:
        print("sayı 1 ve 2 değildir")

#örnek 2;
y = [1,2]

match y:
    case [1,2]:
        print("true")
    case _:
        print("false")

#örnek 3;

z = int(input("günün haftanın kaçıncı gün olduğunu giriniz : "))

match z:
    case 1|2|3|4|5:
        print("hafta içidir")
    case 6|7:
        print("hafta sonudur")
    case _:
        print("yanlış girdi")

#örnek 4

name = input("adınızı giriniz : ")
age = int(input("yaşınızı giriniz :"))

bilgi = (name,age)

match bilgi:
    case (name,age) if age>18:
        print(f"{name} bir reşittir.")
    case (name,age):
        print(f"{name} reşit değildir.")
    case _:
        print("hata... hata kodu : 502")