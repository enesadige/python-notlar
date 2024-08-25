#pythonda if else yapısı

#burada öncelikli bilgi python dilinde döngü ya da koşullarda çalıştırılacak kodlar için c++ dilindeki gibi {} ifadeleri yok
#bunu sağlamak için şunu yaparız : içinde yazdırılacak kodları alt satırda koşuldan daha ileride yazarız boşluk ya da tab ile
#ve çalışacak kodlar hep aynı düzeyde olmalıdır bu satır düzeni bozulunca o bloktan çıkar

#if için mantık ve koşul operatörleriyle bir kısım belirleriz ve yazılan şey true çevirirse çalışır
#burada else if ifadesini kullanmak için elif şeklinde yazarız pythonda

#---------------------------------------------------------------------------------------------------------------------

#basit hali
if 3==3:
    print("koşul sağlandı\n")
else:
    print("koşul sağlanmadı\n")

#bir örnek daha 
username = input("kullanıcı adınızı giriniz : ")
password = input("şifreyi giriniz :")

if username=="enes.adige" :
    if password=="1234":
        print("hoşgeldiniz...\n")
    else:
        print("parola yanlış...\n")
else:
    print("kullanıcı adı yanlış...\n")

#else if ile kullanımı

x = int(input(":"))
y = int(input(":"))

if x>y:
    print("x büyüktür")
elif x==y:
    print("x , y'ye eşittir")
else:
    print("y büyüktür")