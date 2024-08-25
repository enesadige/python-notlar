#pythonda dictionaryler

#bu aslında key => value mantığı ile çalışır
#yani 34 => istanbul bilgisini saklamak için diyebiliriz basit tabirle

#öncelikle burda değerleri {} içine yazarız 
#şu şekilde yazılır {"key" : "value"}
#listede örneğin ankara yokken plakalar["ankara"] = 06 yazarsam listenin sonuna bunu ekler
#value değiştirmek istersem örneğin plakalar["kocaeli"] = new_value_değeri yazmam yeterlidir
#birden çok value bilgisi girebiliriz
#bu bilgilere tek tek erişmek için de [][] gibi iki tane kapalı parantez kullanırız örneği aşağıda verilmiştir

#bilgileri kullanıcıdan alarak bir dict. oluşturma örneği aşağıdadır
#bir de bu bilgileri .update()ile de yapabiliriz
#---------------------------------------------------------------------------------

plakalar = {"kocaeli":41, "istanbul":34}
print(plakalar["kocaeli"])
plakalar["ankara"] = 6
print(plakalar)
plakalar["kocaeli"] = "new_value"


users = {
    "enes daşcı" : {
        "age" : 21,
        "roles" :["admin"],
        "email" : "enesdasci@gmail.com",
        "adres" : "istanbul",
        "telefon no" : "05001001010"
    },
    "duran daşcı" : {
        "age" : 65,
        "roles" : ["admin","user"],
        "email" : "durandasci@gmail.com",
        "adres" : "istanbul",
        "telefon no" : "05002002020"
    }
}

print(users["enes daşcı"])
print(users["enes daşcı"]["age"])
print(users["duran daşcı"]["roles"])
print(users["duran daşcı"]["roles"][0])

#kullanıcıdan girdi ile oluşturma
ogrenciler = {}
number = input("öğrenci no :")
name = input("öğrenci adı :")
surname = input("öğrenci soyadı :")
phone = input("öğrenci telefon :")

ogrenciler[number] = {
    "ad": name,
    "soyad": surname,
    "telefon": phone
}

#update() ile kullanımı
number = input("öğrenci no :")
name = input("öğrenci adı :")
surname = input("öğrenci soyadı :")
phone = input("öğrenci telefon :")

ogrenciler.update({
    number:{
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print(ogrenciler)
print()

ogrNo = input("öğrenci no : ")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)