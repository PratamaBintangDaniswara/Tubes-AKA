# <h1 align="center">Analisis perbandingan algoritma Pemangkatan dengan metode iteratif D&C vs Rekursif D&C</h1>
<p align="center">Pratama Bintang Daniswara - 103112400051</p>
<p align="center">Abid Fadilah Mustofa - 103112400046</p>
<p align="center">Muhammad Fatham Mubina - 103112430188</p>

### Code
```py
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000) # Limit agar tidak error 

def powerIterativeDc(a, n):
    result = 1
    base = a
    exponent = n
    while exponent > 0:
        if exponent % 2 == 1: # Jika pangkat ganjil
            result *= base
        base *= base # Kuadratkan basis
        exponent //= 2 # Bagi pangkat menjadi dua
    return result

def powerRecursiveDc(a, n): # Menghitung pangkat D&C Rekursif
    if n == 0: return 1
    if n == 1: return a
    temp = powerRecursiveDc(a, n // 2) # Membagi masalah menjadi n // 2
    
    if n % 2 == 0: # Menggabungkan hasil dengan kuadrat
        return temp * temp
    else:
        return a * temp * temp

def main():
    print("Tubes AKA: Analisis D&C Iteratif vs D&C Rekursif")
    try:
        a = int(input("Masukkan angka basis : "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    nHistory = []
    iterDcHistory = []
    recDcHistory = []

    while True:
        userInput = input("Masukkan nilai eksponen (n) atau ketik 'udah ah cape' untuk keluar: ")
        if userInput.lower() == 'udah ah cape':
            print("Sekian dari kelompok kami. Terimakasihhhhh")
            break
        try:
            n = int(userInput)
            if n < 0:
                print("Silakan masukkan angka positif")
                continue
            
            # Pengukuran Waktu
            startI = time.perf_counter() # Iteratif D&C O(log n) 
            powerIterativeDc(a, n)
            tI = time.perf_counter() - startI
            
            startDc = time.perf_counter() # Rekursif D&C O(log n) 
            powerRecursiveDc(a, n)
            tDc = time.perf_counter() - startDc
            
            rawData = list(zip(nHistory, iterDcHistory, recDcHistory)) # Simpan dan Pengurutan Data 
            rawData.append((n, tI, tDc))
            rawData.sort(key=lambda x: x[0])
            
            nHistory, iterDcHistory, recDcHistory = zip(*rawData)
            nHistory, iterDcHistory, recDcHistory = list(nHistory), list(iterDcHistory), list(recDcHistory)
            
            print(f"Hasil Tes n={n}:")
            print(f"- Iteratif D&C: {tI:.8f} detik")
            print(f"- Rekursif D&C: {tDc:.8f} detik")
             
            plt.figure(figsize=(10, 6)) # Grafik 
            plt.plot(nHistory, iterDcHistory, marker='s', label='Iterative D&C O(log n)', color='pink', linewidth=2)
            plt.plot(nHistory, recDcHistory, marker='o', label='Recursive D&C O(log n)', color='blue', linewidth=2)
            
            plt.title(f'Analisis Performa D&C (Basis a = {a})')
            plt.xlabel('Nilai Eksponen (n)')
            plt.ylabel('Waktu Eksekusi (detik)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            
            print("\nGrafik terbuka. Tutup grafik untuk input selanjutnya.")
            plt.show()
            
        except ValueError:
            print("error. Masukan angka bulat.")

if __name__ == "__main__":
    main()
```

##### a=2 n=1000
![Screenshot Output 1](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000.png)

##### a=2 n=1000, 3000 
![Screenshot Output 2](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000.png)
 
##### a=2 n=1000, 3000, 5000
![Screenshot Output 3](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000%2C%205000.png)

##### a=2 n=1000, 3000, 5000, 7000
![Screenshot Output 3](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000%2C%205000%2C%207000.png)

##### a=2 n=1000, 3000, 5000, 7000, 10000
![Screenshot Output 3](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000%2C%205000%2C%207000%2C%2010000.png)