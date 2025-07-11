# WORDEX
# enough reborn kodlarından yararlanılmıştır
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

# WORDEX ASCII Sanatı Başlangıcı
def print_ascii():
    print("""
W       W   OOOOO   RRRRR   DDDD    EEEEE   X     X
W       W  O     O  R    R  D   D   E        X   X
W   W   W  O     O  RRRRR   D   D   EEEEE     X X
W W   W W  O     O  R   R   D   D   E        X   X
WW     WW   OOOOO   R    R  DDDD    EEEEE   X     X
""")
# WORDEX ASCII Sanatı Bitişi

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value) and not attribute.startswith('__'):
        servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print_ascii()
    print(f"""
Sms: {len(servisler_sms)}           by @Wordex

1- SMS Gönder (Normal)

2- SMS Gönder (Turbo)

3- Çıkış

Seçim: """, end="")

    try:
        menu = input()
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        # Normal SMS gönderme işlemi
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []

        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: " + Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                sleep(3)
                continue

        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, end="")
        mail = input()
        if mail != "" and ("@" not in mail or ".com" not in mail):
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun? (Sonsuz için 'enter' tuşuna basınız): " + Fore.LIGHTGREEN_EX, end="")
        kere = input()
        if kere == "":
            kere = None
        else:
            try:
                kere = int(kere)
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
                sleep(3)
                continue

        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.LIGHTGREEN_EX, end="")
        try:
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")

        if kere is None:
            # Sonsuz döngü
            for tel in tel_liste:
                sms = SendSms(tel, mail)
                while True:
                    for fonk in servisler_sms:
                        exec(f"sms.{fonk}()")
                        sleep(aralik)
        else:
            for tel in tel_liste:
                sms = SendSms(tel, mail)
                while sms.adet < kere:
                    for fonk in servisler_sms:
                        if sms.adet >= kere:
                            break
                        exec(f"sms.{fonk}()")
                        sleep(aralik)

        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        # Turbo SMS gönderme işlemi
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX, end="")
        tel_no = input()

        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.LIGHTGREEN_EX, end="")
        mail = input()
        if mail != "" and ("@" not in mail or ".com" not in mail):
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()

        def Turbo():
            while not dur.is_set():
                thread_list = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread_list.append(t)
                    t.start()
                for t in thread_list:
                    t.join()

        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
    else:
        print(Fore.LIGHTRED_EX + "Geçersiz seçim, tekrar deneyin.")
        sleep(2)
        