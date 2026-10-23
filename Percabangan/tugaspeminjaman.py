jumlahpinjam = int(input("Inputkan jumlah buku yang dipinjam = "))
lamapinjam = int(input("Inputkan lama peminjaman = "))
haritelat = lamapinjam - 7
if lamapinjam > 7:
    denda = 2000 * haritelat * jumlahpinjam
    print("Lama peminjaman", lamapinjam, "hari, Jumlah hari terlambat :", haritelat, "hari dan besarnya denda adalah", denda)
else:
    print("Jumlah buku yang dipinjam =", jumlahpinjam, "dan lama peminjaman adalah", lamapinjam)