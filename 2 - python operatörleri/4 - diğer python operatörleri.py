#python dilindeki diğer operatorler

#is ve in operatörlerini göreceğiz burada

#burada referans kavramının önemi gözüküyo
#şöyle : x ve y aşağıda aynı referansa işaret ediyo fakat z, x'den farklı referansa işaret ediyo
#biz x==z desek true çeviricek çübkü değerleri aynı fakat x is z false çevirir çünkü işaret ettikleri bellek adresleri farklı
#burada da "not" kullanabiliriz

#in operatöründe ise burada ise in ifadesinin soluna yazdığımız şey sağdakinin içinde var mı ona bakarız

#---------------------------------------------------------------------------------------------------------------------

x = y = [1,2,3]
z = [1,2,3]

#is operatörü
print(x is y)
print(x is z)
print(x is not z)
print()

#in operatörü
print(1 in z)
print(1 not in z)
name = "enes"
print("e" in name)


