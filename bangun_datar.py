#File "bangun_datar" untuk kumpulan def() atau fungsi perhitungan bangun datar yang akan dipanggil. dibuat oleh E. Keisha P.
import math
from gambar import *

#Bangun datar:

#Perhitungan Luas dan Keliling Lingkaran
def lingkaran(): 
    r= int(input("Berapa jari-jari lingkaran?:"))
    if r % 7 == 0:  #Jika jari-jari merupakan perkalian 7
        phi = 22 / 7
    else:           #Jika jari-jari bukan merupakan perkalian 7
        phi = 3.14
    luas = phi * (r ** 2)
    keliling = 2 * phi * r
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling lingkaran= {keliling}")
    print(f"Luas lingkaran= {luas}")
    print("")

#Perhitungan Luas dan Keliling Segitiga
def segitiga(): 
    alas= int(input("berapa alas/sisi segitiga?: "))
    tinggi= int(input("berapa tinggi segitiga?: "))
    keliling= alas + alas + alas
    luas= 1/2 * alas * tinggi
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling segitiga= {keliling}")
    print(f"Luas segitiga= {luas}")
    print("")

#Perhitungan Luas dan Keliling Persegi
def persegi(): 
    sisi= int(input("berapa sisi persegi?: "))
    keliling= 4 * sisi
    luas= sisi * sisi
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling persegi= {keliling}")
    print(f"Luas persegi= {luas}")
    print("")

#Perhitungan Luas dan Keliling Persegi Panjang
def persegi_panjang(): 
    panjang= int(input("Berapa panjang persegi panjang?: "))
    lebar= int(input("Berapa lebar persegi panjang?: "))
    keliling= 2 * (panjang + lebar)
    luas= panjang * lebar
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling persegi panjang= {keliling}")
    print(f"Luas persegi panajng= {luas}")
    print("")

#Perhitungan Luas dan Keliling Trapesium
def trapesium(): 
    tinggi= int(input("Berapa tinggi/sisi kiri trapesium?: "))
    atas= int(input("Berapa sisi atas?: "))
    bawah= int(input("Berapa sisi bawah?: "))
    kanan= int(input("berapa sisi kanan?: "))
    keliling= atas + bawah + kanan + tinggi
    luas= 1/2 * (atas + bawah) * tinggi
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling trapesium= {keliling}")
    print(f"Luas trapesium= {luas}")
    print("")
    draw_trapesium_sama_kaki()

#Perhitungan Luas dan Keliling Jajargenjang
def jajargenjang(): 
    alas= int(input("Berapa panjang sisi alas?: "))
    sisiMiring= int(input("Berapa panjang sisi miring?: "))
    tinggi= int(input("Berapa tinggi jajargenjang?: "))
    luas= alas * tinggi
    keliling= 2 * (alas + sisiMiring)
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling jajargenjang= {keliling}")
    print(f"Luas jajargenjang= {luas}")
    print("")

#Perhitungan Luas dan Keliling Layang-layang
def layang_layang(): 
    diag1= int(input("Berapa diagonal 1?: "))
    diag2= int(input("Berapa diagonal 2?: "))
    sisi1= int(input("Berapa panjang sisi pertama?: "))
    sisi2= int(input("Berapa panjang sisi kedua?: "))
    keliling= 2 * (sisi1 + sisi2)
    luas= 1/2 * diag1 * diag2
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling layang-layang= {keliling}")
    print(f"Luas layang-layang= {luas}")
    print("")

#Perhitungan Luas dan Keliling Belah Ketupat
def belah_ketupat(): 
    diag1= int(input("Berapa diagonal 1?: "))
    diag2= int(input("Berapa diagonal 2?: "))
    sisi= int(input("Berapa panjang sisinya?: "))
    keliling= 4 * sisi
    luas= 1/2 * diag1 * diag2
    luas= round(luas,2)
    keliling= round(keliling,2)
    print("")
    print(f"Keliling belah ketupat= {keliling}")
    print(f"Luas belah ketupat= {luas}")
    print("")