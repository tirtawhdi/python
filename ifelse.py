print(f'Halo selamat datang di situs kami!!!')
print(f'Apakah kamu sudah cukup usia untuk membuka situs ini?')
usia = int(input('Masukkan usia kamu untuk melanjutkan '))

if usia <= 0:
    print(f'Wahh, sayangnya kamu belum lahir di dunia ini')
elif usia >= 1 and usia <= 3:
    print(f'Bayi tidak boleh main internet, Banyakin minum asi ya')
elif usia >= 4 and usia <= 5:
    print(f'Balita banyakin tidur ya, jangan main internet terus')
elif usia >= 6 and usia <= 12:
    print(f'Kamu masih anak-anak, main sama temen-temen aja ya')
elif usia >= 13 and usia <= 17:
    print(f'Kamu masih remaja nih, jangan lupa belajar ya')
elif usia >= 18 and usia <=59:
    print(f'Kamu sudah dewasa, kamu bisa melanjutkan ke situs kami ')
elif usia >= 60:
    print(f'Lansia lansia, banyakin main sama cucu ya')