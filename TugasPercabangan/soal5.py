bilangan1 = int(input("Masukkan bilangan pertama : "))
bilangan2 = int(input("Masukkan bilangan kedua : "))
bilangan3 = int(input("Masukkan bilangan ketiga : "))

if bilangan1 > bilangan2 and bilangan1 < bilangan3 or bilangan1 < bilangan2 and bilangan1 > bilangan3:
    print("Bilangan tengah adalah bilangan 1, yaitu bilangan dengan nilai", bilangan1)
elif bilangan2 > bilangan1 and bilangan2 < bilangan3 or bilangan2 < bilangan1 and bilangan2 > bilangan3:
    print("Bilangan tengah adalah bilangan 2, yaitu bilangan dengan nilai", bilangan2)
elif bilangan3 > bilangan1 and bilangan3 < bilangan2 or bilangan3 < bilangan1 and bilangan3 > bilangan2:
    print("Bilangan tengah adalah bilangan 3, yaitu bilangan dengan nilai", bilangan3)
else:
    print("Tidak ada bilangan karena terdapat bilangan yang sama")
