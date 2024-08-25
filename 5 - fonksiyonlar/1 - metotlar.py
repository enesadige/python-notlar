import os; os.system("clear")
#python dilinde metotlar

#öncelikle method bir nevi özel fonksiyonlardır
#yani python kütüphanesi ile birlikte gelen özel fonksiyonlardır
#mesela list.append() buradaki .append metoddur

#daha doğru bir tanım yaparsak metodlar python kütüphanesinde standart gelen sınıflardır 
#yani list. ile çağırdığımız metodlar aslında list adında oluşturulmuş class içindeki fonksiyonlardır


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#method örneği
list = [1,2,3,4,5]

#append() metoddur örneğin
list.append(11)

#bunların hepsinin standart gelen bir class olduğunu görme
print(type(list))

