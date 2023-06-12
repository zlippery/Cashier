# Class Transaction
class Transaction:
    '''Menginisialisasi atribut ke dalam class
    Atribut: item dan total'''
    def __init__(self):
        '''Pendefinisian atribut dengan method init'''
        self.items = []
        self.total = 0

    # Method add_item
    def add_item(self, item):
        '''Fungsi tambah item pesanan baru ke dictionary'''
        self.items.append(item)
        self.total += item[1] * item[2]

    # Method update_item_name
    def update_item_name(self, old_name, new_name):
        '''Fungsi mengubah nama item pesanan
        Objek:
        old_name: nama item lama
        new_name: nama item baru'''
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name.capitalize()
                break

    # Method update_item_qty
    def update_item_qty(self, name, qty):
        '''Fungsi ini untuk mengubah jumlah item pesanan
        Objek:
        name: nama item
        qty: jumlah item baru'''
        for item in self.items:
            if item[0] == name:
                old_qty = item[1]
                item[1] = qty
                self.total += (qty - old_qty) * item[2]
                break

    # Method update_item_price
    def update_item_price(self, name, price):
        '''Fungsi ini untuk mengubah harga item pesanan
        Objek:
        name: nama item
        price: harga baru'''
        for item in self.items:
            if item[0] == name:
                old_price = item[2]
                item[2] = price
                self.total += (price - old_price) * item[1]
                break

    # Method delete_item
    def delete_item(self, name):
        '''Fungsi ini untuk menghapus salah satu item pesanan'''
        for item in self.items:
            if item[0] == name:
                self.total -= item[1] * item[2]
                self.items.remove(item)
                break

    # Method reset_transaction
    def reset_transaction(self):
        '''Fungsi ini untuk menghapus seluruh item pesanan atau reset transaksi'''
        self.items = []
        self.total = 0

    # Method check_order
    def check_order(self):
        '''Fungsi ini untuk mengecek daftar item pesanan yang sudah ditambahkan
        dan memanggil method show_transaction'''
        if not self.items:
            print("Tidak ada item dalam pesanan")
            return False
        for item in self.items:
            if len(item) != 3:
                print("Terdapat kesalahan input data")
                return False
        print("Pemesanan sudah benar")
        self.show_transaction()

    # Method show_transaction
    def show_transaction(self):
        '''Fungsi ini untuk menampilkan daftar
        seluruh item pesanan

        Output:
        nomor, nama item, jumlah item, harga item, dan total harga item
        '''
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        print("|----|-----------|-------------|------------|-------------|")
        for i, item in enumerate(self.items):
            print(f"| {i+1:<2} | {item[0]:<9} | {item[1]:^11} | {item[2]:^10} | {item[1]*item[2]:^11} |")

    # Method total_price
    def total_price(self):
        '''Fungsi ini untuk menghitung total pesanan yang dibeli,
        total diskon, dan total bayar

        Parameter:
        Pesanan kurang dari Rp200.000, tidak dapat diskon
        Pesanan lebih dari Rp200.000, diskon 5%
        Pesanan lebih dari Rp300.000, diskon 8%
        Pesanan lebih dari Rp500.000, diskon 10%
        '''
        if self.total > 500000:
            discount = 0.1
        elif self.total > 300000:
            discount = 0.08
        elif self.total > 200000:
            discount = 0.05
        else:
            discount = 0
        discounted_total = self.total * (1 - discount)
        print(f"Total belanja: {self.total}")
        print(f"Diskon: {discount*100:.0f}%")
        print(f"Total bayar: {discounted_total}")
        return discounted_total
