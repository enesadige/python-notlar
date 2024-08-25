import os; os.system("clear")
#python dilinde lambda expressions, map ve filter nedir

#örneğin elimizde bir liste olsun ve bu listedeki her sayının karesini almak için bir fonksiyon yapalım
#normalde tek tek metodlar ile liste elemanlarını alabiliriz ama bunun başka bir yolu lambdadır

#map metodu ile dizi üstündeki her elemana ulaşıp bunu fonksiyondan geçirebiliriz
#map metodunun kullanım şekli aşağıda verilmiştir
#biz bu map metodunun liste türünü almamız ya da for döngüsü ile bir değişkene bu fonksiyon ve liste işleminin sonucunu atmamız gerekir

#lambda ise şudur biz bir kareal fonksiyonu tanımlayıp onu map içine atmak yerine map içinde direkt bir kere kullanılacak isimsiz bir fonksiyon tanımlayabiliriz
#aşağıda nasıl yapılacağının örneği var
#bu sayede bir fonksiyonu bir kere kullanıp atıcaksak böyle bi fonksiyon tanımlamak yerine lambda ile halledebiliriz

#bir diğer kullanımı da şöyledir lambda ile oluşturulmuş işlemlere bir isim verebiliriz ve daha sonra map içinde direkt bu ismi de kullanabiliriz
#ama bunun için o isimle o lambda işlemlerinin tanımlanmış olması gerekiyor
#daha sonra bu lambdayı bir fonksiyon gibi de kullanabiliriz

#şimdi gelelim filtere bu şu demek aslında aşağıda biz lambda ile yazdık ve mapa gönderdik
#mapa gönderdiğimiz numbersin tüm elemanları için işlem yaptı ama biz bu elemanları bi filtreden geçirmek istersek bunu kullanırız
#bunu da filter işlemi ile yaparız aşağıda örneği var 

#-----------------------------------------------------------------------------------------------------------------------------------------------

def kareal(num) : return num**2

numbers = [1,2,3,4,5]

#-----------------------------------------------------------------------------------------------------------------------------------------------
#map kullanımı

#list()ile resulta atma burada liste oluşturup onu ekrana yazar
result = list(map(kareal, numbers))
print(result)
print()

#for döngüsü ile atma burada tek tek ekrana yazar
for item in map(kareal, numbers):
    print(item)
print()

#-----------------------------------------------------------------------------------------------------------------------------------------------

#lambda kullanımı
result = list(map(lambda num: num**3, numbers))
print(result)

#lambdaya isim verme
ikikat = lambda num: num*2
sonuc = list(map(ikikat, numbers))
print(sonuc)

#fonksiyon gibi kullanımı
print(ikikat(3))

#-----------------------------------------------------------------------------------------------------------------------------------------------

#filter işlemi
sayilar = [1,2,3,4,5,6,7,8,9]

check_even = lambda num: num%2==0
result = list(filter(check_even, sayilar))
print(result)
