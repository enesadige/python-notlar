#python dilinde listeler

#aslında dizilere benzerdir listeler
#listelerde her eleman aynı türde olmak zorunda değil bir elemanı int bir elemanı string olabilir
#aşağıdaki gibi yeniden listenin elemanlarına değer atanabilir değiştirilebilir aynı şekilde eleman sayısı da böyle
#yeni bir liste oluşturuş iki listenin elemanlarını birleştirip yeni bir liste oluşturabiliriz
#örneğin list3 = list1 + list2 ile iki listi birleştirebiliriz
#burada şunu unutma : ben aşağıda my_list için string ifade de ekledim içine len(my_list) yapınca stringin her karakterini 1 olarak saymaz stringin hepsini direkt bir eleman olarak alır

#liste içinde liste saklamak için : şöyle yaparız örneğin >> list4 = [list1, list2] yani köşeli paranteze alır listeleri virgülle ayırırız
#in operatörü ile bir elemanın var olup olmadığını kontrol edebiliriz
#yani 1 sayısı elemanı ise 1 in my_list True çevirir
#del komutu ile eleman silebiliriz

#--------------------------------------------------------------------------------------------------

my_list = [1,2,3]
my_list = ["bir", 2, True, 5.6]
print(my_list)
print(my_list[0])
print(my_list[1])

list1 = [1,2,3]
list2 = [3,4,5]
list3 = list1 + list2
print(list3)
list4 = [list1, list2]
print(list4)
print(list4[0])
print(list4[0][0])
print(1 in list3) 
del my_list[-1]