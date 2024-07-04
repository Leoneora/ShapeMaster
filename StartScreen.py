#Tampilan awal
from bangun_datar import *
from bangun_ruang import *
from gambar import *
import os

lanjut = True
os.system('clear')

while lanjut:
    print("============")
    print("SHAPE MASTER!")
    print("============")
    print("Halo!")
    print("Shape Master adalah alat yang dapat membantumu menghitung geometri.")
    print("Saya akan membantu menghitung luas & keliling bangun datar dan volume & luas permukaan bangun ruang.")
    Jenis_Bangun= input("Apa yang akan kita hitung kali ini? (bangun ruang / bangun datar): ").lower()
    if Jenis_Bangun == "bangun datar":
        print("""Berikut adalah daftarnya:
            1. Lingkaran
            2. Segitiga
            3. Persegi
            4. Persegi Panjang
            5. Trapesium
            6. Jajar genjang
            7. Layang-layang
            8. Belah ketupat""")
        Bangun_datar= int(input("Nomor berapa yang anda pilih? (Tulis dengan angka): "))
        if Bangun_datar == 1:
            lingkaran()
            draw_lingkaran()
        elif Bangun_datar == 2:
            segitiga()
            draw_segitiga()
        elif Bangun_datar == 3:
            persegi()
        elif Bangun_datar == 4:
            persegi_panjang()
        elif Bangun_datar == 5:
            trapesium()
        elif Bangun_datar == 6:
            jajargenjang()
        elif Bangun_datar == 7:
            layang_layang()
        else:
            belah_ketupat()

    elif Jenis_Bangun == "bangun ruang":
        print("""Berikut adalah daftarnya:
            1. Tabung
            2. Bola
            3. Kerucut
            4. Balok
            5. Kubus
            6. Limas""")
        Bangun_ruang= int(input("Nomor berapa yang anda pilih? (Tulis dengan angka): "))
        if Bangun_ruang == 1:
            tabung()
        elif Bangun_ruang == 2:
            bola()
        elif Bangun_ruang == 3:
            kerucut()
        elif Bangun_ruang == 4:
            balok()
        elif Bangun_ruang == 5:
            kubus()
        else:
            limas()
            
    jawab = input("Mau tanya lagi? (Ya/Tidak): ").lower()
    lanjut = (jawab == "ya")


print("Baiklah! Sampai jumpa!! ^^")
