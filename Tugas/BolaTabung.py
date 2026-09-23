# tugas hitung bola dan tabung

d = float(input('Input diameter lingkaran : '))
t = float(input('Input tinggi tabung : '))

r = d / 2
k = 2 * 3.14 * r
l = 3.14 * r * r
vb = 4 / 3 * 3.14 * r * r * r
vt = l * t

print(f'Jari jari lingkaran tersebut adalah {r:.2f}')
print(f'keliling lingkaran tersebut adalah {k:.2f}')
print(f'Luas lingkaran tersebut adalah {l:.2f}')
print(f'Volume bolanya adalah {vb:.2f}')
print(f'Volume tabungnya adalah {vt:.2f}')