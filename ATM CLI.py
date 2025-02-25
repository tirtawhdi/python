saldo = 8000000
hutang = 1000000
welcome = 'Halo selamat datang di ATM Tirta jaya'
opsi = '''Ketik "1" untuk mengecek saldo
Ketik "2" untuk mengisi saldo
Ketik "3" untuk mengecek hutang
Ketik "4" untuk membayar hutang
Ketik "0" untuk exit'''

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
    if total_bayar > saldo:
        print('Saldo tidak mencukupi')
        input('Tekan enter untuk kembali ke menu')
        return main()
    elif total_bayar > hutang:
        print('Kamu memasukan angka melebihi hutang')
        print(f'Kamu memiliki hutang sebesar {rupiah(hutang)}')
        print(f'Kamu akan membayar hutang sebesar {rupiah(hutang)}')
        jawab = input('Ketik "ya" untuk melanjutkan, "tidak" untuk kembali ke menu: ')
        if jawab.lower() == 'ya':
            total_bayar = hutang
            hutang = hutang - total_bayar
            saldo = saldo - total_bayar
            print(f'Selamat. kamu telah membayar hutang sebesar {rupiah(total_bayar)}')
            print(f'Sekarang saldo mu adalah {rupiah(saldo)}')
            print('SELAMAT HUTANG MU LUNASSS')
            return saldo, hutang
        if jawab.lower() == 'tidak':
            print('Yasudah. Terimakasih')
            input('Tekan enter untuk kembali ke menu')
            return main()
        else:
            print('Masukan input yang valid')
            input('Tekan enter untuk melanjutkan')
            return bayar_hutang(saldo, hutang, total_bayar)
    elif total_bayar <= saldo:
        hutang = hutang - total_bayar
        saldo = saldo - total_bayar
        print(f'Selamat. kamu telah membayar hutang sebesar {rupiah(total_bayar)}')
        print(f'Sekarang saldo mu adalah {rupiah(saldo)}')
        if hutang <= 0:
            print('Selamat hutang mu lunas!!!')
        else:
            print(f'Sekarang hutang mu adalah {rupiah(hutang)}')
        return saldo, hutang

# Pilihan 4
def bayar_hutang_menu(saldo, hutang):
    if hutang <= 0:
        print('Kamu tidak memiliki hutang')
        input('Tekan enter untuk kembali ke menu')
        return main()
    else:
        print(f'Kamu memiliki saldo sebesar {rupiah(saldo)}')
        print(f'Kamu memiliki hutang sebesar {rupiah(hutang)}')
        print(f'Apakah kam yakin ingin membayar hutang?')
        jawab = input('Jawab "ya" atau "tidak": ')
        if jawab.lower() == 'ya':
            bayar = input('Mau bayar berapa?: ')
            if bayar.isdigit():
                bayar = int(bayar)
                saldo, hutang = bayar_hutang(saldo, hutang, bayar)
                return saldo, hutang
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
    if hutang <= 0:
        print('Kamu tidak memiliki hutang')
        input('Tekan enter untuk kembali ke menu')
        return main()
    else:
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
            input('Tekan enter untuk kembali ke menu')
            return main()
        elif pilihan == 0:
            print('Terimakasih telah menggunakan layanan kami')
            input('Tekan enter untuk keluar')
            return
        else:
            print('Pilihan tidak tersedia')
            return main()
    else:
        print(f'Masukan input yang valid')
        input('Tekan enter untuk melanjutkan')
        return main()
main()