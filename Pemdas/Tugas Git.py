data_panen = { 
    'lokasi1' : {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 600
        }
    },
    'lokasi3': {
        'nama_lokasi':'kebun c',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'kebun D',
        'hasil_panen' : {
            'padi': 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#nomor1
def total_panen():
    for i in data_panen.items():
        print(f"\n{i[0]}")
        print(f"Lokasi: {i[1]['nama_lokasi']}")
        for j in i[1]['hasil_panen'].items():
            print(f"{j[0]}: {j[1]}")
total_panen()

#nomor2
print("\ntotal jagung lokasi 2:",data_panen['lokasi2']['hasil_panen']['jagung'])

#nomor3
print("\nnama lokasi 3:",data_panen['lokasi3']['nama_lokasi'])

#nomor4
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

#nomor5
jumlah_padi = padi_lokasi1 + padi_lokasi2 + padi_lokasi3 + padi_lokasi4 + padi_lokasi5
jumlah_kedelai = kedelai_lokasi1 + kedelai_lokasi2 + kedelai_lokasi3 + kedelai_lokasi4 + kedelai_lokasi5

print("\ntotal padi: ",jumlah_padi)
print("total kedelai: ",jumlah_kedelai)

#nomor6
def pengecekan():
    for k,i in data_panen.items():
        if i['hasil_panen']['jagung'] > 800 or i['hasil_panen']['padi'] > 1300 :
            print("\nlokasi memerlukan perhatian khusus untuk penanganan hasil panen")
        else:
            print("\nlokasi dalam kondisi baik maknyus")
pengecekan()

print("tugas git")
print("ini perubahan")
