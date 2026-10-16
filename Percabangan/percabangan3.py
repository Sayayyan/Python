#Menginput Nilai Tugas, UTS, dan UAS
tugas = float(input('Masukkan nilai Tugas : '))
uts = float(input('Masukkan nilai UTS : '))
uas = float(input('Masukkan nilai UAS : '))

#Menghitung Nilai Akhir sesuai dengan Bobot
nilai = (0.15 * tugas) + (0.35 * uts) + (0.5 * uas)

#Menentukan Grade Berdasarkan Nilai Akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'

#Menentukan Status Kelulusan Berdasarkan Nilai AKhir
if nilai > 60:
    status = "Lulus"
else:
    status = "Tidak lulus"

#Menampilkan Nilai AKhir, Grade, dan Status kelulusan
print('Nilai AKhir : ', nilai)
print('Grade : ', grade)
print('Status : ', status)

#BUAT FLOWCHARTNYA