#string ve char işlemleri 

#------------------------------------------------------------------------------------------

#python dili her string ifadeyi ya da char ifadesini de string  yani karakter dizisi olarak algılar
#indeksler c++ diline benzer ve 0 ile başlar
#x = "enes" ifadesinde x[0] = "e" dir
#len() ifadesi karakter sayısını verir
#dolayısıyla son karakteri yazdırmak için print(x(len(x))) yazarım
#string ifadenin belli bir kısmını yazdırmak için print(x[2:5]) yazabiliriz indeksi iki ile beş arasındakileri yazar
#bir de şu ifade vardır print(x[2:40:2]) bu şu demek iki karakterde bir al

#------------------------------------------------------------------------------------------

name, surname = "enes", "daşcı"
age = 21
greeting = "My name is : " + name + " " + surname + " and I'm " + str(age) + " years old."
print(greeting, " ")
print(greeting[0], " ")
print(greeting[1], " ")
print(len(greeting), " ")               #karakter sayısını verir
print(greeting[len(greeting)-1], " ")   # son karakteri yazdırır, -1 indeksler 0'dan başladığından dolayı
print(greeting[-1], " ")                #bu da son karakteri yazdırmanın farklı yolu   
print(greeting[0:10], " ")              #belli kısmını yazdırmak için indeks numaralarıyla
print(greeting[4:], " ")                #istediğimiz yerden yazmaya başlaması için
print(greeting[0:-1:2])                 #bir karakter yaz bir karakteri atla demek gibi bir şey

#------------------------------------------------------------------------------------------

#STRİNG FORMATLAMA

#tek tek böyle + ile vesaire uğraşmadan yazdırmak için
#örneğin "ifade {}".format(değişken adı) komutunu kullanabiliriz
#böyle yapınca {} içine o stringi yazar
#bunu birden çok ekleyebiliriz
#ek bilgi : {} yazınca bunlara format içinden bir indeks gelir 
#yani format içinde aşağıda isimin indeksi 0, soyisiminki 1'dir
#ben süslü parantez içine indeks yazarak yer sıra değiştirebilirim
#aşağıda bu .formatın diğer bir kullanımı da bulunmaktadır

isim = "enes"
soyisim = "daşcı"
yas = 20
print("My name is {} {}".format(isim, soyisim))
print("My name is {1} {0}".format(isim, soyisim))
print("My name is {n} {s}".format(n=isim, s=soyisim))
 

#bir de fstring vardır bu da .format ile hiç uğraşmadan değişkenleri yazı içinde yazdırmamıza yarar
print(f"My name is {isim} {soyisim}")


#şimdi aşağıda bir float sayının kaç basamağını yazdırmak istersek nasıl yapacağımızı göstericez
#aşağıda {}içindeki r = 1.3 >>soldaki sayı tam kısım için ayrılan basamak sayısını, sağdaki sayı ise virgülden sonra kaç basamağı yazılacağını gösteriyo

result = 200/700
print("the result is ",result)
print("the result is {r:1.4}".format(r=result))


