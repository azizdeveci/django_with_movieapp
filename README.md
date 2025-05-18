# Film Uygulaması

Bu proje, Django web framework'ü kullanılarak geliştirilmiş bir film uygulamasıdır.

## Özellikler

- Ana sayfa görüntüleme
- Film listesi görüntüleme
- Film detaylarını görüntüleme
- Film ID'sine göre detay sayfası

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [proje-url]
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Veritabanı migrasyonlarını yapın:
```bash
python manage.py migrate
```

4. Sunucuyu başlatın:
```bash
python manage.py runserver
```

## Kullanım

Uygulama aşağıdaki URL'ler üzerinden erişilebilir:

- Ana Sayfa: `http://127.0.0.1:8000/` veya `http://127.0.0.1:8000/home`
- Film Listesi: `http://127.0.0.1:8000/movies`
- Film Detayları: `http://127.0.0.1:8000/movies/<film_id>`

## Teknolojiler

- Python
- Django
- HTML/CSS
- SQLite (varsayılan veritabanı)

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun


![Uygulama Ekran Görüntüsü](https://github.com/azizdeveci/django_with_movieapp/blob/django_with_movieapp/movies/static/img/ss.jpg) 
