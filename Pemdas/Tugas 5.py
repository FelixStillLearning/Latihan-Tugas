def hitung_IMT(berat_badan, tinggi_badan):
    IMT = berat_badan / (tinggi_badan ** 2)
    
    if IMT < 18.5:
        kondisi = "Underweight"
    elif IMT >= 18.5 and IMT < 25:
        kondisi = "Normal weight"
    elif IMT >= 25 and IMT < 30:
        kondisi = "Overweight"
    else:
        kondisi = "Obesity"
    
    return IMT, kondisi

banyak_data = []   
while True:
    nama = input("Masukkan nama: ")
    berat_badan = float(input("Berat badan (kg): "))
    tinggi_badan = float(input("Tinggi badan (m): "))
    IMT, kondisi = hitung_IMT(berat_badan, tinggi_badan)

    banyak_data.append({ 'nama': nama, 'berat_badan': berat_badan, 'tinggi_badan': tinggi_badan, 'IMT': IMT, 'kondisi': kondisi })

    retry = input("mau itung lagi ga? (y/n): ")
    if retry == 'n':
        break
    elif retry  != 'y':
        print("jawaban tidak valid")
        break 

# for i,data in enumerate(banyak_data):
#     print("data ke",i+1)
#     print(f"Nama = {data['nama']}\nberat badan = {data['berat_badan']}\ntinggi badan = {data['tinggi_badan']}\nIMT = {data['IMT']}\nkondisi = {data['kondisi']}")

for data in (banyak_data):
    # print("data ke",i+1)
    print(f"Nama = {data['nama']}\nberat badan = {data['berat_badan']}\ntinggi badan = {data['tinggi_badan']}\nIMT = {data['IMT']}\nkondisi = {data['kondisi']}")