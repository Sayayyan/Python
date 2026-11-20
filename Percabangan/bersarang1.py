print('Contoh program Nested If')
print('Masukkan data anda dengan benar')
nama = str(input('Nama : '))
print('Jenis kelamin')
print('1. Laki-laki')
print('2. Perempuan')
jenis = int(input('Masukkan kode jenis kelamin (1-2) : '))
if(jenis == 1):
    tinggi = int(input('Tinggi Badan : '))
    if(tinggi >= 165):
        print('\n-----Anda Lulus-----')
    else:
        print('Maaf, tinggi badan anda belum memenui syarat')
elif(jenis == 2):
    tinggi = int(input('Tinggi Badan : '))
    if(tinggi >= 160):
        print('\n-----Anda Lulus-----')
    else:
        print('Maaf, tinggi badan anda belum memenui syarat')
else:
    print('Silahkan masukkan kode jenis kelamin dengan benar')