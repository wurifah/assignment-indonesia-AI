# no 1
print("    --Program input data--   ")
print("  ")
nama         = input("Masukkan nama Anda                 = ")
umur     = int(input("Masukkan umur Anda                 = "))
tinggi = float(input("Masukkan tinggi badan Anda dalam cm= "))
print("  ")
print("Nama saya {}, umur saya {} tahun dan tinggi {} cm".format(nama,umur,tinggi))


# no 2
print("  ")
print("  ")
print("    ============================     ")
print("              ")
print("    --Program menghitung luas lingkaran--   ")
print("      ")
jari = int(input("Masukkan nilai jari-jari dalam cm = "))
phi = 22/7;
luas = phi*jari*jari
print("Luas lingkaran dengan jari-jari sebesar {} adalah {:.2f} cm\u00b2".format(jari,luas))

# no 3 
print("              ")
print("    ============================     ")
print("              ")
print("    --Program menentukan keulusan siswa--   ")
teori   = float(input("Masukkan nilai ujian teori   = "))
praktik = float(input("Masukkan nilai ujian praktik = "))
kkm = 70;
if teori >kkm and praktik > kkm:
    print("Selamat, Anda lulus")
elif teori >kkm and praktik <= kkm:
    print("Anda harus mengulang ujian praktik")
elif teori <= kkm and praktik > kkm:
    print("Anda harus mengulang ujian teori")
else :
    print("Anda harus mengulang ujian teori dan praktek")
