#Tampilan awal
from bangun_datar import *
from bangun_ruang import *
from gambar import *
import os

lanjut = True
while lanjut:
    os.system('clear')
    print("============")
    print("SHAPE MASTER!")
    print("============")
    print("Halo!")
    print("Shape Master adalah alat yang dapat membantumu menghitung geometri.")
    print("Saya akan membantu menghitung luas & keliling bangun datar dan volume & luas permukaan bangun ruang.")
    print("")
    jenisBangun= input("Apa yang akan kita hitung kali ini? (bangun ruang / bangun datar / quit): ").lower()
    print("")
    if jenisBangun == "quit" or jenisBangun == "q":
        lanjut= False
        break

    elif jenisBangun == "bangun datar":
        print("""Berikut adalah daftarnya:
            1. Lingkaran
            2. Segitiga
            3. Persegi
            4. Persegi Panjang
            5. Trapesium
            6. Jajar genjang
            7. Layang-layang
            8. Belah ketupat
            -------------------------------
            9. Kembali ke menu sebelumnya
            -------------------------------""")
        bangunDatar= int(input("Nomor berapa yang anda pilih? (Tulis dengan angka): "))
        if bangunDatar == 1:
            lingkaran()
            draw_lingkaran()
        elif bangunDatar == 2:
            segitiga()
            draw_segitiga()
        elif bangunDatar == 3:
            persegi()
            draw_persegi()
        elif bangunDatar == 4:
            persegi_panjang()
            draw_PersegiPanjang()
        elif bangunDatar == 5:
            trapesium()
        elif bangunDatar == 6:
            jajargenjang()
            draw_jajargenjang
        elif bangunDatar == 7:
            layang_layang()
        elif bangunDatar == 8:
            belah_ketupat()
        else:
            continue
    elif jenisBangun == "bangun ruang":
        print("""Berikut adalah daftarnya:
            1. Tabung
            2. Bola
            3. Kerucut
            4. Balok
            5. Kubus
            6. Limas
            -------------------------------
            7. Kembali ke menu sebelumnya
            -------------------------------""")
        bangunRuang= int(input("Nomor berapa yang anda pilih? (Tulis dengan angka): "))
        if bangunRuang == 1:
            tabung()
        elif bangunRuang == 2:
            bola()
        elif bangunRuang == 3:
            kerucut()
        elif bangunRuang == 4:
            balok()
        elif bangunRuang == 5:
            kubus()
        elif bangunRuang == 6:
            limas()
        else:
            continue
    else:
        print("!!!!!!!!!!!!")
        print("Pilih lagi!")
        print("!!!!!!!!!!!!")
    
    print("")
    jawab = input("Mau tanya lagi? (Ya/Tidak): ").lower()
    lanjut = (jawab == "ya")


print("")
print("Baiklah! Sampai jumpa!! ^^")
print("")
