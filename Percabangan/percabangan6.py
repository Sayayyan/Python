belanja = int(input("Masukkan total belanja anda : "))

if belanja > 30000:
    print("Anda mendapatkan diskon 20%")
    diskon = 0.2 * belanja
else:
    print("Anda tidak mendapatkan diskon")
    diskon = 0

print("Diskon anda sebesar", diskon)
total_bayar = belanja - diskon
print("Anda harus membayar sebesar", total_bayar)