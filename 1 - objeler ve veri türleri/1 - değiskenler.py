#değişken tanımlama - variables

#değişken tanımlarken c++ dilindeki gibi int, float gibi şeyleri başına yazmamıza gerek yoktur pythonda
#burada değişken kuralları c++ diline benzerdir yani aynı isimde birden çok değişken oluşturulamaz
x = 5       #int
y = 5.1     #float
z = 'a'     #char
a = "enes"  #string
b = "daşcı"
c = True    #bool
x = y #burada çok basit şekilde değer atıyabiliriz ve tür dönüşümüne gerek yoktur

#pythondaki çıktı komutu "print()" dir
print(x)
print(y)
print(z)
print(a)
print(b)
print(a + '\n' + b) #string ifadeler bu şekilde birleştirilebilir
print(int(b)) #normalde true değerini yazdırırken true yazar böyle yapınca 1 yazar
print('\n') #bu da alt satıra geçme aynı c++ ile

#matematiksel ifadeler aşağıdadır
sayi1, sayi2, sayi3 = 1, 2, 3
print(sayi1 + sayi2)
print(sayi1 - sayi2)
print(sayi1 * sayi2)
print(sayi1 / sayi2)
print(sayi1 % sayi2)  #kalanı verir
print(sayi1 // sayi2) #tam sayı bölmesidir int değer çevirir
print(sayi1 ** sayi2) #üs alma işlemidir 1. sayı, 2. üs olur


