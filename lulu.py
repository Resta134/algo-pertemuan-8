print ("Kelompok 4")
print ("Isi data diri")
print ("Pilih fasilitas yang harus di kembangkan :")
print ("1. Kebersihan kendaraan")
print ("2. Keramahan pengemudi")
print ("3. Ketepatan waktu")
print ("4. Pengembangan fasilitas aplikasi")
print ("5. Cara mengemudi pengendara")
print ("6. Keluar")

#meminta input dari pengguna
pilihan = input('Masukan pilihan Anda : ')

#memproses Pilihan pengguna
if pilihan == "1":
    print("Anda memilih pilihan satu fasilitas penggunaan grab untuk bahan evaluasi kebersihan kendaran")

    nama_responden = str(input("Nama Responden : "))
    rating = int(input("Rating : "))
    ulasan = str(input("Ulasan : "))
    print("Kebersihan kendaraan :", nama_responden, rating, ulasan)

elif pilihan == "2":
    print ("Sikap dari pengemudi")
    nama_responden = str(input("Nama Responden : "))
    rating = int(input("Rating : "))
    ulasan = str(input("Ulasan : "))
    print ("Keramahan pengemudi : ", nama_responden, rating, ulasan)

elif pilihan == "3":
    print("Ketepatan waktu pengemudi dalam menjemput konsumen")

    nama_responden = str(input("Nama Responden : "))
    kehadiran_tepat_waktu = int(input("Kehadiran tepat waktu : "))
    ulasan = str(input("Ulasan : "))
    print ("ketepatan waktu : ", nama_responden, kehadiran_tepat_waktu, ulasan)

elif pilihan == "4" :
    print ("Pengembangan aplikasi dengan meningkatkan layanan fasilitas")

    nama_responden = str(input("Nama Responden : "))
    rating = int(input("Rating : "))
    ulasan = str(input("Ulasan : "))
    print ("Pengembangan fasilitas aplikasi : ", nama_responden, rating, ulasan)

elif pilihan == "5" :
    print("Melihat bagaimana pengemudi berkendara di jalan")
    nama_responden = str(input("Nama Responden : "))
    rating  = int(input("Rating : "))
    ulasan = str(input("Ulasan : "))
    print("Cara mengemudi pengendara : ", nama_responden, rating, ulasan)

else : 
    pilihan == 6
    print ("Terimakasih")