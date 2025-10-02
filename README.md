# eshop-pbp

## Tautan Deploy PWS
Aplikasi sudah di-deploy di PWS, dapat diakses melalui:  
[https://johannes-nichola-eshoppbp.pbp.cs.ui.ac.id/]

---

## TUGAS 1
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

## TUGAS 1
## Implementasi Checklist Step-by-Step

1. **Data Delivery diperlukan dalam Pengimplementasian Sebuah Platfom**
    Data delivery diperlukan agar data dari server dapat dikirim ke client (misal browser atau aplikasi mobile) dengan cara yang terstruktur dan mudah diolah. Tanpa data delivery yang baik, platform tidak bisa menampilkan informasi secara real-time, konsisten, atau aman. Data delivery juga memungkinkan integrasi antar sistem dan mendukung API, sehingga data bisa digunakan di berbagai front-end atau layanan lain.

2. **XML dan JSON: JSON Lebih Populer**
    Menurut saya, JSON lebih baik dari XML, dan tentu JSON lebih populer bukan tanpa alasan. Terdapat beberapa hal yang membuat JSON lebih populer, diantaranya JSON lebih ringan (ukurannya lebih kecil dan lebih cepat dikirim dibandingkan dengan XML). Selain itu, syntax yang lebih sederhana menjadi alasan utama bagi saya mengapa JSON lebih populer (JSON lebih mudah dibaca manusia dan bisa langsung digunakan di JS). JSON pun didukung hampir semua bahasa pemrograman modern (high level).

3. **Fungsi method is_valid() pada form Django**
    is_valid() adalah method untuk memeriksa apakah data yang dikirim oleh user memenuhi aturan validasi form (return boolean). Validasi ini diperlukan agar data yang akan tersimpan di database valid dan aman. Selain itu, dapat membantu user dengan memberi feedback error jika ada data yang salah/tidak lengkap.

4. **Pentingnya csrf_token dalam membuat form di Django**
    csrf_token digunakan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Artinya, dengan csrf_token, server dapat memverifikasi request yang masuk ke aplikasi kita berasal dari situs resmi, sehingga penyerang (user tidak bertanggung jawab) tidak dapat memanipulasi data/aksi tidak sah (membuat form palsu di situs lain dan request tanpa sepengetahuan user asli (user yang benar benar ingin menggunakan aplikasi kita)).

5. **Step-by-step melanjutkan proyek Django**
    1. Melanjutkan proyek Django (eshop-pbp) yang sudah dibuat sebelumnya.
    2. Menambahkan fungsi create_products() dan show_products() untuk membuat produk baru dan menampilkan detail produk, kemudian tambahkan path URL dalam variabel urlpatterns pada file urls.py.
    3. Membuat halaman (main.html) yang menampilkan data objek dengan tombol "+ Add Products" yang redirect ke halaman form (create_products.html) dan tombol "Detail" di setiap produk untuk menampilkan detail produk (products_detail.html).
    4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya (models.py -> forms.py -> views.py -> create_products.html). File models.py untuk bagan data, forms.py untuk data apa yang akan dimintai input dari user, views.py menghubungkan data amodels.py untuk ditampilkan melalui create_products.html.
    5. Membuat halaman yang menampilkan detail dari setiap data objek model (models.py -> views.py -> products_detail.html). File models.py untuk bagan data, views.py menghubungkan data pada database berbentuk models.py untuk ditampilkan melalui products_detail.html.
    6. Menambahkan 4 fungsi views (show_xml(), show_json(), show_xml_by_id(), show_json_by_id()) sebagai method untuk menampilkan data dari models.py. Tidak lupa untuk menambahkan path URL ke dalam variabel urlpatterns keempat fungsi tersebut yang telah diimport dari views.py ke urls.py
    7. Gunakan Postman sebagai Data Viewer

6. **Feedback untuk asisten dosen**
    Bagi saya, apa yang disampaikan dan dijelaskan asisten dosen sudah cukup baik. Ketika ada pertanyaan pun asisten dosen dapat dengan baik menjelaskan dan asisten dosen juga tidak asal menjawab jika belum mengerti. Saya rasa, performa asisten dosen sudah cukup baik.

## Screenshot hasil akses URL pada Postman
![alt text](images/xml.png)
![alt text](images/json.png)
