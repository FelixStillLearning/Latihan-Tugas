import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def create_mushroom_boundary(grid_size=15):
    # Inisialisasi grid kosong
    grid = np.zeros((grid_size, grid_size))
    
    # Membuat bentuk jamur
    # Kepala jamur
    # Garis horizontal atas
    for i in range(5, 10):
        grid[3][i] = 1
    
    # Garis horizontal bawah kepala
    for i in range(5, 10):
        grid[6][i] = 1
    
    # Garis vertikal kiri kepala
    for i in range(3, 7):
        grid[i][4] = 1
    
    # Garis vertikal kanan kepala
    for i in range(3, 7):
        grid[i][10] = 1
    
    # Batang jamur
    # Garis vertikal kiri batang
    for i in range(7, 12):
        grid[i][6] = 1
    
    # Garis vertikal kanan batang
    for i in range(7, 12):
        grid[i][8] = 1
    
    # Garis horizontal bawah batang
    for i in range(6, 9):
        grid[11][i] = 1
    
    return grid

def boundary_fill_8(grid, x, y, fill_value, boundary_value):
    if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
        return
    
    current_value = grid[x][y]
    if (current_value == boundary_value or current_value == fill_value):
        return
        
    grid[x][y] = fill_value
    plt.clf()  # Clear the current figure
    plot_current_state(grid, "Proses Pengisian Warna")
    plt.pause(0.1)  # Memberikan delay kecil untuk animasi
    
    # Mengisi 8 arah tetangga
    boundary_fill_8(grid, x+1, y, fill_value, boundary_value)
    boundary_fill_8(grid, x-1, y, fill_value, boundary_value)
    boundary_fill_8(grid, x, y+1, fill_value, boundary_value)
    boundary_fill_8(grid, x, y-1, fill_value, boundary_value)
    boundary_fill_8(grid, x+1, y+1, fill_value, boundary_value)
    boundary_fill_8(grid, x-1, y+1, fill_value, boundary_value)
    boundary_fill_8(grid, x+1, y-1, fill_value, boundary_value)
    boundary_fill_8(grid, x-1, y-1, fill_value, boundary_value)

def plot_current_state(grid, title):
    # Custom colormap: putih (background), hitam (boundary), merah (fill)
    colors = ['white', 'black', 'red']
    cmap = plt.matplotlib.colors.ListedColormap(colors)
    
    # Plot grid dengan imshow
    plt.imshow(grid, cmap=cmap)
    
    # Tambahkan grid
    plt.grid(True, color='gray', linewidth=0.5, alpha=0.5)
    
    # Atur ticks
    plt.xticks(range(15))
    plt.yticks(range(15))
    
    plt.title(title)

# Set up the figure
plt.figure(figsize=(8, 8))

# Buat grid dan tampilkan kondisi awal
grid = create_mushroom_boundary()
plot_current_state(grid, "Outline Jamur (Hitam)")
plt.show()

# Tunggu sebentar sebelum mulai filling
time.sleep(2)

# Setup figure baru untuk proses filling
plt.figure(figsize=(8, 8))

# Lakukan boundary fill untuk kepala jamur
print("Mengisi kepala jamur...")
boundary_fill_8(grid, 4, 7, 2, 1)  # Fill kepala

# Tunggu sebentar sebelum mengisi batang
time.sleep(1)

# Lakukan boundary fill untuk batang jamur
print("Mengisi batang jamur...")
boundary_fill_8(grid, 9, 7, 2, 1)  # Fill batang

# Tampilkan hasil akhir
plt.clf()
plot_current_state(grid, "Hasil Akhir")
plt.show()

print("Proses pengisian warna selesai!")