from unittest import result
from colorama import Cursor
import mysql.connector
import os

db = mysql.connector.connect(host = "localhost", user = "root", passwd = "pusbangdisini26", database = "uas_basdat")

def inputData(db):
    Logistic_id = input("ID Pengiriman : ")
    Tanggal_Pengiriman = input("Tanggal : ")
    Jenis_Pengiriman = input("Jenis Pengiriman : ")
    Status = input("Status Pengiriman : ")
    Jalur_Pengiriman = input("Jalur Pengiriman : ")
    Jenis_Barang = input("Jenis Barang : ")
    Asal_Pengiriman = input("Asal : ") 
    Tujuan_Pengiriman = input("Kota Tujuan : ")
    val = (Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman)
    cursor = db.cursor()
    sql = "INSERT INTO data_logistik (Logistic_id, Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{}Data telah disimpan!".format(cursor.rowcount))

def showData(db):
    cursor = db.cursor()
    sql = "SELECT * FROM data_logistik"
    cursor. execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Belum ada data yang tercatat!")
    else:
        for data in results:
            print(data)

def updateData(db):
    cursor = db.cursor()
    showData(db)
    Logistic_id = input ("ID Pengiriman : ")

    Tanggal_Pengiriman = input("Tanggal : ")
    Jenis_Pengiriman = input("Jenis Pengiriman : ")
    Status = input("Status Pengiriman : ")
    Jalur_Pengiriman = input("Jalur Pengiriman : ")
    Jenis_Barang = input("Jenis Barang : ")
    Asal_Pengiriman = input("Asal : ") 
    Tujuan_Pengiriman = input("Kota Tujuan : ")
    
    sql = "UPDATE data_logistik SET Tanggal_Pengiriman = %s, Jenis_Pengiriman = %s, Status = %s, Jalur_Pengiriman = %s, Jenis_Barang = %s, Asal_Pengiriman = %s, Tujuan_Pengiriman = %s WHERE Logistic_id = %s"
    val = (Tanggal_Pengiriman, Jenis_Pengiriman, Status, Jalur_Pengiriman, Jenis_Barang, Asal_Pengiriman, Tujuan_Pengiriman, Logistic_id)
    cursor.execute(sql, val)
    db.commit()
    print("{}Data telah terupdate!". format(cursor.rowcount))

def deleteData(db):
    cursor = db.cursor()
    showData(db)
    keyword = input("ID Pengiriman : ")
    cursor.execute("DELETE FROM data_logistik WHERE Logistic_id = %(keyword)s", {'keyword' : keyword})
    db.commit()
    print("{}Data telah dihapus!".format(cursor.rowcount))

def searchData(db):
    cursor = db.cursor()
    keyword = input("Keyword : ")
    cursor.execute("SELECT * FROM data_logistik WHERE Logistic_id LIKE  %(keyword)s", {'keyword' : keyword})
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Belum ada data!")
    else:
        for data in results:
            print(data)


def menuUtama(db):
    print("=== PASTI SAMPAI EXPRESS ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")


    menu = input("Pilih menu> ")
    os.system("cls")
    
    if menu == "1":
        inputData(db)
    elif menu == "2":
        showData(db)
    elif menu == "3":
        updateData(db)
    elif menu == "4":
        deleteData(db)
    elif menu == "5":
        searchData(db)
    elif menu == "0":
        exit()
    else:
        print("Salah!")

if __name__ == "__main__":
  while(True):
    menuUtama(db)