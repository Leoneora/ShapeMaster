#File "bangun_ruang" untuk kumpulan def() atau fungsi perhitungan bangun ruang yang akan dipanggil. dibuat oleh E. Keisha P.
import math

#Bangun ruang:

def tabung():
    r= int(input("Berapa jari-jari alas/tutup tabung?: "))
    t= int(input("Berapa tinggi tabung?: "))
    phi= 22/7
    Volume= phi*r*r*t
    A= 2*phi*r(r+t)
    print(f"Volume tabung= {Volume}")
    print(f"Luas Permukaan tabung= {A}")

def bola():
    r= int(input("Berapa jari-jari bola?: "))
    phi= 22/7
    Volume= 4/3*phi*r*r*r
    A= 4*phi*r*r
    print(f"Volume bola= {Volume}")
    print(f"Luas Permukaan bola= {A}")
    
def kerucut():
    r= int(input("Berapa jari-jari alas kerucut?: "))
    t= int(input("Berapa tinggi kerucut?: "))
    s= int(input("Berapa garis pelukis kerucut?: "))
    phi= 22/7
    Volume= 1/3*phi*r*r*t
    A= phi*r*(r+s)
    print(f"Volume kerucut= {Volume}")
    print(f"Luas Permukaan kerucut= {A}")

def balok():
    p= int(input("Berapa panjang balok?: "))
    l= int(input("Berapa lebar balok?: "))
    t= int(input("Berapa tinggi balok?: "))
    Volume= p*l*t
    A= 2*(p*l+l*t+t*p)
    print(f"Volume balok= {Volume}")
    print(f"Luas Permukaan balok= {A}")

def kubus():
    s= int(input("Berapa sisi kubus?: "))
    Volume= s*s*s
    A= 6*s*s
    print(f"Volume kubus= {Volume}")
    print(f"Luas Permukaan kubus= {A}")

def limas():
    jenis = input("Apakah jenis limasnya? (segitiga/segiempat): ").lower()
    if jenis == "segitiga":
        # Input untuk limas segitiga
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi_alas = float(input("Masukkan tinggi alas segitiga: "))
        tinggi_limas = float(input("Masukkan tinggi limas: "))
        
        # Menghitung luas alas dan volume
        luas_alas = 0.5 * alas * tinggi_alas
        volume = (1/3) * luas_alas * tinggi_limas
        
        # Menghitung luas permukaan
        sisi_miring = math.sqrt((alas / 2)**2 + tinggi_limas**2)
        luas_permukaan = luas_alas + 3 * (0.5 * alas * sisi_miring)
        
    elif jenis == "segiempat":
        # Input untuk limas segiempat
        sisi_alas = float(input("Masukkan panjang sisi alas persegi: "))
        tinggi_limas = float(input("Masukkan tinggi limas: "))
        
        # Menghitung luas alas dan volume
        luas_alas = sisi_alas ** 2
        volume = (1/3) * luas_alas * tinggi_limas
        
        # Menghitung luas permukaan
        sisi_miring = math.sqrt((sisi_alas / 2)**2 + tinggi_limas**2)
        luas_permukaan = luas_alas + 4 * (0.5 * sisi_alas * sisi_miring)
    
    else:
        print("Jenis limas tidak valid. Masukkan 'segitiga' atau 'segiempat'.")
        return
    
    print(f"Luas permukaan limas {jenis}: {luas_permukaan}")
    print(f"Volume limas {jenis}: {volume}")