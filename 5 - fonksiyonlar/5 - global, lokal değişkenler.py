import os; os.system("clear")
#python dilinde global ve lokal değişkenler

#global ve lokal değişkenler c++ dilindeki anlamlarıyla aynı anlama gelirler
#fonksiyonlar kendi içinde bir çalışma alanı oluşturur ve daha sonra sadece bu alandaki ifadeler bu alanı etkiler
#burada şu detay da var fonksiyon içinde global olan bir değişken için bir değişiklik yapılmazsa fonksiyon içindeki örneğin print ifadesinde de global değerini çıktı verir

#iç içe fonksiyonlarda en içteki fonksiyon içinde olduğu fonksiyondaki değişken değerleri ile iş yapar
#eğer içinde olduğu fonksiyonda bir işlem yoksa o değişkenin global değerini alır
#eğer en içteki fonksiyon değişkene kendi işlem yaparsa kendi yaptığını kullanır

#global değişkeni fonksiyon içinden de değiştirmenin yolu var aşağıda örneği yazılı

#--------------------------------------------------------------------------------------------------------------------------------

#burada global ve lokalin ne olduğunun basit özeti var
x = "global x"

def func():
    x = "local x"
    print(x)

func()
print(x)
print()

#iç içe örneği
name = "enes"
def greeting():
    name = "erkam"
    def say():
        print(f"hello {name}")
    say()
greeting()

#iç içe ikinci örnek
def greeting_two():
    name = "erkam"
    def say():
        name = "onur"
        print(f"hello {name}")
    say()
greeting_two()
#--------------------------------------------------------------------------------------------------------------------------------
#global değişkene fonk içinden değişiklik yaptırma

x = 50
def test():
    global x #global olarak değişiklikler yapmak için
    x = 100
test()
print(x)