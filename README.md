# Integrity Sentinel 🛡️ (File Integrity Monitor)

Bu proje, kritik sistem dosyalarında yetkisiz değişiklikleri tespit etmek için geliştirilmiş bir **Siber Savunma (Blue Team)** aracıdır.

## 🚀 Nasıl Çalışır?
Python ve **SHA-256 Hashing** algoritmasını kullanarak hedef dosyanın dijital parmak izini (Hash) çıkarır. Arka planda çalışan servis, dosyanın bütünlüğünü sürekli kontrol eder ve herhangi bir bayt değişikliğinde (Data Corruption / Tampering) alarm verir.

## 🔑 Teknik Detaylar
* **Algoritma:** SHA-256 (Secure Hash Algorithm 256-bit)
* **Kullanım Alanı:** Malware tespiti, Konfigürasyon takibi, Log güvenliği.
* **Dil:** Python 3 (Standart kütüphaneler: hashlib, os, time)

## 🛠️ Kurulum
```bash
git clone https://github.com/Enes6153/Integrity-Sentinel.git
python fim_tool.py
