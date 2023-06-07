# Cashier

LATAR BELAKANG

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi berencana untuk melakukan perbaikan proses bisnis dengan membuat sistem kasir self-service dimana customer bisa langsung memasukkan jenis item, jumlah item, dan harga item yang dibeli dan fitur-fitur lainnya. Selain itu, customer yang tidak berada di kota tersebut bisa membeli barang di supermarket Andi.

REQUIREMENT ATAU OBJECTIVES

Fungsi dalam sistem kasir self-service meliputi:
Customer membuat ID transaksi customer: trnsct_123 = transaction()
Customer menambahkan nama item, jumlah item, dan harga item yang dibeli: add_item([<nama item>, <jumlah item>, <harga per item>])
Jika customer salah menambahkan item yang dibeli, customer bisa update:
Nama item: update_item_name(<nama item>, <update nama item>)
Jumlah item: update_item_qty(<nama_item>, <update jumlah item>)
Harga item: update_item_price(<nama_item>, <update harga item>)
Jika customer batal membeli,
Customer bisa menghapus salah satu item pesanan: delete_item(<nama item>)
Customer bisa menghapus seluruh item pesanan: reset_transaction()
Jika sudah selesai input, customer bisa mengecek daftar item pesanan yang sudah ditambahkan: check_order(). Dengan ketentuan:
Jika tidak ada kesalahan input, maka keluar pesan “Pemesanan sudah benar”
Jika terjadi kesalahan input, maka keluar pesan “Terdapat kesalahan input data”
Lalu mengeluarkan fungsi output pesanan yang sudah dibeli
Jika sudah mengecek, customer bisa menghitung total pesanan yang dibeli: total_price(). Dengan ketentuan:
Jika total belanja > Rp200.000, makan dapat diskon 5%
Jika total belanja > Rp300.000, makan dapat diskon 8%
Jika total belanja > Rp500.000, makan dapat diskon 10%


Alur program atau flowchart:
