import modul_edit

user_id = input("Silakan masukkan nama Anda: ")
print(f'Halo {user_id}!')
trnsct_123 = modul_edit.Transaction()


def add_item():
    item_name = input("Masukkan nama item: ").lower()
    item_quantity = int(input("Masukkan jumlah item: "))
    item_price = int(input("Masukkan harga item: "))
    trnsct_123.add_item((item_name, item_quantity, item_price))
    print("Item yang dibeli adalah:")
    trnsct_123.show_transaction()
    menu()


def update_name_item():
    item_index = int(input("Masukkan nomor item yang akan diubah: "))
    new_name = input("Masukkan nama item baru: ").lower()
    trnsct_123.update_item_name(trnsct_123.items[item_index - 1][0], new_name)
    menu()


def update_quantity_item():
    item_index = int(input("Masukkan nomor item yang akan diubah: "))
    new_quantity = int(input("Masukkan jumlah item baru: "))
    trnsct_123.update_item_qty(trnsct_123.items[item_index - 1][0], new_quantity)
    menu()


def update_price_item():
    item_index = int(input("Masukkan nomor item yang akan diubah: "))
    new_price = int(input("Masukkan harga item baru: "))
    trnsct_123.update_item_price(trnsct_123.items[item_index - 1][0], new_price)
    menu()


def delete_item():
    item_index = int(input("Masukkan nomor item yang akan dihapus: "))
    trnsct_123.delete_item(trnsct_123.items[item_index - 1][0])
    trnsct_123.show_transaction()
    menu()


def reset_transaction():
    trnsct_123.reset_transaction()
    print("Semua item berhasil didelete!")
    menu()


def check_order():
    trnsct_123.check_order()
    menu()


def show_transaction():
    trnsct_123.show_transaction()
    menu()


def total_price():
    print("Item yang dibeli adalah:")
    trnsct_123.show_transaction()
    trnsct_123.total_price()
    menu()


def menu():
    print("""
    1. Add Item
    2. Update Item Name
    3. Update Item Quantity
    4. Update Item Price
    5. Delete Item
    6. Reset Transaction
    7. Check Order
    8. Total Price
    """)

    while True:
        fitur = input("Pilih menu yang ingin dipilih: ")
        if fitur.isdigit() and 1 <= int(fitur) <= 8:
            fitur = int(fitur)
            break
        print("Masukkan angka dari 1 hingga 8")

    if fitur == 1:
        add_item()

    elif fitur == 2:
        update_name_item()

    elif fitur == 3:
        update_quantity_item()

    elif fitur == 4:
        update_price_item()

    elif fitur == 5:
        delete_item()

    elif fitur == 6:
        reset_transaction()

    elif fitur == 7:
        check_order()

    elif fitur == 8:
        total_price()


menu()
