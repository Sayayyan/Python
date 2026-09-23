# Latihan Python - XI RPL III

---

## 1. Sejarah Singkat Pemrograman Python

**Python** adalah bahasa pemrograman tingkat tinggi yang pertama kali dikembangkan oleh **Guido van Rossum** pada tahun **1989** di CWI (Centrum Wiskunde & Informatica) di Belanda. Guido memulai pengembangan Python sebagai pengganti bahasa pemrograman ABC yang pernah dia kerjakan sebelumnya.

**Inspirasi Python:**
Python terinspirasi terutama dari bahasa pemrograman **ABC** yang mengembangkan konsep tipe data dinamis, penanganan exception, dan fungsionalitas tinggi. Selain itu, Python juga terpengaruh oleh:
- **C**: Sintaks, struktur, dan fleksibilitasnya
- **Modula-3**: Konsep modul dan package
- **Smalltalk**: Konsep orientasi objek yang bersih
- **Lisp**: Konsep fungsional dan powerful metaprogramming (meski Python tidak mengikutinya secara langsung)
- **Shell scripting**: Kemudahan penggunaan dan readable syntax

Nama "Python" sendiri diambil dari acara televisi BBC **"Monty Python's Flying Circus"** yang disukai oleh Guido, bukan dari ular python seperti namanya.

- **1991**: Python versi 0.9.0 pertama kali dirilis ke publik, sudah mendukung konsep orientasi objek dan tipe data dasar.
- **1994**: Python 1.0 dirilis dengan fitur fungsional seperti lambda, map, filter, dan reduce.
- **2000**: Python 2.0 dirilis dengan fitur cycle-detecting garbage collector, list comprehensions, dan NumPy.
- **2008**: Python 3.0 dirilis (merupakan versi yang broke compatibility dengan Python 2) dengan banyak perbaikan desain.
- **2020**: Python 2 mencapai end-of-life, dan Python 3 menjadi versi standar.

Guido van Rossum menjabat sebagai "Benevolent Dictator For Life" (BDFL) hingga tahun 2018, ketika pusat pengembangan Python beralih ke model kepemilikan komunitas melalui Python Steering Council.

---

## 2. Tipe Data pada Python

### a. Integer (`int`)
Bilangan bulat tanpa desimal. Berupa bilangan positif, negatif, atau nol.
```python
usia = 17
suhu = -5
nilai = 100
```

### b. Float (`float`)
Bilangan riil/desimal yang memiliki titik desimal.
```python
phi = 3.14
berat = 55.5
suhu_celcius = 36.6
```

### c. String (`str`)
Urutan karakter yang diapit oleh tanda kutip (tunggal `'...'` atau ganda `"..."`).
```python
nama = "Sofian"
alamat = 'Jakarta Selatan'
kalimat = "Halo, selamat datang!"
```

### d. Boolean (`bool`)
Tipe data logika yang hanya memiliki dua nilai: `True` atau `False`.
```python
is_active = True
is_deleted = False
lulus = True
```

**Perbedaan:**
| Tipe Data | Deskripsi | Contoh |
|-----------|-----------|--------|
| Integer | Bilangan bulat | `42`, `-7` |
| Float | Bilangan desimal | `3.14`, `0.001` |
| String | Teks/karakter | `"hello"`, `'a'` |
| Boolean | Logika True/False | `True`, `False` |

---

## 3. Aturan Penulisan Variabel pada Python

1. **Nama variabel harus dimulai dengan huruf (a-z, A-Z) atau underscore (`_`)**, tidak boleh dimulai dengan angka.
   ```python
   nama = "Andi"      # Benar
   _private = 10      # Benar
   1data = 5          # Salah! Tidak boleh dimulai dengan angka
   ```

2. **Nama variabel hanya boleh mengandung huruf, angka, dan underscore.**
   ```python
   user_name = "Budi"    # Benar
   data_2024 = 100       # Benar
   nama-user = "Andi"    # Salah! Menggunakan tanda -
   ```

3. **Nama variabel bersifat case-sensitive (huruf besar dan kecil dianggap berbeda).**
   ```python
   Nama = "Andi"
   nama = "Budi"
   # Nama dan nama adalah variabel yang berbeda
   ```

4. **Tidak boleh menggunakan kata kunci (keyword) Python.**
   ```python
   class = "XII"    # Salah! 'class' adalah keyword Python
   for = 10         # Salah! 'for' adalah keyword Python
   ```

5. **Disarankan menggunakan nama yang deskriptif dan jelas (mnemonic).**
   ```python
   # Baik
   umur_siswa = 17
   total_nilai = 85.5
   
   # Kurang baik
   x = 17      # Tidak jelas maknanya
   tn = 85.5   # Singkatan yang tidak intuitif
   ```

6. **Boleh menggunakan huruf Unicode/ISO (untuk Python 3).**
   ```python
   nilai_φ = 3.14   # Benar
   ```

7. **Konvensi penulisan:**
   - **snake_case**: variabel dan fungsi → `nama_variabel`
   - **CamelCase**: kelas → `NamaKelas`
   - Variabel private: diawali underscore → `_private_var`

---

## 4. Operator pada Python

### a. Operator Aritmatika
Operator untuk operasi matematika dasar.

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `+` | Penjumlahan | `5 + 3` | `8` |
| `-` | Pengurangan | `10 - 4` | `6` |
| `*` | Perkalian | `3 * 4` | `12` |
| `/` | Pembagian | `10 / 3` | `3.333...` |
| `//` | Pembagian integer (floor) | `10 // 3` | `3` |
| `%` | Modulus (sisa bagi) | `10 % 3` | `1` |
| `**` | Eksponen (pangkat) | `2 ** 3` | `8` |

```python
a = 10
b = 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

### b. Operator Perbandingan
Operator untuk membandingkan dua nilai, hasilnya selalu Boolean.

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama dengan | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `3 < 5` | `True` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama | `3 <= 5` | `True` |

```python
x = 10
y = 20
print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 10)  # True
print(y <= 20)  # True
```

### c. Operator Logika
Operator untuk operasi logika (AND, OR, NOT).

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `and` | DAN | `True and True` | `True` |
| `or` | ATAU | `True or False` | `True` |
| `not` | TIDAK | `not True` | `False` |

```python
a = True
b = False
print(a and b)    # False
print(a or b)     # True
print(not a)      # False

# Contoh praktis
umur = 20
punya_ktp = True
bisa_vote = umur >= 17 and punya_ktp  # True
```

### d. Operator Penugasan (Assignment)
Operator untuk memberikan nilai ke variabel.

| Operator | Contoh | Equivalen | Keterangan |
|----------|--------|-----------|------------|
| `=` | `x = 5` | - | Memberikan nilai 5 ke x |
| `+=` | `x += 3` | `x = x + 3` | Tambah lalu assign |
| `-=` | `x -= 2` | `x = x - 2` | Kurangi lalu assign |
| `*=` | `x *= 4` | `x = x * 4` | Kalikan lalu assign |
| `/=` | `x /= 2` | `x = x / 2` | Bagi lalu assign |
| `%=` | `x %= 3` | `x = x % 3` | Modulus lalu assign |
| `**=` | `x **= 2` | `x = x ** 2` | Pangkat lalu assign |
| `//=` | `x //= 2` | `x = x // 2` | Floor divide lalu assign |

```python
x = 10
x += 5    # x = 15
x *= 2    # x = 30
x -= 10   # x = 20
x /= 4    # x = 5.0
```

### e. Operator Keanggotaan (Membership)
Operator untuk mengecek apakah suatu nilai ada dalam suatu objek (list, string, tuple, dll).

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `in` | Keanggotaan | `'a' in 'apple'` | `True` |
| `not in` | Tidak keanggotaan | `'z' not in 'apple'` | `True` |

```python
nama = "Python"
print('P' in nama)        # True
print('y' in nama)        # True
print('Z' not in nama)    # True

angka = [1, 2, 3, 4, 5]
print(3 in angka)         # True
print(10 in angka)        # False
print(10 not in angka)    # True
```

---

## 5. Perbedaan Ekspresi dan Statement

### Ekspresi (Expression)
**Ekspresi** adalah kombinasi dari nilai, variabel, operator, dan panggilan fungsi yang **dievaluasi menghasilkan sebuah nilai**.

Contoh:
```python
# Ekspresi menghasilkan nilai
2 + 3              # menghasilkan 5
x * 10             # menghasilkan nilai x dikali 10
len("hello")       # menghasilkan 5
x > 5              # menghasilkan True/False
f"{nama} Umur {umur}"  # menghasilkan string
```

### Statement (Perintah)
**Statement** adalah instruksi lengkap yang melakukan suatu tindakan. Statement **bisa berisi ekspresi**, tapi statement sendiri adalah perintah yang dieksekusi.

Contoh:
```python
# Statement (perintah)
x = 5                    # Assignment statement
if x > 3:                # Conditional statement
    print("Besar")       # Fungsi call statement
for i in range(10):      # Loop statement
    print(i)             # Fungsi call statement
def tambah(a, b):        # Function definition statement
    return a + b
```

### Perbedaan Utama:

| Aspek | Ekspresi | Statement |
|-------|----------|-----------|
| **Hasil** | Mengevaluasi ke sebuah nilai | Melakukan tindakan/eksekusi |
| **Contoh** | `2 + 3`, `x > 5`, `len("abc")` | `x = 5`, `if`, `for`, `def`, `print()` |
| **Bisa berdiri sendiri?** | Tidak, harus ada konteks | Ya, sebagai perintah lengkap |
| **Dalam if/while** | Ekspresi digunakan sebagai kondisi | Statement adalah blok perintah |

### Contoh Perbedaan dalam Kode:
```python
# x = 10  ini adalah STATEMENT (assignment statement)
# 10 adalah EKSPRESI (literal expression)

# if x > 5:  --> 'x > 5' adalah EKSPRESI (kondisi)
#     print(x)  --> ini STATEMENT (fungsi call statement)

# Ekspresi bisa ada di dalam statement:
y = (2 + 3) * 4    # (2 + 3) * 4 adalah ekspresi, y = ... adalah statement
```

---

## 6. Struktur Kontrol Percabangan

### a. `if` (Kondisi Sederhana)
Digunakan untuk menjalankan blok kode **hanya jika kondisi benar**.

```python
umur = 17

if umur >= 17:
    print("Anda sudah dewasa")
```

### b. `if-else` (Kondisi dengan Alternatif)
Digunakan ketika ada **dua kemungkinan**: kondisi benar atau salah.

```python
nilai = 85

if nilai >= 80:
    print("Predikat: A (Sangat Baik)")
else:
    print("Predikat: B (Baik)")
```

### c. `if-elif-else` (Banyak Kondisi)
Digunakan ketika ada **lebih dari dua kemungkinan**.

```python
nilai = 75

if nilai >= 90:
    print("Predikat: A")
elif nilai >= 80:
    print("Predikat: B")
elif nilai >= 70:
    print("Predikat: C")
elif nilai >= 60:
    print("Predikat: D")
else:
    print("Predikat: E")
```

### d. `match-case` (Python 3.10+)
Digunakan untuk **pencocokan pola** (pattern matching), mirip seperti switch-case di bahasa lain, tapi lebih powerful.

```python
# Contoh 1: Match dengan literal
hari = "Senin"

match hari:
    case "Senin":
        print("Hari kerja pertama")
    case "Selasa":
        print("Hari kerja kedua")
    case "Sabtu" | "Minggu":    # Bisa multiple case dengan |
        print("Weekend!")
    case _:
        print("Hari tidak dikenal")

# Contoh 2: Match dengan struktur data
data = {"nama": "Budi", "umur": 20}

match data:
    case {"nama": nama, "umur": umur}:
        print(f"Nama: {nama}, Umur: {umur}")
    case {"nama": nama}:
        print(f"Hanya nama: {nama}")
    case _:
        print("Format tidak sesuai")
```

### Perbedaan `if-elif` dan `match-case`:
- `if-elif-else`: Lebih fleksibel, bisa mengecek kondisi kompleks (range, operasi logika).
- `match-case`: Lebih bersih untuk pencocokan langsung dengan nilai tertentu, bisa menangani struktur data (pattern matching).

---

## 7. Struktur Kontrol Perulangan

### a. `for` Loop
`for` digunakan ketika **jumlah iterasi diketahui** atau untuk mengiterasi melalui **kumpulan data (sequence)**.

```python
# Contoh 1: Iterasi melalui list
mahasiswa = ["Andi", "Budi", "Citra"]

for nama in mahasiswa:
    print(f"Halo, {nama}!")

# Contoh 2: Menggunakan range()
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(2, 11, 2):  # 2, 4, 6, 8, 10 (awal, akhir, langkah)
    print(i)
```

### b. `while` Loop
`while` digunakan ketika **jumlah iterasi tidak diketahui di awal**, dan perulangan berlanjut selama kondisi benar.

```python
# Contoh 1: Menghitung mundur
count = 5

while count > 0:
    print(count)
    count -= 1

print("Selamat Jumat!")

# Contoh 2: Input sampai kondisi terpenuhi
password = ""

while password != "rahasia":
    password = input("Masukkan password: ")
    if password != "rahasia":
        print("Password salah, coba lagi!")

print("Login berhasil!")
```

### Perbedaan `for` dan `while`:

| Aspek | `for` | `while` |
|-------|-------|---------|
| **Jumlah iterasi** | Diketahui / terbatas | Tidak diketahui / bisa tak terhingga |
| **Kapan berhenti** | Sequence habis / range selesai | Kondisi loop menjadi False |
| **Penggunaan umum** | Iterasi data, fixed iterations | Menunggu kondisi tertentu, sentinel loop |
| **Risiko** | Loop pasti berhenti | Bisa infinite loop jika kondisi tidak pernah False |

### Contoh Perbandingan:

```python
# for: tahu harus mengulang 5 kali
for i in range(5):
    print(i)

# while: tahu harus melanjutkan sampai total mencapai 100
total = 0
angka = 0

while total < 100:
    angka += 1
    total += angka

print(f"Total: {total}, Jumlah angka: {angka}")
```

---

## 8. Struktur Data pada Python

### a. List (`list`)
**List** adalah kumpulan item yang **terurut**, **bisa diubah (mutable)**, dan **bisa berisi duplikat**.

```python
# Membuat list
buah = ["apel", "mangga", "jeruk"]

# Accessing
print(buah[0])    # "apel"
print(buah[-1])   # "jeruk"

# Mutable - bisa diubah
buah[1] = "pepaya"
print(buah)       # ["apel", "pepaya", "jeruk"]

# Bisa duplikat
angka = [1, 2, 2, 3, 3, 3]
print(angka)      # [1, 2, 2, 3, 3, 3]

# Operasi list
buah.append("pisang")       # tambah di akhir
buah.insert(1, "durian")    # insert di posisi 1
buah.remove("apel")         # hapus item
hasil = len(buah)           # panjang list
```

### b. Tuple (`tuple`)
**Tuple** adalah kumpulan item yang **terurut**, **tidak bisa diubah (immutable)**, dan **bisa berisi duplikat**.

```python
# Membuat tuple
warna = ("merah", "hijau", "biru")

# Accessing
print(warna[0])    # "merah"

# Immutable - TIDAK bisa diubah
# warna[1] = "kuning"  --> ERROR!

# Bisa duplikat
koordinat = (10, 20, 10)

# Tuple packing & unpacking
point = (3, 4)
x, y = point        # Unpacking
print(x)            # 3
print(y)            # 4
```

### Perbedaan List vs Tuple:

| Fitur | List | Tuple |
|-------|------|-------|
| Mutable | Ya (bisa diubah) | Tidak (immutable) |
| Syntax | `[]` kurung siku | `()` kurung kurawal |
| Kecepatan | Lebih lambat | Lebih cepat |
| Penggunaan | Data yang sering berubah | Data yang tetap (konstanta) |
| Method | Banyak method | Sedikit method |

### c. Dictionary (`dict`)
**Dictionary** adalah kumpulan item dalam bentuk **pasangan key-value**, **tidak terurut** (sejak Python 3.7 terurut berdasarkan insertion), **mutable**, dan **key harus unik**.

```python
# Membuat dictionary
mahasiswa = {
    "nama": "Andi",
    "nim": "12345",
    "jurusan": "RPL"
}

# Accessing dengan key
print(mahasiswa["nama"])        # "Andi"
print(mahasiswa.get("nim"))     # "12345"
print(mahasiswa.get("email", "Tidak ada"))  # default value

# Mutable - bisa diubah/tambah
mahasiswa["email"] = "andi@mail.com"
mahasiswa["nama"] = "Budi"

# Menghapus
del mahasiswa["jurusan"]

# Operasi dictionary
keys = mahasiswa.keys()        # semua key
values = mahasiswa.values()    # semua value
items = mahasiswa.items()      # semua pasangan (key, value)
jumlah = len(mahasiswa)        # jumlah pasangan
```

### d. Set (`set`)
**Set** adalah kumpulan item yang **tidak terurut**, **tidak memungkinkan duplikat**, dan **mutable**.

```python
# Membuat set
huruf = {"a", "b", "c"}

# Set otomatis menghilangkan duplikat
angka = {1, 2, 2, 3, 3, 3}
print(angka)    # {1, 2, 3}

# Immutable elements only (set tidak bisa berisi list/dict)
# s = {1, [2, 3]}   --> ERROR!

# Operasi set
huruf.add("d")          # tambah item
huruf.remove("a")       # hapus item

# Operasi matematika set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union: {1, 2, 3, 4, 5, 6}
print(a & b)   # Intersection: {3, 4}
print(a - b)   # Difference: {1, 2}
print(a ^ b)   # Symmetric difference: {1, 2, 5, 6}
```

### Perbandingan Keempat Struktur Data:

| Struktur | Terurut | Mutable | Duplikat | Akses | Penggunaan |
|----------|---------|---------|----------|-------|------------|
| **List** | Ya | Ya | Diizinkan | Index | Koleksi data umum |
| **Tuple** | Ya | Tidak | Diizinkan | Index | Data tetap/konstanta |
| **Dict** | Ya* | Ya | Key unik | Key | Data berpasangan key-value |
| **Set** | Tidak | Ya | Tidak | Tidak ada | Elemen unik, operasi himpunan |

---
