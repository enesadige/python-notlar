#python dilinde veritürü dönüşümleri

#python dilinde değişkeni önceden tanımlaman gerekmez ihtiyacın olduğunda direkt değer ataması için yazıp aynı satırda değeri atayabilirler
#python dili input ifadesini bir şey belirtmezsek her zaman string olarak algılayacaktır
#yani input olarak 123 girilse bunu string algılar int algılaması için 
#int() yazıp parantez içine input ifadesini yazmamız gerekir
#ya da input aldıktan sonra işleme sokarken örneğin x değişkeni olsun int(x) ile işlem yaparsak int algılar
#tür dönüşümü yaparken stringe çevirmek için str() ile yaparız sting() ile değil

#------------------------------------------------------------------------------------------

#1.örnek
a = int(input("a sayısının değerini giriniz : "))
print(a)

#2.örnek
b = input("b sayısının değerini giriniz : ")
print(b, ", türü = ", type(b))        #burada da 10 yazıcak ama türü string olarak
print(int(b), ", türü = ", type(int(b)))   #burada da ama türü int olarak
print() #altsatıra geçmek için endl gibi düşün 

#------------------------------------------------------------------------------------------

#biz tür dönüşümü için şunu yaparız
#aşağıdaki şekilde tür dönüştürebiliriz
sayi_bir = 5
sayi_bir = float(sayi_bir)
print("değeri : ", sayi_bir, ", türü = ", type(sayi_bir))
sayi_bir = str(sayi_bir)
print("değeri : ", sayi_bir, ", türü = ", type(sayi_bir))
