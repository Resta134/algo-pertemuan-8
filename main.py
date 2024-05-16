import tgs1

print('Selamat datang di program Manajemen Stok Barang!')
print('Pilihan : ')
print('1. Tambah Data Barang')
print('2. Hapus Data Barang')
print('3. Tampilkan Data Barang')
print('4. Keluar')

while True:
    pilihan = int(input('Masukan Pilihan : '))
    print('=================')
    if pilihan == 1 :
        tgs1.tambah_data_barang()
    elif pilihan == 2 :
        tgs1.hapus_data_barang()
    elif pilihan == 3 :
        tgs1.tampilkan_data()
    else:
        pilihan == 4 
        print('Terimakasih')