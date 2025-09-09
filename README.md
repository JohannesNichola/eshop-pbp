# eshop-pbp

## Tautan Deploy PWS
Aplikasi sudah di-deploy di PWS, dapat diakses melalui:  
[https://johannes-nichola-eshoppbp.pbp.cs.ui.ac.id/]

---

## Implementasi Checklist Step-by-Step

1. **Step-by-step membuat proyek Django baru**
    1. Buat proyek Django baru dengan code django-admin startproject eshop_pbp lalu masuk ke folder project.
    2. Buat aplikasi main dengan code python manage.py startapp main.
    3. Atur routing di eshop_pbp/urls.py dengan menambahkan path("", include("main.urls")).
    4. Buat model Product (class) pada main models.py sesuai atribut yang telah ditentukan.
    5. Migrasi database dengan code python manage.py makemigrations kemudian python manage.py migrate.
    6. Buat fungsi view (def show_main(request)) pada main/views.py yang akan melakukan render template main.html dengan data Product.
    7. Routing aplikasi dengan mengarahkan path ke fungsi view di main/urls.py.
    8. Buat template pada main.html untuk menampilkan data Product dengan sintaks {% for p in products %}.
    9. Finishing, push ke repo, dan jalankan deploy melalui PWS.

2. **Bagan request client ke web aplikasi berbasis Django** 
    Client (Browser)
        |
        | HTTP Request ((GET /) atau (/products))
        v
    urls.py (Routing)
        |
        | Pemetaan URL ke fungsi/view tertentu
        v
    views.py (Logic)
        |
        | Ambil data dari models.py (database) jika perlu
        v
    models.py (Database)
        |
        | Query/Manipulasi data
        v
    views.py
        |
        | Kirim data ke template
        v
    Template HTML (main.html)
        |
        | Render data menjadi HTML
        v
    Client (Browser)
        |
        | HTTP Response (HTML page)

3. **Peran settings.py dalam proyek Django**
    settings.py digunakan untuk mengontrol seluruh perilaku *project* mulai dari konfigurasi dasar (SECRET_KEY, DEBUG, ALLOWED_HOSTS), database (DATABASES), aplikasi yang aktif (INSTALLED_APPS), template (TEMPLATES), keamanan, hingga deployment. Tanpa adanya settings.py, Django tidak mengerti bagaimana cara menjalankan *project* yang dibuat.

4. **Cara kerja migrasi database di Django**
    Migrasi database di Django dilakukan dengan cara Django menerjemahkan model Python menjadi tabel di database. Proses dimulai ketika kita menuliskan model di models.py berisi field dan tipe datanya. Kemudian, Django membuat file migrasi (python manage.py makemigrations). Selanjutnya, Django membaca file migrasi dan menjalankan SQL agar sesuai tabel database (python manage.py migrate). Terakhir, setiap migrasi akan dicatat agar tidak berulang.

5. **Alasan Django dijadikan permulaan pembelajaran pengembangan perangkat lunak**
    Django merupakan full-stack framework yang sudah menyediakan semua komponen utama web (routing, model/database, views, template, admin), sehingga pemula bisa fokus memahami arsitektur MVT tanpa harus menggabungkan banyak tools. Struktur proyeknya jelas, interaksi database yang mudah, dan dokumentasinya lengkap, membuat Django ideal sebagai langkah pertama belajar pengembangan perangkat lunak.

6. **Feedback untuk asisten dosen**
    Bagi saya, apa yang disampaikan dan dijelaskan asisten dosen sudah cukup baik. Ketika ada pertanyaan pun asisten dosen dapat dengan baik menjelaskan dan asisten dosen juga tidak asal menjawab jika belum mengerti. Saya rasa, performa asisten dosen sudah cukup baik.