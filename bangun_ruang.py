#File "bangun_ruang" untuk kumpulan def() atau fungsi perhitungan bangun ruang yang akan dipanggil. dibuat oleh E. Keisha P.
import math

#Bangun ruang:

def tabung():
    jariJari= int(input("Berapa jari-jari alas/tutup tabung?: "))
    tinggi= int(input("Berapa tinggi tabung?: "))
    phi= 22/7
    volume= phi*(jariJari*jariJari)*tinggi
    luasPermukaan= 2*phi*jariJari*(jariJari+tinggi)
    volume= round(volume,2)
    luasPermukaan= round(luasPermukaan,2)
    print(f"Volume tabung= {volume}")
    print(f"Luas Permukaan tabung= {luasPermukaan}")

def bola():
    jariJari= int(input("Berapa jari-jari bola?: "))
    phi= 22/7
    volume= 4/3*phi*jariJari*jariJari*jariJari
    luasPermukaan= 4*phi*jariJari*jariJari
    print(f"Volume bola= {volume}")
    print(f"Luas Permukaan bola= {luasPermukaan}")
    
def kerucut():
    jariJari= int(input("Berapa jari-jari alas kerucut?: "))
    tinggi= int(input("Berapa tinggi kerucut?: "))
    garisPelukis= int(input("Berapa garis pelukis kerucut?: "))
    phi= 22/7
    volume= 1/3*phi*jariJari*jariJari*tinggi
    luasPermukaan= phi*jariJari*(jariJari+garisPelukis)
    print(f"Volume kerucut= {volume}")
    print(f"Luas Permukaan kerucut= {luasPermukaan}")

def balok():
    panjang= int(input("Berapa panjang balok?: "))
    lebar= int(input("Berapa lebar balok?: "))
    tinggi= int(input("Berapa tinggi balok?: "))
    volume= panjang*lebar*tinggi
    luasPermukaan= 2*(panjang*lebar + lebar*tinggi + tinggi*panjang)
    print(f"Volume balok= {volume}")
    print(f"Luas Permukaan balok= {luasPermukaan}")

def kubus():
    sisi= int(input("Berapa sisi kubus?: "))
    volume= sisi**3
    luasPermukaan= 6 * sisi**2
    print(f"Volume kubus= {volume}")
    print(f"Luas Permukaan kubus= {luasPermukaan}")

def limas():
    jenis = input("Apakah jenis limasnya? (segitiga/segiempat): ").lower()
    if jenis == "segitiga":
        # Input untuk limas segitiga
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggiAlas = float(input("Masukkan tinggi alas segitiga: "))
        tinggiLimas = float(input("Masukkan tinggi limas: "))
        
        # Menghitung luas alas dan volume
        luasAlas = 0.5 * alas * tinggiAlas
        volume = (1/3) * luasAlas * tinggiLimas
        
        # Menghitung luas permukaan
        sisiMiring = math.sqrt((alas / 2)**2 + tinggiLimas**2)
        luasPermukaan = luasAlas + 3 * (0.5 * alas * sisiMiring)
        
    elif jenis == "segiempat":
        # Input untuk limas segiempat
        sisiAlas = float(input("Masukkan panjang sisi alas persegi: "))
        tinggiLimas = float(input("Masukkan tinggi limas: "))
        
        # Menghitung luas alas dan volume
        luasAlas = sisiAlas ** 2
        volume = (1/3) * luasAlas * tinggiLimas
        
        # Menghitung luas permukaan
        sisiMiring = math.sqrt((sisiAlas / 2)**2 + tinggiLimas**2)
        luasPermukaan = luasAlas + 4 * (0.5 * sisiAlas * sisiMiring)
    
    else:
        print("Jenis limas tidak valid. Masukkan 'segitiga' atau 'segiempat'.")
        return
    
    print(f"Luas permukaan limas {jenis}: {luasPermukaan}")
    print(f"Volume limas {jenis}: {volume}")