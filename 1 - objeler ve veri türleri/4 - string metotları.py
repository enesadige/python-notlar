#STRİNG METOTLARI

#upper() metodu bütün karakterleri büyük harfe çevirir
#lower() da tam tersi
#title() ise her kelimenin başını büyük harfe çeviri
#capitalize() ise verilen stringin sadece ilk harfini büyüğe çevirir
#strip() metodu ise baştaki ve sondaki boşlukları siler
#strip() de parantez içine bir şey yazarsak bunları siler özelleştirilebilir yani
#split() metodu ise stringde her boşlukta böler ve ayrı ayrı char dizisi gibi kelimeleri sınıflandırır ()içine bir şey yazarsak ondan itibaren böler
#burada biz örneğin 5.kelimesine erişmek istersek message.split()[4] yazarız
#bir de birleştirme vardır yani böldük split ile şimdi birleştirmek için şunu yaparız >> " ".join(message) yazarsak "" içindeki ifadeleri gördükce birleştirir

#bir de cümle içinde kelime arama vardır aşağıda yazan .find() metodu bu kelime varsa pozitif yoksa negatif değer dönderir
#bir de .startswith() metodu vardır parantez içine yazdığımız şeyle başlıyosa ifade true dönderir
#bir de tersi endswith() vardır tam tersi bittiğine bakar
#bir de replace("ifade", "ifade") vardır parantez içine yazdığımız ilk ifadeyi arar yerine ikinciyi yazar ama orada yazar string ifadede değiştirmez

#önemli bir metod: center() metodu bu metodda parantez içine girdiğimiz boyuta çıkarır stringi başına ve sonuna boşluk ekleyerek ve tam ortalar
#bu metodda istersek boşluk eklemek yerine parantez içine ne ekleyeceğini de koyabiliriz
#bir de istersek sadece sağına ya da soluna ekletebiliriz bunun içinde .ljust ya da .rjust kullanırız

#yazılan şey alfabetik mi ya da sayısal mı isdigit() ve isalpha() ile kontrol ederiz

#---------------------------------------------------------------------------------------------------

message = "my name is enes daşcı"
message_two = " xx my name is enes daşcı xy "
print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())
print(message_two.strip())
print(message_two.strip("xy "))
print(message.split())
print(message.split("is"))
print(message.split()[2])
print()

message = message.split()
print(message)
message = " ".join(message)
print(message)

print(message.find("name"))
print(message.find("yok"))

print(message.startswith("m"))
print(message[4:].startswith("a"))
print(message.endswith("ı"))
print(message.replace("daşcı", "adige"))

print(message.center(50))
print(len(message.center(50)))
print(message.center(50, "-"))
print(message.ljust(30, "-"))
print(message.rjust(30, "-"))

mesaj_bir = "123456"
mesaj_iki = "enes daşcı"
mesaj_uc = "enes 123"
print(mesaj_bir.isdigit())
print(mesaj_iki.isalpha())
print(mesaj_uc.isdigit())
print(mesaj_uc.isalpha())