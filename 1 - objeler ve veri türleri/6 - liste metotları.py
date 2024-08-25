#pythonda liste metotları

#min(list_name) ile listedeki minimum değeri alırız
#belirli elemanı almak için stringe benzer list[3:6] gibi yazarız
#liste üzerine eleman eklemek için .append(değer) metodu kullanırız
#indeks ile istediğimiz konuma eleman ekleyebiliriz
#pop() metodu ile listeden eleman sileriz parantez içine bir şey yazmazsak sondakini yazarsak yazdığımız indeksteki elemanı siler
#remove() metodu ile ise silmek istediğimiz elemanın ismini değerini girerek indeksiyle uğraşmadan silebiliriz
#sort() metodu ile listedeki şeyler alfabetik ya da sayısal olarak sıralanır
#sort() ile yaptığımızın tam tersini yapmak için .reverse() metodunu kullanırız
#count(değer) ile içinde o değerden kaç tane var bunu sayabiliriz örneğin listede 6 tane 10 değeri olsun bu durumda count(10) ekrana 6 yazdırır
#clear() metodu ile tüm elemanları siler listeyi boşaltırız


#-----------------------------------------------------------------------------------------------------------------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,0]
letters = ["a","b","c","d","e","f"]

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val = min(letters)
print(val)
val = max(letters)
print(val)

print(numbers[3:6])

numbers.append(10)
numbers.insert(3,11)
print(numbers)
numbers.pop()
numbers.pop(3)
print(numbers)

numbers.remove(7)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
print(numbers.count(0))
numbers.clear()
print(numbers)
