from random import randint
from time import sleep
from mylibs import welcome_message, gua

def sikinci_games(result):
    sikinci = randint(1, 4)
    buah = gua_array
    buah[sikinci - 1] = '|buah|'
    if result.isdigit():
        result = int(result)
        ans = input(f'Apakah kamu yakin memilih gua nomor {result}? (ya/tidak): ')
        if ans.lower() == 'ya':
            print("\033[A\033[K", end="")
            print(f'Kamu memilih gua nomor {result}')
            print('loading -')
            sleep(0.5)
            print("\033[A\033[K", end="")
            print('loading - -')
            sleep(0.5)
            print("\033[A\033[K", end="")
            print('loading - - -')
            sleep(0.5)
            print("\033[A\033[K", end="")
            print('loading - - - -')
            sleep(0.5)
            print("\033[A\033[K", end="")
            print('loading - - - - -')
            sleep(0.5)
            print("\033[A\033[K\033[A\033[K\033[A\033[K\033[A\033[K", end="")
            if result == sikinci:
                print(space, *gua_array, space)
                print(border1)
                print(f'Selamat Kamu berhasil menemukan buah-buahan tersebut')
                print('Kinci pun terkejut dan lari menjauh')
            elif result > 4 or result < 1:
                print('Masukan input yang valid')
            else:
                print(space, *gua_array, space)
                print(border1)
                print('Kamu memilih gua yang salah')
                print('Kinci pun tertawa dan lari menjauh')
                input('Tekan enter untuk exit')
                print("\033[A\033[K", end="")
                print('Terimakasih sudah bermain SIKINCI')
        elif ans.lower  == 'tidak':
            print('baiklah kalau begitu')
    else:
        print('Masukan input yang valid')
        sikinci_games(input('Pilih gua yang kamu rasa benar: '))
def sikinci_games_menu():
    welcome_message('Selamat datang di SIKINCI GAMES')
    jawab = input('Apakah kamu ingin bermain? (ya/tidak): ')
    print("\033[A\033[K", end="")
    while jawab.lower() != 'ya' and jawab.lower() != 'tidak':
        print('Harap masukan input (ya/tidak)')
        jawab = input('Apakah kamu ingin bermain? (ya/tidak): ')
        print("\033[A\033[K\033[A\033[K", end="")
    if jawab.lower() == 'ya':
        nama = input('Silahkan masukan nama kamu: ')
        print("\033[A\033[K", end="")
        while len(nama) < 2 or nama == ' ':
            print('Nama harus terdiri inimal 3 karakter')
            nama = input('Silahkan masukan nama kamu: ')
            print("\033[A\033[K\033[A\033[K", end="")
        print(f'Halo {nama}, kamu akan bermain SIKINCI')
        input('Tekan enter untuk melanjutkan')
        print("\033[A\033[K\033[A\033[K\033[A\033[K\033[A\033[K", end="")
        print('Kinci adalah hewan yang suka mencuri dan bersembunyi')
        print('Kinci suka bersembunyi di tempat yang gelap dan lembab.')
        input('Tekan enter untuk melanjutkan')
        print("\033[A\033[K", end="")
        print('Suatu hari kinci mencuri buah-buahan dan ia pun menyembunyikan buah-buahan tersebut.')
        print('Kinci menyembunyikan buah-buahan tersebut di tempat yang gelap dan lembab.')
        input('Tekan enter untuk melanjutkan')
        print("\033[A\033[K", end="")
        print('Lalu kamu secara tidak sengaja melihat kinci yang sedang menyembunyikan buah-buahan di gua')
        print('Tetapi terdapat 4 gua yang berbeda')
        print('Kamu harus memilih gua yang benar untuk mendapatkan buah-buahan tersebut')
        input('Tekan enter untuk melanjutkan')
        print("\033[A\033[K", end="")
        gua()
        jawaban = input('Pilih gua yang kamu rasa benar: ')
        print("\033[A\033[K\033[A\033[K", end="")
        sikinci_games(jawaban)
    else:
        print('Baiklah kalau begitu')
        input('Tekan enter untuk exit')
sikinci_games_menu()