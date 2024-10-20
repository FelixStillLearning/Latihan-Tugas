import numpy as np
import matplotlib.pyplot as plt

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
    
    # Mengisi 8 arah tetangga
    boundary_fill_8(grid, x+1, y, fill_value, boundary_value)
    boundary_fill_8(grid, x-1, y, fill_value, boundary_value)
    boundary_fill_8(grid, x, y+1, fill_value, boundary_value)
    boundary_fill_8(grid, x, y-1, fill_value, boundary_value)
    boundary_fill_8(grid, x+1, y+1, fill_value, boundary_value)
    boundary_fill_8(grid, x-1, y+1, fill_value, boundary_value)
    boundary_fill_8(grid, x+1, y-1, fill_value, boundary_value)
    boundary_fill_8(grid, x-1, y-1, fill_value, boundary_value)

def plot_grid(grid, title):
    plt.figure(figsize=(8, 8))
    
    # Custom colormap untuk 3 warna
    colors = ['white', 'red', 'black']
    cmap = plt.matplotlib.colors.ListedColormap(colors)
    
    # Plot grid dengan imshow
    plt.imshow(grid, cmap=cmap)
    
    # Tambahkan grid
    plt.grid(True, color='black', linewidth=0.5)
    
    # Atur ticks
    plt.xticks(range(15))
    plt.yticks(range(15))
    
    plt.title(title)
    plt.show()

# Buat grid dan tampilkan
grid = create_mushroom_boundary()
plot_grid(grid, "Jamur (Sebelum Boundary Fill)")

# Lakukan boundary fill
# Fill kepala jamur
boundary_fill_8(grid, 4, 7, 2, 1)  # Fill kepala
# Fill batang jamur
boundary_fill_8(grid, 9, 7, 2, 1)  # Fill batang

plot_grid(grid, "Jamur (Setelah Boundary Fill)")
