#python dilinde while döngüsü

#buradaki while döngüsünün amacı da c++dakine benzerdir sadece syntaxı farklıdır
#while not ifadesi vardır bu da değer false olduğu sürece çalışır
#burada da break ve continue komutları vardır

#aşağıda kullanıcı girişi ile ilgili kullanım örneği vardır
#pythonda string ifade boşsa bu false kabul edilir
#yani name = "" ifadesinde bool(name) = False'dur



#--------------------------------------------------------------------------------------------------------------

#ilk basit while
x = 0

while x < 10:
    print(x, end = " ")
    x+=1
print("bitti")
print()

#break ifadesi, koşul sağlansa bile döngüyü durdurur
x = 0
while x < 10:
    x+=1
    if x >= 5:
        break
    print(x, end = " ")
print()

#continue kullanımı koşul sağlansa bile onu atlar devam eder
x = 0
while x < 10:
    if(x%2==0):
        x += 1
        continue
    else:
        print(x, end = " ")
        x += 1
print()

#kullanıcı girişi ile kullanımıi while not ile
name = ""
while not name:
    name = input("name is : ")

print(f"name is {name}")
