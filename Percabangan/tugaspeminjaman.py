jumlahpinjam = int(input("Inputkan jumlah buku yang dipinjam = "))
lamapinjam = int(input("Inputkan lama peminjaman = "))

if lamapinjam > 7:
    denda = 2000 * (lamapinjam - 7) * jumlahpinjam
    print("Lama peminjaman", lamapinjam, "hari, Jumlah hari terlambat", lamapinjam - 7, "hari dan besarnya denda adalah", denda)
else:
    print("Jumlah buku yang dipinjam =", jumlahpinjam, "dan lama peminjaman adalah", lamapinjam)