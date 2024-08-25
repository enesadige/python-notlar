#pythonda sets

#sets aslında listelere benzer
#tek farklılığı burda elemanları indekslenemez yani print(fruits[0]) gibi bir kod satırı kullanamam hata verir
#elemanlarına döngüler ile ulaşılabilir daha öğrenmedik ama örneğini aşağıda yazdım
#elemanlar sets içinde sırasızdır yani indekslenemediğinden her seferinde sıraları değişebilir
#yani elemanları bir torba içine atar gibi düşün hepsi barınıyo fakat sırası yok
#***burada önemli kısım burada bir eleman set içinde sadece bir kere olabilir yani set içinde iki tane "apple" olamaz

#.add() ile içine eleman ekleyebiliriz
#.update(["...","..."]) ile içine liste götürebiliriz, burada listedeki tüm elemanları .add() ile eklemiş gibi olur
#.remove("...") ile bir elemanı silebiliriz 
#.discard("...") ile de silme işlemi yapabiliriz
#burada .pop() çalıştırmak tehlikelidir çünkü normalde bu son elemanı siler fakat setlerde elemanlar sırasız olduğundan hangi elemanı sileceği belli değildir
#.clear() ile tüm elemanları silebiliriz

#bir elemanı bir kere yazdıracağının aşağıda örneği var

#---------------------------------------------------------------------------------------------------------------------

fruits = {"orange", "apple", "banana"}
print(type(fruits))
print(fruits)
print()

#daha öğrenmedik ama örneği 
for x in fruits:
    print(x)
print()

#yeni eleman eklemek için
fruits.add("cherry")
print(fruits)
print()

##liste eklemek için
fruits.update(["mango", "grape"])
print(fruits)
print()

#silmek için
fruits.remove("mango")
fruits.discard("apple")
print(fruits)
print()

#hepsini temizle
fruits.clear()
print(fruits)
print()

#bir elemanı bir kere yazdıracağının örneği
my_list = [1,2,3,3,4,4,5,5,5]
print(my_list)
print(set(my_list))


