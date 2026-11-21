angka = int(input("Masukkan Bilangan : "))
if angka > 0:
    if angka %2 != 0:
        print("Bilangan tersebut merupakan bilangan positif ganjil")
    else:
        print("Bilangan tersebut merupakan bilangan positif genap")
elif angka < 0:
    if angka %2 != 0:
        print("Bilangan tersebut merupakan bilangan negatif ganjil")
    else:
        print("Bilangan tersebut merupakan bilangan negatif genap")
else:
    print("Bilangan tersebut merupakan bilangan netral")