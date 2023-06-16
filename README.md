## README.md

Ini adalah repository GitHub yang berisi proyek Python untuk menambahkan pengguna ke suatu domain menggunakan API. Proyek ini terdiri dari beberapa file Python dan menggunakan pustaka-pustaka berikut:

- `time`: Modul yang menyediakan berbagai fungsi terkait waktu.
- `requests_toolbelt.multipart.encoder`: Pustaka untuk mengenkripsi data dalam format multipart.
- `requests`: Pustaka untuk mengirim permintaan HTTP.
- `json`: Modul untuk bekerja dengan format JSON.
- `datetime`: Modul untuk bekerja dengan data dan waktu.
- `logging`: Modul untuk pencatatan (logging) aplikasi.

### Langkah-langkah
Berikut adalah langkah-langkah untuk menjalankan proyek ini:

1. Pastikan Anda memiliki semua pustaka yang diperlukan yang tercantum di atas terinstal di lingkungan Python Anda.

2. Unduh semua file proyek Python dari repository GitHub ini.

3. Pastikan Anda memiliki file `example.txt` yang berisi informasi pengguna yang akan ditambahkan ke domain. File ini harus memiliki format yang sesuai dengan yang diharapkan oleh fungsi `getAllUsers()`.

4. Buka file `main.py` dan lakukan pengaturan yang diperlukan, seperti mengubah nilai `domain`, `username`, dan `password`. Anda juga dapat mengatur token akses jika Anda memiliki token yang valid.

5. Jalankan file `main.py` menggunakan lingkungan Python Anda. Hasilnya akan dicatat dalam file log `log.txt`, yang akan berisi informasi tentang pengguna yang berhasil ditambahkan dan pesan kesalahan jika terjadi.

6. Setelah menjalankan proyek, Anda dapat melihat log di file `log.txt` untuk mengetahui hasilnya.

Catatan: Pastikan untuk memahami kode dan memodifikasinya sesuai kebutuhan Anda sebelum menjalankannya.