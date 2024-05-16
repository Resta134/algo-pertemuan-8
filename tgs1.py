data = []

def tambah_data_barang():
    nama = str(input('Masukan Nama Barang : '))
    stok = int(input('Masukan Stok Barang : '))
    data_new = {'nama_barang' : nama, 'stok_barang' : stok}
    data.append(data_new)

def hapus_data_barang():
    hapus = int(input('Hapus data index ke : '))
    data.pop(hapus)

def tampilkan_data():
    for i in data:
    print('-',i['nama'], ['stok'])