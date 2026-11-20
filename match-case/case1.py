warna_lampu = input('Warna lampu lalu lintas : ')

match warna_lampu:
    case 'merah':
        print(warna_lampu, "artinya berhenti")
    case 'kuning':
        print(warna_lampu, "artinya hati-hati")
    case 'hijau':
        print(warna_lampu, "artinya boleh jalan")
    case _:
        print('Warna lampu lalu lintas tidak ditemukan')