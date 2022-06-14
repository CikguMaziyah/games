#function untuk 3 games
import random
#permainan pertama teka nombor
def tekanombor():
#tajuk pilihan pertama
    print("***TEKA NOMBOR***")

    #penggunaan module random randint
    x=random.randint(1,10)
    #setkan variable guess kepada tiada nilai
    guess=None
    
    #setkan ulangan 
    while x!=guess:
        
        #pengguna memasukkan nilai yang diteka jenis data integer dan disimpan dalam pembolehubah guess       
        guess=int(input("Pilih nombor antara 1 hingga 10: "))

        #penggunaan struktur kawalan if elif 
        if x==guess:
            print("Anda hebat!")
        elif x>guess:
            print("Cuba nombor yang lebih besar.")
        elif x<guess:
            print("Cuba nombor yang lebih kecil.")

#permainan kedua teka huruf
def tekahuruf():
    print("***TEKA HURUF***")
    
    #penggunaan module random choice dengan setkan variable y dengan character USTP
    y="USTP"
    x=random.choice(y)
    guess=None
    
    while x!=guess:
        guess=str(input("Pilih satu huruf dari perkataan USTP: "))
        
        if x==guess:
            print("Bagus.")
        else:
            print("Maaf.Cuba lagi.")

#permainan ketiga teka nama buah
def tekabuah():
    print("***TEKA NAMA BUAH***")

    #array nama buah
    buah=["cempedak","cermai","ciku","ceri"]

    #random method choice variable z menyimpan info dari senarai buah
    z=random.choice(buah)
            
    #setkan variable namabuah kepada tiada nilai
    namabuah=None         
            
    #while untuk ulangan 
    while z != namabuah:
            
    #pengguna memasukkan satu nama buah bermula dengan huruf c
        namabuah=str(input("Masukkan nama buah bermula huruf c(gunakan huruf kecil): "))
                
        if z==namabuah:
            print("Tahniah!!!")          
        else:
            print("Cuba lagi...")

#Senarai menu pilihan untuk pilihan pengguna
print("SELAMAT DATANG KE PERMAINAN TEKA-TEKA")
print("Menu Pilihan")
print("1.Teka Nombor")
print("2.Teka Huruf")
print("3.Teka Nama Buah")
print("4.Keluar Permainan")

#setkan pemboleh ubah pilihan sebagai 0 selagi pengguna belum memasukkan nilai pilihan
pilihan=0

#ulangan sekiranya pengguna ingin meneruskan permainan atau tidak
while pilihan!='4':

    #pemboleh ubah untuk pengguna memasukkan pilihan
    pilihan=str(input("Masukkan pilihan anda. Taip nombor 1, 2, 3 atau 4."))
    
    #struktur kawalan if, elif untuk 3 pilihan permainan yang dipilih pengguna
    if(pilihan=='1'):
        tekanombor()
    elif(pilihan=='2'):     
        tekahuruf()
    elif(pilihan=='3'):
        tekabuah()
        
print("Terima kasih kerana menggunakan permainan ini. Jumpa lagi.")
