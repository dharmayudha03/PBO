import mysql.connector
import os

db = mysql.connector.connect(
    host = 'localhsot',
    user = 'root',
    passwd = '',
    database = 'pbo'
)

def insert_data(db):
    name = input('Masukkan nama: ')
    alamat = input('Masukkan Alamat: ')
    val = (name, alamat)
    cursor = db.cursor()
    sql = "INSERT INTO customers (name, alamat) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    if cursor.rowcount < 0:
        print('Tidak ada data')
    else:
        for data in results:
            print(data)

def update_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input('Pilih id Customer: ')
    name = input('Nama baru: ')
    alamat = input('Alamat baru: ')

    sql = "UPDATE customers SET name = %s, alamat = %s WHERE customer_id = %s"
    val = (name, alamat, customer_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dirubah".format(cursor.rowcount))

def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    customer_id = input('Pilih id customer: ')
    sql = "DELETE FORM customers WHERE customer_id = %s"
    val = (customer_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM customers WHERE name LIKE %s OR alamat LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tida ada data")
    else:
        for data in results:
            print(data)

def show_menu(db):
    print("=== APLIKASI DATABASE PBO ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("-----------------------")
    menu = input("Pilih Menu: ")

    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Pilihan adan tidak ada")

if __name__ == "__main__":
    while(True):
        show_data(db)


