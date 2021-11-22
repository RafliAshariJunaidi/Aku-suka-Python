

#mendefinisikan fungsi
def hitung_FPB(x, y):

# memilih bilangan yang paling kecil
if x > y:
smaller = y
else:
smaller = x
for i in range(1, smaller+1):
if((x % i == 0) and (y % i == 0)):
fpb = i

return fpb

num1 = 96
num2 = 24

num1 = int(input(“Masukan bilangan pertama: “))
num2 = int(input(“Masukan bilangan kedua: “))

print(“FPB dari”, num1,”dan”, num2,” =”, hitung_FPB(num1, num2))

Contoh 6: Program kalkulator sederhana
# fungsi penjumlahan
def add(x, y):
return x + y

# fungsi pengurangan
def subtract(x, y):
return x – y

# fungsi perkalian
def multiply(x, y):
return x * y

# fungsi pembagian
def divide(x, y):
return x / y

# menu operasi
print(“Pilih Operasi.”)
print(“1.Jumlah”)
print(“2.Kurang”)
print(“3.Kali”)
print(“4.Bagi”)

# Meminta input dari pengguna
choice = input(“Masukkan pilihan operasi (1/2/3/4): “)

num1 = int(input(“Masukkan bilangan pertama: “))
num2 = int(input(“Masukkan bilangan kedua: “))

if choice == ‘1’:
print(num1,”+”,num2,”=”, add(num1,num2))

elif choice == ‘2’:
print(num1,”-“,num2,”=”, subtract(num1,num2))

elif choice == ‘3’:
print(num1,”*”,num2,”=”, multiply(num1,num2))

elif choice == ‘4’:
print(num1,”/”,num2,”=”, divide(num1,num2))
else:
print(“Input salah”)

# Program untuk menampilkan semua bilangan prima pada interval tertentu
# Ubah nilai lower dan upper untuk hasil yang lain
lower = 200
upper = 300
print(“Bilangan prima antara”,lower,”and”,upper,”:”)
for num in range(lower,upper + 1):
if num > 1:
for i in range(2,num):
if (num % i) == 0:
break
else:
print(num)

Contoh 7: Program untuk mencetak semua permutasi
from itertools import permutations

# Mendapatkan semua permutasi dari [1, 2, 3]
perm = permutations([1, 2, 3])

# Print semua permutasi
for i in perm:
print(i)

Contoh 8: Program untuk mengirim e-mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = “alamat pengirim”
toaddr = “alamat penerima”
msg = MIMEMultipart()
msg[‘From’] = fromaddr
msg[‘To’] = toaddr
msg[‘Subject’] = “judul pesan”

body = “isi pesan”
msg.attach(MIMEText(body, ‘plain’))

server = smtplib.SMTP(‘smtp.gmail.com’, 587)
server.starttls()
server.login(fromaddr, “password pengirim”)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

Contoh 9: Program Menghitung Luas Bentuk 2 Dimensi
#Mencetak Menu
def menu():
print “Pilih Bentuk 2D”
print
print “1. Persegi Panjang”
print “2. Lingkaran”
print “3. Segitiga”
print “4. Keluar”

def persegi():
print “Menghitung Luas Persegi Panjang”
p = input(“Masukkan Panjang : “)
l = input(“Masukkan Lebar : “)
luas = p*l
print “Luas Persegi Panjang adalah “,luas
print
print “Coba lagi [Y/N]? ”
back = raw_input().upper()
if back == “Y”:
menu()
else:
exit()

def lingkaran():
print “Menghitung Luas Lingkaran”
r = input(“Masukkan Jari-Jari : “)
luas = 3.14*(r**2)
print “Luas Lingkaran adalah “,luas
print
print “Coba lagi [Y/N]? ”
back = raw_input().upper()
if back == “Y”:
menu()
else:
exit()

def segitiga():
print “Menghitung Luas Segitiga”
a = input(“Masukkan Alas : “)
t = input(“Masukkan Tinggi : “)
luas = (a*t)/2
print “Luas Segitiga adalah “,luas
print
print “Coba lagi [Y/N]? ”
back = raw_input().upper()
if back == “Y”:
menu()
else:
exit()

#Program Menghitung Luas
print “Selamat Datang di Program Untuk Menghitung Luas”
print “———————————————–”
print
menu()

while l:
#input
pilih = input(“Masukkan pilihan : “)

if pilih == 1:
persegi()
elif pilih == 2:
lingkaran()
elif pilih == 3:
segitiga()
elif pilih == 4:
print “\n”*100
break
else:
print “Maaf pilihan yang anda masukkan tidak terdaftar”
print “Coba lagi [Y/N] ? ”
coba = raw_input().upper()
if coba == “Y”:
menu()
else:
print “\n”*100
break

Contoh 10: Menghitung Zakat Penghasilan
nama=[]
gaji=[]
emas=[]
zakat=[]
pertahun=[]
perbulan=[]
nisab=[]
print (‘+———————————————–+’)
print (‘| Penghitung Zakat Penghasilan |’)
print (‘| menurut pendapatan kasar (brutto) |’)
print (‘| |’)
print (‘+———————————————–+’)
data=int(input(‘Masukan banyak data : ‘))
print(‘==========================================’)

for i in range(data):
a = input(‘Masukan nama : ‘)
nama.append(a)
b = int(input(‘Masukan harga emas saat ini: ‘))
emas.append(b)
c = int(input(‘Masukkan penghasilan Anda per bulan : ‘))
gaji.append(c)
print(”)

for i in range(data):
d = 12 * gaji[i]
pertahun.append(d)
e = 0.025 * pertahun[i]
zakat.append(e)
f = 85 * emas[i]
nisab.append(f)
g = zakat[i] / 12
perbulan.append(g)

for i in range(data):
print (”)
print(‘—————————————-‘)
print(‘ Zakat Penghasilan (Brutto)’)
print(‘—————————————-‘)
print(‘Nama :’,nama[i])
print(‘Harga 1 gram emas :’,’Rp.’,emas[i])
print(‘Penghasilan per bulan :’,’Rp.’,gaji[i])
print(‘Penghasilan per tahun :’,’Rp.’,pertahun[i])
print(‘Harga nishab (85 gram emas) :’,’Rp.’,nisab[i])
print(‘Zakat penghasilan :’,’2.5% x’,pertahun[i],’=’,’Rp.’,zakat[i])
if pertahun[i] >= nisab[i]:
print(‘Keterangan : WAJIB Zakat Rp.’,zakat[i],’/tahun’)
print(‘ atau Rp. ‘,perbulan[i],’/bulan’)
print(”)
if pertahun[i] <= nisab[i]:
print(‘Keterangan : Anda belum termasuk Wajib Zakat’)

Contoh 11: Program Menentukan Nilai Akhir Semester
#Deklarasi Fungsi Operator
def fungsi_total_nilai(var_harian, var_uts, var_uas) :
var_harian = int(var_harian) * 0.3
var_uts = int(var_uts) * 0.3
var_uas = int(var_uas) * 0.4

var_total = var_harian + var_uts + var_uas
return var_total

#Deklarasi Fungsi Percabangan
def fungsi_percabangan (var_nilai) :
var_huruf = “”
if (var_nilai >= 0 and var_nilai < 20) : var_huruf = “E” elif (var_nilai >= 20 and var_nilai < 40) : var_huruf = “D” elif (var_nilai >= 40 and var_nilai < 60) : var_huruf = “C” elif (var_nilai >= 60 and var_nilai < 80) : var_huruf = “B” elif (var_nilai >= 80 and var_nilai < 100) :
var_huruf = “A”
return var_huruf

#Deklarasi Fungsi Perulangan
def fungsi_perulangan():
var_hasil_perulangan = 0
for i in range(1,3):
print(“——–Nilai Ke “,i,”——–“)
var_harian = input(“Nilai Harian : “)
var_uts = input(“Nilai UTS : “)
var_uas = input(“Nilai UAS : “)

#Pemanggilan fungsi Penjumlahan
var_hasil_perulangan +=(int(fungsi_total_nilai(var_harian, var_uts, var_uas)))

return var_hasil_perulangan /i

#Pemanggilan fungsi perulangan
var_total = fungsi_perulangan()

print(“——–Total Nilai ——–“)
print(“Total nilai yang didapat : “,var_total)

#Pemanggilan Fungsi Percabangan
print(“Total Nilai Dalam Huruf : “, fungsi_percabangan(var_total)