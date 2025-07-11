# WordexChecker
# enough reborn kodlarından yararlanılmıştır
from colorama import Fore, Style, init
from time import sleep
from os import system
from sms import SendSms
import threading

init(autoreset=True)  # Renklerin kalıcı olmaması için

# WORDEX ASCII Sanatı Başlangıcı
print(Fore.YELLOW + """
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
    if callable(attribute_value):
        if not attribute.startswith('__'):
            servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print(Fore.YELLOW + """
W       W   OOOOO   RRRRR   DDDD    EEEEE   X     X
W       W  O     O  R    R  D   D   E        X   X
W   W   W  O     O  RRRRR   D   D   EEEEE     X X
W W   W W  O     O  R   R   D   D   E        X   X
WW     WW   OOOOO   R    R  DDDD    EEEEE   X     X

""" + Fore.GREEN + f"Sms: {len(servisler_sms)}           by @Wordex\n\n" +
Fore.GREEN +
"1- SMS Gönder (Normal)\n\n" +
"2- SMS Gönder (Turbo)\n\n" +
"3- Çıkış\n\n" +
Fore.YELLOW + "Seçim: ", end="")

    try:
        menu = input()
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.RED + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        # 1. seçeneğin işlemleri
        system("cls||clear")
        print(Fore.GREEN + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): " + Fore.YELLOW, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.GREEN + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: " + Fore.YELLOW, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.RED + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
            sonsuz = ""
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.RED + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(Fore.GREEN + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.YELLOW, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.RED + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.GREEN + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: " + Fore.YELLOW, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.RED + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.GREEN + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.YELLOW, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.RED + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        if kere is None:
            while True:
                for i in tel_liste:
                    sms = SendSms(i, mail)
                    for attribute in servisler_sms:
                        getattr(sms, attribute)()
                        sleep(aralik)
        else:
            for i in tel_liste:
                sms = SendSms(i, mail)
                while sms.adet < kere:
                    for attribute in servisler_sms:
                        if sms.adet >= kere:
                            break
                        getattr(sms, attribute)()
                        sleep(aralik)

        print(Fore.RED + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 2:
        # Turbo seçeneği
        system("cls||clear")
        print(Fore.GREEN + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.YELLOW, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.RED + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.GREEN + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.YELLOW, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.RED + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()

        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()

        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print(Fore.RED + "\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(Fore.RED + "Çıkış yapılıyor...")
        break

    else:
        print(Fore.RED + "Geçersiz seçim, tekrar deneyin.")
        sleep(2)
