hari = int(input('Masukkan angka hari : '))

match hari:
    case 1:
        print('Hari ke-', hari, 'adalah hari senin')
    case 2:
            print('Hari ke-', hari, 'adalah hari selasa')
    case 3:
            print('Hari ke-', hari, 'adalah hari rabu')
    case 4:
            print('Hari ke-', hari, 'adalah hari kamis')
    case 5:
            print('Hari ke-', hari, 'adalah hari jumat')
    case 6:
            print('Hari ke-', hari, 'adalah hari sabtu')
    case 7:
            print('Hari ke-', hari, 'adalah hari minggu')
    case _:
            print('Hari ke-', hari, 'tidak ditemukan')