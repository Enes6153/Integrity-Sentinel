import hashlib
import timecd
import os

def calculate_hash(file_path):
    """
    Dosyanın SHA-256 parmak izini (Hash) hesaplar.
    Dosyada tek bir nokta değişse bile bu değer tamamen değişir.
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Dosyayı parça parça oku (Büyük dosyalar için hafıza dostu)
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def main():
    print("###########################################")
    print("#    INTEGRITY SENTINEL - FIM TOOL        #")
    print("#    (SHA-256 Dosya Bütünlük Takibi)      #")
    print("###########################################")
    
    # Takip edilecek dosyayı sor
    target_file = input("\n[?] Takip edilecek dosya adı (Örn: banka_verisi.txt): ")
    
    # 1. Dosya var mı kontrol et
    if not os.path.exists(target_file):
        print(f"[!] HATA: '{target_file}' dosyası bulunamadı! Önce dosyayı oluşturun.")
        return

    # 2. İlk referans (Baseline) Hash'ini al
    print("[*] Referans parmak izi hesaplanıyor...")
    baseline_hash = calculate_hash(target_file)
    print(f"[+] HEDEF KİLİTLENDİ. Orijinal Hash:\n    {baseline_hash}")
    print("\n[*] Nöbet modu AKTİF. Değişiklik bekleniyor... (Durdurmak için CTRL+C)")

    # 3. Sonsuz döngüde sürekli kontrol et
    try:
        while True:
            time.sleep(2) # 2 saniye bekle
            
            current_hash = calculate_hash(target_file)
            
            # Dosya silindiyse
            if current_hash is None:
                print(f"\n[!!!] ALARM: Dosya SİLİNDİ veya erişilemiyor!")
                break
            
            # Hash değiştiyse (Biri dosyayı değiştirdi!)
            if current_hash != baseline_hash:
                print(f"\n[!!!] ALARM: DOSYA DEĞİŞİKLİĞİ TESPİT EDİLDİ!")
                print(f"[ Eski Parmak İzi ]: {baseline_hash}")
                print(f"[ Yeni Parmak İzi ]: {current_hash}")
                
                # Yeni hash'i artık normal kabul et ve takibe devam et
                baseline_hash = current_hash
                print("[*] Yeni durum kaydedildi, izlemeye devam ediliyor...")
                
    except KeyboardInterrupt:
        print("\n\n[-] İzleme durduruldu.")

if __name__ == "__main__":
    main()
