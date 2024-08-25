#python dilinde tuple nedir

#aslında tuple şu demektir sabit liste yani aslında tuple da tek bir eleman üzerinde değişiklik yapmamıza izin vermiyo
#eleman eklenemez, çıkarılamaz, değiştirilemezdir yani
#oluştururken listeden tek farkı [] yerine () kullanırız ya da hiç kullanmayız

#genellikle çok az metodu vardır count() ve index() gibi
#count() kaç tane olduğunu yazarken index() indeks numarasını yazar

#burada da "+" ile iki tuple ı toplayıp bir başka tuple a koyabiliriz

#--------------------------------------------------------------------------------------------------------------------------------------------

list = [1,2]
tuple = (3,4,4)

print(type(list))
print(type(tuple))

print(tuple.count(4))
print(tuple.index(4))