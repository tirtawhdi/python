saldo = 0
hutang = 1000000
welcome = 'Halo selamat datang di ATM Tirta jaya'
opsi = '''Ketik "1" untuk mengecek saldo
Ketik "2" untuk mengisi saldo
Ketik "3" untuk mengecek hutang
Ketik "4" untuk membayar hutang'''

# Integer ke rupiah
def rupiah(saldo):
    return f'Rp{saldo:,.2f}'.replace(',', '.')

# Deposit
def deposit(saldo, total_depo):
    saldo = saldo + total_depo
    print(f'Selamat. Anda berhasil deposit sebesar {rupiah(total_depo)}')
    print(f'Sekarang saldo anda adalah {rupiah(saldo)}')
    return saldo

def depo():
    duit = input('Masukkan nominal deposit: ')
    if duit.isdigit():
        duit = int(duit)
        duit = deposit(saldo, duit)
        return duit 
    else:
        print('Masukan input yang valid')
        return depo()
# Saldo
def cek_saldo(saldo):
    print(f'Saldo anda adalah {rupiah(saldo)}')
    
# Bayar hutang fungsi    
def bayar_hutang(saldo, hutang, total_bayar):
    hutang = hutang - total_bayar
    saldo = saldo - total_bayar
    print(f'Selamat. kamu telah membayar hutang sebesar {rupiah(total_bayar)}')
    print(f'Sekarang saldo mu adalah {rupiah(saldo)}')
    return saldo, hutang

# Pilihan 4
def bayar_hutang_menu(saldo, hutang):
    print(f'Kamu memiliki saldo sebesar {rupiah(saldo)}')
    print(f'Kamu memiliki hutang sebesar {rupiah(hutang)}')
    print(f'Apakah kam yakin ingin membayar hutang?')
    jawab = input('Jawab "ya" atau "tidak": ')
    if jawab.lower() == 'ya':
        bayar = input('Mau bayar berapa?: ')
        if bayar.isdigit():
            bayar = int(bayar)
            if bayar > saldo:
                print('Saldo tidak mencukupi')
                input('Tekan enter untuk kembali ke menu')
                return main()
            else:
                saldo, hutang = bayar_hutang(saldo, hutang, bayar)
        else:
            print('Masukan input yang valdi')
            input('Tekan enter untuk melanjutkan')
            return bayar_hutang_menu(saldo, hutang)
    elif jawab.lower() == 'tidak':
        print('Yasudah. Terimakasih')
        input('Tekan enter untuk kembali ke menu')
        return main()
    else:
        print('Input tidak valid')
        input('Tekan enter untuk melanjutkan')
        bayar_hutang_menu(saldo, hutang)
        return saldo, hutang

# Cek hutang
def cek_hutang(hutang):
    print(f'Hutang anda adalah {rupiah(hutang)}')
    input('Tekan enter untuk kembali ke menu')
    return main()

def main():
    global saldo, hutang
    print(welcome)
    print(opsi)
    pilihan = input('Masukan pilihanmu: ')
    if pilihan.isdigit():
        pilihan = int(pilihan)
        if pilihan == 1:
            cek_saldo(saldo)
            input('Tekan enter untuk kembali ke menu')
            return main()
        elif pilihan == 2:
            saldo = depo()
            input('Tekan enter untuk kembali ke menu')
            return main()
        elif pilihan == 3:
            cek_hutang(hutang)
        elif pilihan == 4:
            saldo, hutang = bayar_hutang_menu(saldo, hutang)
        else:
            print('Pilihan tidak tersedia')
    else:
        print(f'Masukan input yang valid')
        input('Tekan enter untuk melanjutkan')
        return main()
main()