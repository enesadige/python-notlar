#pythonda value ve reference

#burada aşağıdaki ilk kısımdan da göreceğiniz üzere bir x,y tanımladık değerler atadık sonra x = y yaptık
#fakat daha sonra y yi değiştirdik baktık x = y yazılı olsa da değişiklik x'e yansımadı

#fakat reference typelarda iş farklı aşağıda örneği var a ve b listeleri tanımlayıp sonra a = b yapıyoruz
#sonra bu koddan altta başka satırda b üzerinden değişiklik yapıyoruz ve b'deki değişiklik a'ya da yansıyo
#** çünkü burada = ile birbirine eşitledikten sonra bunlar iki ayrı listede aynı adresi gösterir bi nevi pointera dönerler
#---------------------------------------------------------------------------------------------------------------------

#value type => string, int ...
x = 5
y = 25
x = y
y = 10
print(x,y)
print()

#reference type => class, list ...
a = ["apple", "banana"]
b = ["apple", "banana"]
a = b
b[0] = "grape"
print(a,b)
print()