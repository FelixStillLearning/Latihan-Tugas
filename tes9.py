import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def create_mushroom_boundary(grid_size_x=15, grid_size_y=15):
    # Inisialisasi grid kosong
    grid = np.zeros((grid_size_y, grid_size_x))
    
    # Membuat bentuk jamur (10x8)
    # Kepala jamur
    # Garis horizontal atas (lebar 8)
    for i in range(3, 11):
        grid[2][i] = 1
    
    # Garis horizontal bawah kepala yang terhubung dengan batang
    for i in range(3, 5):  # sisi kiri
        grid[5][i] = 1
    for i in range(9, 11):  # sisi kanan
        grid[5][i] = 1
    
    # Garis vertikal kiri kepala
    for i in range(2, 6):
        grid[i][2] = 1
    
    # Garis vertikal kanan kepala
    for i in range(2, 6):
        grid[i][11] = 1
    
    # Batang jamur
    # Garis vertikal kiri batang
    for i in range(5, 12):
        grid[i][5] = 1
    
    # Garis vertikal kanan batang
    for i in range(5, 12):
        grid[i][8] = 1
    
    # Garis horizontal bawah batang
    for i in range(5, 9):
        grid[11][i] = 1
    
    return grid

def plot_current_state(grid, title):
    plt.clf()
    # Warna: putih (0), hitam (1), red (2)
    colors = ['white', 'black', 'red']
    cmap = plt.matplotlib.colors.ListedColormap(colors)

    # Tampilkan grid menggunakan colormap yang disesuaikan
    plt.imshow(grid, cmap=cmap, vmin=0, vmax=2)
    plt.grid(True, color='gray', linewidth=0.5, alpha=0.5)
    plt.xticks(np.arange(-0.5, 15, 1))
    plt.yticks(np.arange(-0.5, 15, 1))
    plt.title(title)
    plt.gca().set_xticks(np.arange(-.5, grid.shape[1], 1), minor=True)
    plt.gca().set_yticks(np.arange(-.5, grid.shape[0], 1), minor=True)
    plt.gca().grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
    plt.gca().tick_params(which='minor', size=0)
    plt.draw()
    plt.pause(0.2)


def boundary_fill_simultaneous(grid, start_x, start_y, fill_value, boundary_value, connectivity=4):
    if grid[start_x][start_y] == boundary_value or grid[start_x][start_y] == fill_value:
        return
    
    queue = deque([(start_x, start_y)])
    
    # Definisi arah tetangga berdasarkan connectivity
    if connectivity == 4:
        neighbors = [
            (-1, 0),  # atas
            (1, 0),   # bawah
            (0, -1),  # kiri
            (0, 1)    # kanan
        ]
    else:  # 8-connected
        neighbors = [
            (-1, 0),  # atas
            (1, 0),   # bawah
            (0, -1),  # kiri
            (0, 1),   # kanan
            (-1, -1), # diagonal kiri atas
            (-1, 1),  # diagonal kanan atas
            (1, -1),  # diagonal kiri bawah
            (1, 1)    # diagonal kanan bawah
        ]
    
    while queue:
        # List untuk menyimpan titik-titik yang akan diisi pada langkah berikutnya
        next_points = []
        
        # Proses semua titik dalam queue secara bersamaan
        while queue:
            x, y = queue.popleft()
            
            # Periksa batasan grid
            if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
                continue

            # Periksa nilai boundary dan fill
            if grid[x][y] == boundary_value or grid[x][y] == fill_value:
                continue

            # Isi titik saat ini
            grid[x][y] = fill_value

            # Tambahkan semua tetangga yang valid ke dalam next_points
            for dx, dy in neighbors:
                next_x, next_y = x + dx, y + dy
                if (0 <= next_x < len(grid) and 
                    0 <= next_y < len(grid[0]) and 
                    grid[next_x][next_y] != boundary_value and 
                    grid[next_x][next_y] != fill_value):
                    next_points.append((next_x, next_y))
        
        # Masukkan next_points ke dalam queue untuk diproses pada langkah berikutnya
        queue.extend(next_points)
        
        # Perbarui tampilan setiap langkah (simultaneous filling)
        plot_current_state(grid, "Proses Pengisian Serentak")
        
i = True
while  i :
    # Set up plot
    plt.figure(figsize=(8, 8))

    # Buat dan tampilkan grid awal
    grid = create_mushroom_boundary()
    plot_current_state(grid, "Outline Jamur (Hitam)")
    plt.pause(2)

    # Tanyakan user ingin menggunakan 4-connected atau 8-connected
    print("Pilih metode pengisian:")
    print("1. 4-connected")
    print("2. 8-connected")
    choice = input("Masukkan pilihan (1/2): ")

    # Mulai proses pengisian serentak
    print("Mengisi jamur secara serentak...")
    if choice == "1":
        boundary_fill_simultaneous(grid, 3, 6, 2, 1, connectivity=4)
    else:
        boundary_fill_simultaneous(grid, 3, 6, 2, 1, connectivity=8)
    # Tampilkan hasil akhir
    plot_current_state(grid, "Hasil Akhir")
    plt.show()

    print("Proses pengisian warna selesai!")\
    
    ulang = input("Apakah ingin melanjutkan (y/n)? ")

    if ulang == "n":
        i = False
    else:
        continue