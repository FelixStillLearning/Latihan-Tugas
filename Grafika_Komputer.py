import numpy as np
import matplotlib.pyplot as plt

def create_mushroom_boundary(grid_size=15):
    # Inisialisasi grid kosong dengan nilai 0
    grid = np.zeros((grid_size, grid_size))
    
    # Membuat bentuk jamur yang lebih besar (nilai 1 untuk boundary)
    # Bagian kepala jamur
    grid[2, 4:11] = 1    # Atas
    grid[7, 4:11] = 1    # Bawah
    grid[3:7, 3] = 1     # Kiri
    grid[3:7, 11] = 1    # Kanan
    
    # Membuat lengkungan kepala jamur
    grid[2, 4:11] = 1    # Atas
    grid[3, 3:12] = 1    # Baris kedua
    grid[6, 3:12] = 1    # Baris sebelum bawah
    grid[7, 4:11] = 1    # Bawah
    
    # Bagian batang jamur
    grid[8:12, 6:9] = 1  # Batang vertikal
    
    # Bagian bawah batang (sedikit lebih lebar)
    grid[11, 5:10] = 1   # Dasar batang
    
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
    plt.figure(figsize=(10, 10))
    # Custom colormap: putih (background), merah (boundary), putih (fill)
    colors = ['white', '#FF0000', 'white']
    plt.imshow(grid, cmap=plt.matplotlib.colors.ListedColormap(colors))
    
    # Menambahkan grid
    plt.grid(True, which='major', color='black', linestyle='-', linewidth=0.5)
    plt.xticks(np.arange(-0.5, len(grid), 1), [])
    plt.yticks(np.arange(-0.5, len(grid), 1), [])
    
    plt.title(title)
    plt.show()

# Membuat dan menampilkan grid
grid = create_mushroom_boundary()
plot_grid(grid, "Bentuk Jamur (Sebelum Boundary Fill)")

# Melakukan boundary fill
# Fill kepala jamur
boundary_fill_8(grid, 4, 7, 2, 1)  # Titik di tengah kepala jamur
# Fill batang jamur
boundary_fill_8(grid, 9, 7, 2, 1)  # Titik di tengah batang jamur

plot_grid(grid, "Bentuk Jamur (Setelah Boundary Fill)")

# Menampilkan koordinat grid
print("\nPetunjuk koordinat grid:")
print("- Boundary (Merah) ditandai dengan nilai 1")
print("- Fill area (Putih) ditandai dengan nilai 2")
print("- Background (Putih) ditandai dengan nilai 0")