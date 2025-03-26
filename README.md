# TharMon - Tharsis Monitor - System for monitoring capsule sensors and environmental data.

**TharMon**, kapsül ve ortam verilerini izleyen bir sistemdir. Bu Python tabanlı yazılım, uçuş sırasında kapsül içi ve çevresel verileri (sıcaklık, basınç, batarya durumu, yakıt tankları durumu vb.) toplayarak uçuş bilgisayarına iletilmesini sağlar. Bu sistem, uçuş güvenliğini izlemek ve yönetmek için kritik verileri takip eder.

## Kullanım Talimatları

### Gereksinimler

Proje Python 3 ile çalışacak şekilde geliştirilmiştir. Sisteminize Python 3'ün yüklü olduğundan emin olun. Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu kullanabilirsiniz:


```bash
pip install -r requirements.txt
```
### Çalıştırma
Projeyi çalıştırmak için aşağıdaki komutu kullanabilirsiniz:
```bash
python3 main.py

```
Bu komut, projenin tüm modüllerini yükler ve çalıştırır. Sistem, ortam verileri, batarya durumu, yakıt seviyesi gibi bilgileri toplar ve uçuş kontrol sistemine iletir.

### Dosya Yapısı
Proje dosya yapısı şu şekilde olacaktır:
```bash
├── ambient.py      # Ortam sıcaklığı ve basınç verilerini toplar
├── battery.py      # Batarya durumu ile ilgili verileri yönetir
├── fuel.py         # Yakıt tanklarının durumunu kontrol eder
├── timer.py        # Zamanlayıcı fonksiyonlarını yönetir
└── main.py         # Ana çalışma dosyası
```
### İletişim

Herhangi bir sorunuz veya öneriniz varsa, aşağıdaki linki kullanabilirsiniz.
- **GitHub Issues**: [https://github.com/evirgenfurkan/tharmon/issues](https://github.com/kullaniciadi/tharmon/issues)
