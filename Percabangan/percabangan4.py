tiket = input("Pilih Jenis tiket V = velvet, G = Gold, D = 4DX atau R = Reguler? ").lower()
jumlah = int(input("Berapa jumlah tiket yang dibeli? "))

if tiket == "v":
    harga = 15000
    jenis = "Velvet"
elif tiket == "g":
    harga = 10000
    jenis = "Gold"
elif tiket == "d":
    harga = 7500
    jenis = "4DX"
elif tiket == "r":
    jenis = "Reguler"
else:
    harga = 0
    jenis = "Yang tidak tersedia"

total = harga * jumlah
print("Anda membeli tiket", jenis, "dengan harga Rp", harga, ", Jumlah tiket =", jumlah, ", Total bayar Rp.", total)