import time
import matplotlib.pyplot as plt
import sys

# Menambah limit rekursi untuk pengerjaan pangkat besar
sys.setrecursionlimit(20000)

#DEFINISI ALGORITMA 

def power_iterative(a, n):
    """Menghitung pangkat dengan perulangan (O(n))"""
    result = 1
    for _ in range(n):
        result *= a
    return result

def power_recursive_dc(a, n):
    """Menghitung pangkat dengan Divide and Conquer (O(log n))"""
    if n == 0: return 1
    if n == 1: return a
    # Divide & Conquer: a^n = (a^(n/2))^2
    temp = power_recursive_dc(a, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        return a * temp * temp

#PROGRAM UTAMA 

def main():
    print("=== Tubes AKA: Analisis Perbandingan Algoritma Pemangkatan ===")
    try:
        a = int(input("Masukkan angka basis : "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    # List untuk menyimpan sejarah pengujian
    n_history = []
    iter_history = []
    dc_history = []

    while True:
        print("\n" + "="*40)
        user_input = input("Masukkan nilai eksponen (n) atau ketik 'exit' untuk keluar: ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            n = int(user_input)
            if n < 0:
                print("Silakan masukkan angka positif.")
                continue
            
            # Pengukuran Waktu 
            # Iteratif O(n)
            start_i = time.perf_counter()
            power_iterative(a, n)
            t_i = time.perf_counter() - start_i
            
            # Divide & Conquer O(log n)
            start_dc = time.perf_counter()
            power_recursive_dc(a, n)
            t_dc = time.perf_counter() - start_dc
            
            # Simpan dan Urutkan Data
            # Data harus diurutkan berdasarkan n agar garis grafik tidak berantakan
            raw_data = list(zip(n_history, iter_history, dc_history))
            raw_data.append((n, t_i, t_dc))
            raw_data.sort(key=lambda x: x[0]) # Urutkan berdasarkan n
            
            # Pisahkan kembali ke list masing-masing
            n_history, iter_history, dc_history = zip(*raw_data)
            n_history = list(n_history)
            iter_history = list(iter_history)
            dc_history = list(dc_history)
            
            # Tampilkan statistik singkat di terminal
            print(f"Hasil Tes n={n}:")
            print(f"- Iteratif: {t_i:.8f} detik")
            print(f"- Rekursif D&C: {t_dc:.8f} detik")
            
            # Menampilkan Grafik 
            plt.figure(figsize=(10, 6))
            plt.plot(n_history, iter_history, marker='s', label='Iteratif O(n)', color='red', linewidth=2)
            plt.plot(n_history, dc_history, marker='o', label='Recursive D&C O(log n)', color='blue', linewidth=2)
            
            plt.title(f'Analisis Performa Pemangkatan (Basis a = {a})')
            plt.xlabel('Nilai Eksponen (n)')
            plt.ylabel('Waktu Eksekusi (detik)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            
            print("\n[INFO] Grafik terbuka. Tutup jendela grafik untuk input selanjutnya.")
            plt.show() # Program akan berhenti di sini sampai grafik ditutup
            
        except ValueError:
            print("Error: Harap masukkan angka bulat (integer) atau ketik 'exit'.")

if __name__ == "__main__":

    main()
