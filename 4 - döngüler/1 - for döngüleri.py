#

#burada da for döngüsünün amacı c++ dilindeki anlama benzerdir fakat syntaxı farklıdır

#aşağıdaki ilk örnek python dilindeki klasik for döngüsüdür bu döngü genellikle bir listenin elemanları yazdırılacağı zaman kullanılır
#ama aslında bu ilk klasik döngünün amacı şu : listenin eleman sayısı kadar for döngüsü yapmk
#end parametresi şu işe yarar mesele c++ da ben döngüden sonra alt satıra geçmesini istersem print('\n') yapıyodum istemezsem yapmıyodum
#pythonda end parametresi kullanmazsak hep alt satıra geçer döngü bitince
#for döngüsüne iki parametre girilebilir for a,b in my_list: gibi

#dictionary yazdırırken for döngüsüne klasik şekilde sokarsak sadece key bilgilerini ekrana yazdırır
#key ve valueyi yazdırması için şunu yaparız >> for item in my_dict.items(): print(item) yazarsak iki bilgiyi de yazar

#pythonda döngünün kaç kere döneceğini range(değer) ile yaparız

#liste üzerinde hem indekslere hem de değerlere ihtiyaç varsa;
#enumerate(liste_Adı) komutunu kullan

#bir de zip() kullanımı vardır zip() iki liste arasında eşleştirme yapar
#bunu liste ya da dict gibi şeyler yapabilirsiniz


#---------------------------------------------------------------------------------------------------------------------

#bir liste oluşturalım
numbers = [1,2,3,4,5]

#birinci kalıp for döngüsü ve end parametresi kullanımı
#end parametresi her döngüden sonra alt satıra geçmek yerine ne yapması gerektiğini söylemek için
for num in numbers:
    print(num, end=" ")
print()

#klasik for döngüsü listenin eleman sayısı kadar döngü yapar
for a in numbers:
    print(f"hello{a}", end=" ")
print()

#bir string ifadeyi sokarsak döngüye her karakterini yazar
name = "enes daşcı"
for n in name:
    print(n)
print()

#for döngüsünde iki parametre tanımlanabilir 
my_list = [(1,2),(3,4),(5,6)]
for a,b in my_list:
    print(f"a = {a}, b = {b}")
print()

#---------------------------------------------------------------------------------------------------------------------
#dictionary örneği
my_dict = {"k1":1, "k2":2, "k3" : 3}

#sadece key yazıcak
for item in my_dict:
    print(item, end = " ")

#valueleri de yazıcak >> .items() metodu ile
for item in my_dict.items():
    print(item, end = " ")
print()

#key ve valueyi ayrı ayrı kullanabilmek için
for key,value in my_dict.items():
    print(f"{key} :", end = " ")
    print(value, end = " ")
print()

#---------------------------------------------------------------------------------------------------------------------
#pythonda kaç kere döneceğini direkt girebiliriz
#*** önemli bilgi : range(5) yaparsam sıfırdan başlayıp 5 e kadar gider
#*** range(2,5) yaparsam 2 den başlayıp 5 e kadar gider
#artış miktarı da belirtilebilir range(1,10,2) yaparsam 2 2 artar
for i in range(5):
    print(i, end = " ")
print()
for i in range(2,5):
    print(i, end = " ")
print()
for i in range(2,10,3):
    print(i, end = " ")
print()
print("\n"*2)

#enumerate kullanımı indekslere ulaşmak için
meyve = ["apple", "banana", "cherry"]
for index, fruits in enumerate(meyve):
    print(f"{index} : {fruits}")
print()

#zip() kullanımı eşleştirme yapar
    
list_one = [1,2,3,4,5]
list_two = ["a","b","c","d"]
list_three = [True, False, True, False, True]

for item in zip(list_one,list_two,list_three):
    print(item, end = " ")