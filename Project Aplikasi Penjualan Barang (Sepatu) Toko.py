listSepatu = [
    {
        'nama': 'Adizero Adidas',
        'merk': 'Adidas',
        'warna': 'Hitam',
        'stock': 5,
        'size': 41,
        'harga': 3400000
    },
    {
        'nama': 'Adidas Tubular',
        'merk': 'Adidas',
        'warna': 'Merah',
        'stock': 10,
        'size': 42,
        'harga': 4500000
    },
    {
        'nama': 'Nike Air Jordan',
        'merk': 'Nike',
        'warna': 'Biru',
        'stock': 8,
        'size': 43,
        'harga': 1000000
    }
]

cart = []

def listSepatumenampilkanDaftarSepatu() :
    print('Daftar Sepatu\n')
    print('Index\t| Nama        \t\t| Merk       \t| Warna   \t| Stock | Size\t| Harga (Rp)')
    for i in range(len(listSepatu)) :
        print('{}\t| {}  \t| {}  \t| {}  \t| {}  \t| {}\t| {}'.format(i,listSepatu[i]['nama'],listSepatu[i]['merk'],listSepatu[i]['warna'],listSepatu[i]['stock'],listSepatu[i]['size'],listSepatu[i]['harga']))

def menambahSepatu() :
    namaSepatu = input('Masukkan Nama Sepatu : ')
    merkSepatu = input('Masukkan Merk Sepatu : ')
    warnaSepatu = input('Masukkan Warna Sepatu : ')
    stockSepatu = int(input('Masukkan Stock Sepatu : '))
    sizeSepatu = int(input('Masukkan Size Sepatu : '))
    hargaSepatu = int(input('Masukkan Harga Sepatu : '))
    listSepatu.append({
        'nama': namaSepatu,
        'merk': merkSepatu,
        'warna': warnaSepatu,
        'stock': stockSepatu,
        'size': sizeSepatu,
        'harga': hargaSepatu
    })
    listSepatumenampilkanDaftarSepatu()

def menghapusSepatu() :
    listSepatumenampilkanDaftarSepatu()
    indexSepatu = int(input('Masukkan index sepatu yang ingin dihapus : '))
    del listSepatu[indexSepatu]
    listSepatumenampilkanDaftarSepatu()

def membeliSepatu() :
    listSepatumenampilkanDaftarSepatu()
    while True :
        indexSepatu = int(input('Masukkan index sepatu yang ingin dibeli : '))
        qtySepatu = int(input('Masukkan jumlah yang ingin dibeli : '))
        if(qtySepatu > listSepatu[indexSepatu]['stock']) :
            print('Stock tidak cukup, stock {} tinggal {}'.format(listSepatu[indexSepatu]['nama'],listSepatu[indexSepatu]['stock']))
        else :
            cart.append({
                'nama': listSepatu[indexSepatu]['nama'], 
                'qty': qtySepatu, 
                'harga': listSepatu[indexSepatu]['harga'], 
                'index': indexSepatu
            })
        print('Isi Cart :')
        print('Nama\t| Qty\t| Harga')
        for item in cart :
            print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
        checker = input('Mau beli yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Daftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    totalHarga = 0
    for item in cart :
        print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
        totalHarga += item['qty'] * item['harga']    
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = int(input('Masukkan jumlah uang : '))
        if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
            for item in cart :
                listSepatu[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for item in cart :
                listSepatu[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        else :
            kekurangan = totalHarga - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))

while True :
    pilihanMenu = input('''
        Selamat Datang di Toko Sepatu Jaya Makmur

        List Menu :
        1. Menampilkan Daftar Sepatu
        2. Menambah Daftar Sepatu
        3. Menghapus Daftar Sepatu
        4. Membeli Sepatu
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        listSepatumenampilkanDaftarSepatu()
    elif(pilihanMenu == '2') :
        menambahSepatu()
    elif(pilihanMenu == '3') :
        menghapusSepatu()
    elif(pilihanMenu == '4') :
        membeliSepatu()
    elif(pilihanMenu == '5') :
        break
    
