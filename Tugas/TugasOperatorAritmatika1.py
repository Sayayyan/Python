# Operator aritmatika menghitung total belanja toko
h = 15000
jb = 5
dp = 8

tk = h * jb
pd = tk * (dp / 100)
tb = tk - pd

print("=== TOTAL PEMBAYARAN TOKO ===")
print("Harga Total          : Rp", tk)
print("Diskon               : Rp", int(pd))
print("Total Harus Dibayar  : Rp", int(tb))
