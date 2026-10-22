lama_pinjam = int(input("Pinjam buku untuk berapa hari : "))
if lama_pinjam > 3:
    hari_terlambat = lama_pinjam -3
    print("Anda meminjam buku selama", lama_pinjam, "hari")
    print("Anda terlambat mengembalikan buku selama", hari_terlambat, "hari")
else:
    print("Anda meminjam buku selama", lama_pinjam, "hari")