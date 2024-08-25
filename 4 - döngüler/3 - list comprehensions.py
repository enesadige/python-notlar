
#pythonda list comp.lar

#aslında bunlar for ve while döngüsüne alternatif bir yöntemdir
#aşağıdaki gibi örneğini yaparak numbers içine dizi olarak atıyacağım
#burada her alınan değer üzerinden de işlem yapılıp öyle aktarılabilir
#örneğin numbers = [x**2 for x in range(10)] buradaki x**2 kısmı işlem kısmıdır
#başka koşullarda ekleyebiliriz

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#x değerini dizi olarak listeye atmanın uzun ve kısa yolu
#uzun yol
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)
print()

#kısa yolu
numbers = [x for x in range(10)]
print(numbers)
print()

#ek koşullar
numbers = [x for x in range(10) if x%3==0]
print(numbers)
print()

#ek koşul kullanımı - 2
results = [x if x%2==0 else f"{x} : tek" for x in range(10)]
print(results)
print()

#string ile kullanımı
my_string = "hello"
my_list = []
my_list = [letter for letter in my_string]
print(my_list)
print()

#örnek : yaş bilgisini hesaplatma 2023 de 
years = [1998,2020,2003,2002]
ages = [2023 - year for year in years]
print(ages)
print()

#iç içe döngülerle kullanma
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
print()