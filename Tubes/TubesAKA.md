# <h1 align="center">Analisis perbandingan algoritma Pemangkatan dengan metode iteratif D&C vs Rekursif D&C</h1>
<p align="center">Pratama Bintang Daniswara - 103112400051</p>
<p align="center">Abid Fadilah Mustofa - 103112400046</p>
<p align="center">Muhammad Fatham Mubina - 103112430188</p>

### Code
```py
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000) # limit

def power_iterative_dc(a, n):
    result = 1
    base = a
    exponent = n
    while exponent > 0:
        if exponent % 2 == 1: # Jika pangkat ganjil, kalikan hasil dengan basis saat ini
            result *= base
        base *= base # Kuadratkan basis
        exponent //= 2 # Bagi pangkat menjadi dua(Divide)
    return result

def power_recursive_dc(a, n):
    if n == 0: return 1
    if n == 1: return a
    temp = power_recursive_dc(a, n // 2)
    if n % 2 == 0:
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

    n_history = []
    iter_dc_history = []
    rec_dc_history = []

    while True:
        user_input = input("Masukkan nilai eksponen (n) atau ketik 'udah ah cape' untuk keluar: ")
        if user_input.lower() == 'udah ah cape':
            break
        try:
            n = int(user_input)
            if n < 0:
                print("Silakan masukkan angka positif")
                continue
            
            #Pengukuran Waktu
            start_i = time.perf_counter() # Iteratif D&C O(log n)
            power_iterative_dc(a, n)
            t_i = time.perf_counter() - start_i
            
            start_dc = time.perf_counter() # Rekursif D&C O(log n)
            power_recursive_dc(a, n)
            t_dc = time.perf_counter() - start_dc
            
            raw_data = list(zip(n_history, iter_dc_history, rec_dc_history)) # Simpan dan Pengurutan data
            raw_data.append((n, t_i, t_dc))
            raw_data.sort(key=lambda x: x[0])
            
            n_history, iter_dc_history, rec_dc_history = zip(*raw_data)
            n_history, iter_dc_history, rec_dc_history = list(n_history), list(iter_dc_history), list(rec_dc_history)
            
            print(f"Hasil Tes n={n}:")
            print(f"- Iteratif D&C: {t_i:.8f} detik")
            print(f"- Rekursif D&C: {t_dc:.8f} detik")
            
            plt.figure(figsize=(10, 6)) # Grafik
            plt.plot(n_history, iter_dc_history, marker='s', label='Iterative D&C O(log n)', color='pink', linewidth=2)
            plt.plot(n_history, rec_dc_history, marker='o', label='Recursive D&C O(log n)', color='blue', linewidth=2)
            
            plt.title(f'Analisis Performa D&C (Basis a = {a})')
            plt.xlabel('Nilai Eksponen (n)')
            plt.ylabel('Waktu Eksekusi (detik)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            
            print("\nGrafik terbuka. Tutup jendela grafik untuk input selanjutnya.")
            plt.show()
            
        except ValueError:
            print("Error: Masukkan angka bulat.")

if __name__ == "__main__":
    main()
```

### Output
##### a=2 n=1000
![Screenshot Output 1](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000.png)

##### a=2 n=1000, 3000 
![Screenshot Output 2](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000.png)
 
##### a=2 n=1000, 3000, 5000
![Screenshot Output 3](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000%2C%205000.png)

##### a=2 n=1000, 3000, 5000, 7000
![Screenshot Output 4](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000%2C%205000%2C%207000.png)

##### a=2 n=1000, 3000, 5000, 7000, 10000

![Screenshot Output 5](https://github.com/PratamaBintangDaniswara/Tubes-AKA/blob/main/Tubes/a%3D2%20n%3D1000%2C%203000%2C%205000%2C%207000%2C%2010000.png)


### Poster
!![Screenshot Output 4](https://www.canva.com/design/DAG8P-wYiw8/Kof9cJ8As4fAxCDxQEmNEQ/edit)
