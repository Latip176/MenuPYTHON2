from random import random
from random import randint
from random import choice
import datetime

garis = "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

def menu():
  print ""
  print "Hallo Selamat Datang Di Menu Python, Ini Adalah Project Yang Dibuat Oleh: Muhammad Latif Harkat Atau Sering Disebut OmenDeveloper, 083870396203 (WhatssApp) Beritahu Jika Ada Bug / Eror"
  print ""
  nama = raw_input("Masukan Nama Anda |>---> ")
  print(garis)
  print ""
  print "Hello,", nama, "Selamat Datang Di Menu Python OmenDev"
  print ""
  print "List Perintah & Fitur : "
  print "1. Calculator"
  print "2. Random Angka, Dan Nama Yang Bisa Anda Set Sendiri!!"
  print "3. Menanyakan Nama Anda"
  print "4. Menanyakan Bot Sedang Apa"
  print "5. No WhatssApp Latip / Omen"
  print "6. Gombalin Aku"
  print "7. Sekarang Tanggal "
  print ""
  print(garis)
  print ""
  perintah = int(raw_input("perintah@latipdev |>---> "))
  if(perintah==1):
    print ""
    print "Calculator V1, Hallo", nama, "Di Calculator"
    print ""
    print "List Operator :"
    print "+ = tambah, - = Kurang, * = Kali, : = Bagi"
    print ""
    angka1 = int(raw_input("Masukan Angka Pertama |>---> "))
    operator = raw_input("Masukan Operator |>---> ")
    angka2= int(raw_input("Masukan Angka Kedua |>---> "))
    if(operator=="+" or operator=="-" or operator=="*" or operator==":"):
      if(operator=="+"):
        print ""
        print "Pertambahan", angka1, operator, angka2, "=", angka1 + angka2
        print ""
      if(operator=="-"):
        print ""
        print "Pengurangan", angka1, operator, angka2, "=", angka1 - angka2
        print ""
      if(operator=="*"):
        print ""
        print "Perkalian", angka1, operator, angka2, "=", angka1 * angka2
        print ""
      if(operator==":"):
        print ""
        print "Pembagian", angka1, operator, angka2, "=", angka1 / angka2
    else:
      print "Ada Yang Salah"
      menu()
  if(perintah==2):
    print ""
    print "Random Angka & Nama V1, Hallo", nama, "Di Random Angka & Nama"
    print ""
    print "Cara Penggunaan Random Angka"
    print "Masukan Angka Minimal"
    print "Masukan Angka Maksimal"
    print "Nanti Akan Muncul Random Angka Yang Tidak Akan Menampilkam Lebih Atau Kurang Dari Angka Minimal Atau Malsimal"
    print ""
    print "Cara Penggunaan Random Nama : "
    print "Masukan Mau Berapa Nama Contoh 3"
    print "Nama 1 : Contoh omen"
    print "Nama 2 : Contoh Mulqi"
    print "Nama 3 : Contoh Astod"
    print "Nanti Akan Ke Random Siapa Yang Akan Tampil Di Dalam Terminal"
    print ""
    print "Pilih Random :"
    print "1. Random Angka"
    print "2. Random Nama"
    print ""
    pilihrandom = int(raw_input("Pilih Random |>---> "))
    if(pilihrandom==1 or pilihrandom==2):
      if(pilihrandom==1):
        print ""
        ranangka1 = int(raw_input("Masukan Angka Minimal |>---> "))
        ranangka2 = int(raw_input("Masukan Angka Maksimal |>---> "))
        randomangka = randint(ranangka1, ranangka2)
        print(garis)
        print "Angka Minimal :", ranangka1
        print "Angka Maksimal :", ranangka2
        print "Random Angka :", randomangka
        print(garis)
    if(pilihrandom==2):
      print ""
      berapanama = int(raw_input("Mau Berapa Nama |>---> "))
      print ""
      berapa2 = 1
      while (berapa2 <= berapanama):
        berapa2 = berapa2 + 1
        name = raw_input("Masukan Nama : ")
        name2 = [name]
        random2 = choice(name2)
      else:
        print ""
        print(garis)
        print "Pemenang Random :", random2
        print(garis)
        print ""
  if(perintah==3):
    print""
    print(garis)
    print "Nama Anda Adalah :", nama
    print(garis)
    print ""
  if(perintah==4):
    print ""
    print(garis)
    sedang1 = "Lagi Gabut", "Pijitin Omen", "Mikirin Kamu", "Lagi Baca Buku", "Lagi Mencari Anda", "Lagi Ngoding", "Lagi Diem"
    sedang2 = choice(sedang1)
    print "Saya Sedang :", sedang2
    print(garis)
    print ""
  if(perintah==5):
    print ""
    print(garis)
    print "Nomer WhatssApp Latip : 083870396203"
    print(garis)
    print ""
  if(perintah==6):
    print ""
    print "Ga Lu Jelek."
    print ""
  if(perintah==7):
    hari_ini = datetime.datetime.now()
    print ""
    print(garis)
    print "Sekarang Tanggal : ", hari_ini
    print ""
    print "Semoga Hari Anda Menyenangkan :)"
    print(garis)
    print ""
      
menu()