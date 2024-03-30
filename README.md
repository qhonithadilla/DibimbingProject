# Assignment/Project Data Warehousing MSIB 6
## Repositori ini berisi file pengerjaan Assignment Python 5

Adapun perintah/penugasan terkait file tersebut, yaitu:
1. Buatlah class MarketingDataETL yang memiliki tiga metode:
   - extract(): akan membaca data dari sebuah file CSV (Misalkan, marketing_data.csv)
   - transform(): akan melakukan pembersihan dan transformasi sederhana pada data (seperti mengubah format tanggal atau membersihkan nilai yang kosong)
   - store(): akan menyimpan data yang telah ditransformasi ke dalam struktur data DataFramet.
2. Gunakan inheritance untuk membuat class TargetedMarketingETL yang mewarisi dari MarketingDataETL.
3. Tambahkan metode segment_customers() yang mengelompokkan pelanggan berdasarkan kriteria tertentu (misalnya, pengeluaran total atau kategori produk yang dibeli).
4. Demonstrasi polymorphism dengan meng-override metode transform() dalam TargetedMarketingETL untuk menambahkan logika segmentasi pelanggan ke dalam proses transformasi.
