#python dilinde atama operatörleri

#python dilinde aynı satırda birden çok değişken oluşturup değer oluşturabiliyoruz
#burada da c++ dilindeki gibi örneğin x += 5 gibi ifadeler kullanabiliyoruz

#bunu tuple ile kolay bi kullanımını görelim yani 3 elemanlı bir tuple ı a,b,c değişkenlerine otomatik atamayı gösterelim aşağıda
#burada önemli kısım : örneğin values 5 elemanlı olsun biz a,b,c ye atarken:
#a,b,*c = values yaparsak ilk iki değeri  a ve b ye atar kalanı c ye dizi şeklinde atar
#fakat burada "*" koymadan 5 elemanlı listeyi 3 değişkene atamaya çalışırsak hata verir
#ve ek olarak yıldızı b ye koyduk diyelim ilk elemanı a ya atar sonra c için son elemanı saklar kalanı b ye dizi olarak atar
#biz * ı a'ya koysaydık 3 değişkene 5 eleman atamaya çalıştığımızdan son iki elemanı b ve c ye atar başta kalanları a'ya dizi olarak atardı
#---------------------------------------------------------------------------------------------------------------------

x,y,z = 5,10,15
x,y = y,z
print(x,y,z,)
print()

#bir örnek yeterli sadece dört işlem değil % gibi ifadelerde kullanılabilir
x += 5
print(x)
x //= 2 #bölmenin int kısmını almak için bir ifade "//"
print(x)
print()

#tuple ile otomatik elemanları atama
values = (1,2,3)
a,b,c = values
print(type(values), " ", values, "\n")
print(a,b,c)
