# Cashier

## I. LATAR BELAKANG

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi berencana untuk melakukan perbaikan proses bisnis dengan membuat sistem kasir self-service dimana customer bisa langsung memasukkan jenis item, jumlah item, dan harga item yang dibeli dan fitur-fitur lainnya. Selain itu, customer yang tidak berada di kota tersebut bisa membeli barang di supermarket Andi.

## II. REQUIREMENT ATAU OBJECTIVES

### A. Fungsi dalam sistem kasir self-service meliputi:
1. Customer membuat ID transaksi customer: `trnsct_123 = transaction()`

2. Customer menambahkan nama item, jumlah item, dan harga item yang dibeli: 
`add_item([<nama item>`, `<jumlah item>`, `<harga per item>])`

3. Jika customer salah menambahkan item yang dibeli, customer bisa update:
- Nama item: `update_item_name(<nama item>, <update nama item>)`
- Jumlah item: `update_item_qty(<nama_item>, <update jumlah item>)`
- Harga item: `update_item_price(<nama_item>, <update harga item>)`

4. Jika customer batal membeli,
- Customer bisa menghapus salah satu item pesanan: `delete_item(<nama item>)`
- Customer bisa menghapus seluruh item pesanan: `reset_transaction()`

5. Jika sudah selesai input, customer bisa mengecek daftar item pesanan yang sudah ditambahkan: `check_order()`
Dengan ketentuan:
- Jika tidak ada kesalahan input, maka keluar pesan “Pemesanan sudah benar”
- Jika terjadi kesalahan input, maka keluar pesan “Terdapat kesalahan input data”
- Lalu mengeluarkan fungsi output pesanan yang sudah dibeli

6. Jika sudah mengecek, customer bisa menghitung total pesanan yang dibeli: `total_price()`. Dengan ketentuan:
- Jika total belanja > Rp200.000, makan dapat diskon 5%
- Jika total belanja > Rp300.000, makan dapat diskon 8%
- Jika total belanja > Rp500.000, makan dapat diskon 10%


### B. Alur program atau flowchart:

## III. FUNCTIONS
Semua fungsi terdapat di dalam class Transaction
- Method `add_item`: Fungsi tambah item pesanan baru ke dictionary
- Method `update_item_name`: Fungsi mengubah nama item pesanan
- Method `update_item_qty`: Fungsi ini untuk mengubah jumlah item pesanan
- Method `update_item_price`: Fungsi ini untuk mengubah harga item pesanan
- Method `delete_item`: Fungsi ini untuk menghapus salah satu item pesanan
- Method `reset_transaction`: Fungsi ini untuk menghapus seluruh item pesanan atau reset transaksi
- Method `check_order`: Fungsi ini untuk mengecek daftar item pesanan yang sudah ditambahkan dan memanggil method show_transaction
- Method `show_transaction`: Fungsi ini untuk menampilkan daftar seluruh item pesanan
- Method `total_price`: Fungsi ini untuk menghitung total pesanan yang dibeli, total diskon, dan total bayar

