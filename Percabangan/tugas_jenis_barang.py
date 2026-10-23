jenis = input("Pilih jenis barang yang ingin dibeli (Meja, Pulpen, Penghapus, Pensil) : ").lower()
harga = int(input("Masukkan harga dari barang yang anda pilih : "))
jumlah = int(input("Masukkan berapa jumlah barang yang anda beli : "))
totalbelanja = harga * jumlah
print("Barang yang anda beli adalah", jenis, "dengan harga", harga, "dan jumlah", jumlah, )
if totalbelanja > 70000:
    diskon = totalbelanja * 0.4
    persen = "40%"
elif totalbelanja > 50000:
    diskon = totalbelanja * 0.3
    persen = "30%"
elif totalbelanja > 30000:
    diskon = totalbelanja * 0.2
    persen = "20%"
else:
    diskon = 0

totalbayar = totalbelanja - diskon
print("Total belanja anda adalah Rp", totalbelanja, " diskon yang anda dapatkan sebesar", persen, " dengan nominal Rp", diskon, ", maka total yang harus anda bayar adalah", totalbayar)