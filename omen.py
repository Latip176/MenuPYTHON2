#!usr/bin/python
from random import random
from random import randint

print "-------------------------------"
print "Hallo Selamat Datang Di Menu Python2 By OmenDev"
print "-------------------------------"

print ""
nama = raw_input("Silahkan Masukan Nama Anda |>---> ")
print ""

print "-------------------------------"
print "Hallo,", nama, "Selamat Datang Di Menu "
print ""
print "List Fitur:"
print "1. Calculator OmenDev"
print "2. Menanyakan Nama Anda"
print "3. Siapa Pembuat Menu Ini"
print "4. Random Angka, Bisa Set Angkanya Jika Anda Memerintahkan Ini"
print ""
print "-------------------------------"
print ""
perintah = int(raw_input("Pilih Perintah Dengan Angka |>---> "))
print ""

if(perintah==1):
  print ""
  print "Hallo", nama, "Selamat Datang Di Calculator Python By OmenDev"
  print ""
  print "Cara Menggunakan : "
  print "Masukan Angka Pertama, Contoh 5"
  print "Operator, List Operator : + = tambah, * = kali, - = kurang, : = bagi."
  print "Masukan Angka Kedua Contoh 5"
  print ""
  
  angka1 = int(raw_input("Masukan Angka Pertama |>---> "))
  operator = raw_input("Operator |>---> ")
  angka2 = int(raw_input("Masukan Angka Kedua |>---> "))
  
  print ""
  
  if(operator=="+" or operator=="*" or operator=="-" or operator==":"):
    if(operator=="+"):
      print "Pertambahan", angka1, operator, angka2, "=", angka1 + angka2
      print ""
    if(operator=="*"):
      print "Perkalian", angka1, operator, angka2, "=", angka1 * angka2
      print ""
    if(operator=="-"):
      print "Pengurangan", angka1, operator, angka2, "=", angka1 - angka2
      print ""
    if(operator==":"):
      print "Pembagian", angka1, operator, angka2, "=", angka1 / angka2
      print ""
      
  else:
      print "Ada Yang Salah!!"
      
if(perintah==2):
  print "-------------------------------"
  print "Saya Buka Peramal Tapi Nama Anda Adalah : ", nama
  print "-------------------------------"
if(perintah==3):
  print "-------------------------------"
  print "Pembuat : OmenDeveloper "
  print "-------------------------------"
if(perintah==4):
  print ""
  print "Hello", nama, "Selamat Datang Di Random Angka By OmenDev"
  print ""
  print "Cara Penggunaan :"
  print "Angka Minimal : Contoh 1"
  print "Angka Maksimal : Contoh 10"
  print "Berarti 1 Sampai 10 Yang Akan Keluar Random"
  print ""
  
  minangka = int(raw_input("Minimal Angka |>---> "))
  makangka = int(raw_input("Maksimal Angka |>---> "))
  random = randint(minangka, makangka)
  
  print "-------------------------------"
  print "Minimal Angka : ", minangka
  print "Maksimal Angka :", makangka
  print "Random :", random
  print "-------------------------------"
