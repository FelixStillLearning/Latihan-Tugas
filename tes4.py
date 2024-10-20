import numpy as np
import matplotlib.pyplot as plt
import time

def create_mushroom_boundary(grid_size_x=15, grid_size_y=15):
    # Inisialisasi grid kosong
    grid = np.zeros((grid_size_y, grid_size_x))
    
    # Membuat bentuk jamur (10x8)
    # Kepala jamur
    # Garis horizontal atas (lebar 8)
    for i in range(3, 11):
        grid[2][i] = 1
    
    # Garis horizontal bawah kepala
    for i in range(3, 11):
        grid[5][i] = 1
    
    # Garis vertikal kiri kepala
    for i in range(2, 6):
        grid[i][2] = 1
    
    # Garis vertikal kanan kepala
    for i in range(2, 6):
        grid[i][11] = 1
    
    # Batang jamur
    # Garis vertikal kiri batang
    for i in range(6, 12):
        grid[i][5] = 1
    
    # Garis vertikal kanan batang
    for i in range(6, 12):
        grid[i][8] = 1
    
    # Garis horizontal bawah batang
    for i in range(5, 9):
        grid[11][i] = 1
    
    return grid

def plot_current_state(grid, title):
    plt.clf()  # Clear figure
    # Custom colormap: putih (background), hitam (boundary), merah (fill)
    colors = ['white', 'black', 'red']
    cmap = plt.matplotlib.colors.ListedColormap(colors)
    
    plt.imshow(grid, cmap=cmap)
    plt.grid(True, color='gray', linewidth=0.5, alpha=0.5)
    plt.xticks(range(15))
    plt.yticks(range(15))
    plt.title(title)
    plt.draw()
    plt.pause(0.1)  # Delay 0.5 detik per langkah

def boundary_fill_8(grid, x, y, fill_value, boundary_value):
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
        return
    
    current_value = grid[x][y]
    if (current_value == boundary_value or current_value == fill_value):
        return
    
    # Fill satu blok
    grid[x][y] = fill_value
    plot_current_state(grid, f"Proses Pengisian Warna (x={x}, y={y})")
    time.sleep(0.5)  # Delay tambahan untuk memperlambat proses
    
    # Mengisi 8 arah tetangga satu per satu
    directions = [
        (x+1, y), (x-1, y),     # kanan, kiri
        (x, y+1), (x, y-1),     # atas, bawah
        (x+1, y+1), (x-1, y+1), # diagonal kanan atas, kiri atas
        (x+1, y-1), (x-1, y-1)  # diagonal kanan bawah, kiri bawah
    ]
    
    for next_x, next_y in directions:
        boundary_fill_8(grid, next_x, next_y, fill_value, boundary_value)

# Set up plot
plt.figure(figsize=(8, 8))

# Buat dan tampilkan grid awal
grid = create_mushroom_boundary()
plot_current_state(grid, "Outline Jamur (Hitam)")
plt.pause(2)  # Tahan 2 detik sebelum mulai mengisi

# Mulai proses pengisian
print("Mengisi kepala jamur...")
boundary_fill_8(grid, 3, 6, 2, 1)  # Fill kepala

print("Mengisi batang jamur...")
boundary_fill_8(grid, 8, 6, 2, 1)  # Fill batang

# Tampilkan hasil akhir
plot_current_state(grid, "Hasil Akhir")
plt.show()

print("Proses pengisian warna selesai!")