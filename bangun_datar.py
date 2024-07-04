#File "bangun_datar" untuk kumpulan def() atau fungsi perhitungan bangun datar yang akan dipanggil. dibuat oleh E. Keisha P.
import math

#Bangun datar:

def lingkaran(): #Perhitungan Luas dan Keliling Lingkaran
    r= int(input("Berapa jari-jari lingkaran?:"))
    if r % 7 == 0:
        phi = 22 / 7
    else:
        phi = 3.14
    luas = phi * (r ** 2)
    keliling = 2*phi*r
    print(f"Keliling lingkaran= {keliling}")
    print(f"Luas lingkaran= {luas}")

def segitiga():
    alas= int(input("berapa alas/sisi segitiga?: "))
    tinggi= int(input("berapa tinggi segitiga?: "))
    keliling= alas+alas+alas
    luas= 1/2 * alas * tinggi
    print(f"Keliling segitiga= {keliling}")
    print(f"Luas segitiga= {luas}")

def persegi():
    sisi= int(input("berapa sisi persegi?: "))
    keliling= 4*sisi
    luas= sisi*sisi
    print(f"Keliling persegi= {keliling}")
    print(f"Luas persegi= {luas}")

def persegi_panjang():
    panjang= int(input("Berapa panjang persegi panjang?: "))
    lebar= int(input("Berapa lebar persegi panjang?: "))
    keliling= 2*(panjang+lebar)
    luas= panjang*lebar
    print(f"Keliling persegi panjang= {keliling}")
    print(f"Luas persegi panajng= {luas}")

def trapesium():
    jenis= input("Jenis trapesium apa yang akan di hitung? (trapesium sama kaki / trapesium segitiga siku-siku): ")
    if jenis == "trapesium sama kaki":
        a= int(input("Berapa sisi atas?: "))
        b= int(input("Berapa sisi bawah?:"))
        c= int(input("berapa sisi kanan?: "))
        d= int(input("Berapa sisi kiri?: "))
        keliling= a+b+c+d
        luas= 1/2 * (a+b) * t
    else:
        t= int(input("Berapa tinggi trapesium?: "))
        a= int(input("Berapa sisi atas?: "))
        b= int(input("Berapa sisi bawah?: "))
        c= int(input("berapa sisi yang terakhir?: "))
        keliling= a+b+c+t
        luas= 1/2 * (a+b) * t
    print(f"Keliling trapesium= {keliling}")
    print(f"Luas trapesium= {luas}")

def jajargenjang():
    a= int(input("Berapa panjang sisi alas?: "))
    b= int(input("Berapa panjang sisi lainnya?: "))
    t= int(input("Berapa tinggi trapesium?: "))
    luas= a*t
    keliling= 2*(a+b)
    print(f"Keliling jajargenjang= {keliling}")
    print(f"Luas jajargenjang= {luas}")

def layang_layang():
    d1= int(input("Berapa diagonal 1?: "))
    d2= int(input("Berapa diagonal 2?: "))
    a= int(input("Berapa panjang sisi pertama?: "))
    b= int(input("Berapa panjang sisi kedua?: "))
    keliling= 2*(a+b)
    luas= 1/2*d1*d2
    print(f"Keliling layang-layang= {keliling}")
    print(f"Luas layang-layang= {luas}")

def belah_ketupat():
    d1= int(input("Berapa diagonal 1?: "))
    d2= int(input("Berapa diagonal 2?: "))
    s= int(input("Berapa panjang sisinya?: "))
    keliling= 4*s
    luas= 1/2*d1*d2
    print(f"Keliling belah ketupat= {keliling}")
    print(f"Luas belah ketupat= {luas}")