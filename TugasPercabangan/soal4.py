bilangan1 = int(input("Masukkan bilangan pertama : "))
bilangan2 = int(input("Masukkan bilangan kedua : "))
bilangan3 = int(input("Masukkan bilangan ketiga : "))
if bilangan1 > bilangan2 and bilangan1 > bilangan3:
    print("Bilangan terbesar adalah bilangan 1, yaitu bilangan dengan nilai", bilangan1)
elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
    print("Bilangan terbesar adalah bilangan 2, yaitu bilangan dengan nilai", bilangan2)
elif bilangan3 > bilangan1 and bilangan3 > bilangan2:
    print("Bilangan terbesar adalah bilangan 3, yaitu bilangan dengan nilai", bilangan3)
elif bilangan1 == bilangan2 == bilangan3:
    print("Ketiga bilangan sama besar, yaitu bilangan dengan nilai", bilangan1)
elif bilangan1 == bilangan2 and bilangan1>bilangan3:
    print("Bilangan yang terbesar adalah bilangan ke 1 dan bilangan ke 2, yaitu bilangan dengan nilai", bilangan1)
elif bilangan2 == bilangan3 and bilangan2 > bilangan1:
    print("Bilangan yang terbesar adalah bilangan ke 2 dan bilangan ke 3, yaitu bilangan dengan nilai", bilangan2)
elif bilangan1 == bilangan3 and bilangan3 > bilangan2:
    print("Bilangan yang terbesar adalah bilangan ke 1 dan bilangan ke 3, yaitu bilangan dengan nilai", bilangan1)