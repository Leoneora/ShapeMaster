#File "bangun_ruang" untuk kumpulan def() atau fungsi perhitungan bangun ruang yang akan dipanggil. dibuat oleh E. Keisha P.
import math

#Bangun ruang:

def tabung():
    jariJari= int(input("Berapa jari-jari alas/tutup tabung?: "))
    tinggi= int(input("Berapa tinggi tabung?: "))
    phi= 22/7
    volume= phi * (jariJari * jariJari) * tinggi
    luasPermukaan= 2 * phi * jariJari * (jariJari + tinggi)
    volume= round(volume,2)
    luasPermukaan= round(luasPermukaan,2)
    print("")
    print("------------------------------------------------------")
    print(f"Volume tabung= {volume}")
    print(f"Luas Permukaan tabung= {luasPermukaan}")
    print("")
    print("""Sifat-sifat Tabung:
          1. Memiliki dua sisi berbentuk lingkaran yang sejajar dan sama besar (alas dan tutup).
          2. Memiliki satu sisi lengkung yang menghubungkan kedua sisi lingkaran.
          3. Tidak memiliki titik sudut.""")
    print("------------------------------------------------------")
    print("")

def bola():
    jariJari= int(input("Berapa jari-jari bola?: "))
    phi= 22/7
    volume= 4/3 * phi * jariJari * jariJari * jariJari
    luasPermukaan= 4* phi * jariJari * jariJari
    volume= round(volume,2)
    luasPermukaan= round(luasPermukaan,2)
    print("")
    print("------------------------------------------------------")
    print(f"Volume bola= {volume}")
    print(f"Luas Permukaan bola= {luasPermukaan}")
    print("")
    print("""Sifat-sifat Bola:
          1. Semua titik pada permukaan bola berjarak sama dari pusat bola.
          2. Tidak memiliki sisi datar.
          3. Tidak memiliki rusuk atau titik sudut.""")
    print("------------------------------------------------------")
    print("")

    
def kerucut():
    jariJari= int(input("Berapa jari-jari alas kerucut?: "))
    tinggi= int(input("Berapa tinggi kerucut?: "))
    garisPelukis= int(input("Berapa garis pelukis kerucut?: "))
    phi= 22/7
    volume= (1/3) * phi * jariJari * jariJari * tinggi
    luasPermukaan= phi * jariJari * (jariJari + garisPelukis)
    volume= round(volume,2)
    luasPermukaan= round(luasPermukaan,2)
    print("")
    print("------------------------------------------------------")
    print(f"Volume kerucut= {volume}")
    print(f"Luas Permukaan kerucut= {luasPermukaan}")
    print("")
    print("""Sifat-sifat Kerucut:
          1. Memiliki satu alas berbentuk lingkaran.
          2. Memiliki satu titik puncak yang tidak terletak pada alas.
          3. Memiliki satu sisi lengkung dan satu sisi datar (alas).<br>4. Memiliki satu rusuk lengkung.""")
    print("------------------------------------------------------")
    print("")

def balok():
    panjang= int(input("Berapa panjang balok?: "))
    lebar= int(input("Berapa lebar balok?: "))
    tinggi= int(input("Berapa tinggi balok?: "))
    volume= panjang * lebar * tinggi
    luasPermukaan= 2 * ((panjang * lebar) + (lebar * tinggi) + (tinggi * panjang))
    volume= round(volume,2)
    luasPermukaan= round(luasPermukaan,2)
    print("")
    print("------------------------------------------------------")
    print(f"Volume balok= {volume}")
    print(f"Luas Permukaan balok= {luasPermukaan}")
    print("""Sifat-sifat Balok:
          1. Memiliki enam sisi berbentuk persegi panjang.
          2. Setiap sisi yang berhadapan sama besar.
          3. Memiliki 12 rusuk yang terdiri dari tiga pasang rusuk yang masing-masing pasangannya sama panjang.
          4. Memiliki 8 titik sudut.""")
    print("------------------------------------------------------")
    print("")

def kubus():
    sisi= int(input("Berapa sisi kubus?: "))
    volume= sisi**3
    luasPermukaan= 6 * sisi**2
    volume= round(volume,2)
    luasPermukaan= round(luasPermukaan,2)
    print("")
    print("------------------------------------------------------")
    print(f"Volume kubus= {volume}")
    print(f"Luas Permukaan kubus= {luasPermukaan}")
    print("")
    print("""Sifat-sifat Kubus:
          1. Memiliki enam sisi berbentuk persegi yang sama besar.
          2. Semua rusuknya sama panjang.
          3. Memiliki 12 rusuk.
          4. Memiliki 8 titik sudut.""")
    print("------------------------------------------------------")

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
        
        volume= round(volume,2)
        luasPermukaan= round(luasPermukaan,2)

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

        volume= round(volume,2)
        luasPermukaan= round(luasPermukaan,2)
    
    else:
        print("Jenis limas tidak valid. Masukkan 'segitiga' atau 'segiempat'.")
        return
    print("")
    print("------------------------------------------------------")
    print(f"Luas permukaan limas {jenis}: {luasPermukaan}")
    print(f"Volume limas {jenis}: {volume}")
    print("")
    print("""Sifat-sifat Limas:
          1. Memiliki satu alas yang berbentuk segi-n (segitiga, segi empat, dll).
          2. Memiliki titik puncak yang tidak terletak pada alas.
          3. Jumlah sisi tegaknya sesuai dengan jumlah sisi pada alasnya.
          4. Memiliki sejumlah rusuk yang sama dengan jumlah sisi alas + 1.
          5. Memiliki jumlah titik sudut yang sama dengan jumlah titik sudut alas + 1.""")
    print("------------------------------------------------------")
    print("")
    