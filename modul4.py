
def closing(*penutup):
    for kalimat in penutup:
        print("Terimakasih Telah Menggunakan Layanan Kami Untuk ",kalimat)


print('Selamat Datang di Bank Kelompok 12')
nama = input('Nama Anda adalah ')
print('\n')
a = 1
n = 3
saldo = 5000000
while (a < 4):
	pin = int(input('Anda memiliki 3 kali kesempatan \nSilakan input 6-pin Anda untuk meneruskan ke menu : '))
	a = a + 1
	n = n - 1
	if (pin == 112233):
		print("Selamat datang ",nama)
		print('Anda memiliki saldo sebesar :  5.000.000 ~rupiah')
		act1 = int(input('(12). Transfer \n(13). Tarik Tunai \nSilakan memasukan kode dengan tepat : ')) 
		if (act1 == 12):
			norek = int(input('\nMasukan nomor rekening tujuan : '))
			out1 = int(input('Maksimal pengiriman Rp 4.000.000 \nJumlah yang akan dikirim(ketik tanpa tanda titik atau koma)  :'))
			sisa = saldo - out1
			print('Anda berhasil mengirim ke rekening ',norek,' dengan jumlah dana ',out1)
			print('Maka sisa saldo Anda adalah ',sisa, 'rupiah')
			closing("Mengirim Dana")

		elif (act1 == 13):
			out2 = int(input('\nMasukan jumlah tarik tunai : '))
			sisa2 = saldo - out2
			print('Silakan ambil uang Anda terlebih dahulu\nSisa saldo Anda adalah ',sisa2,' rupiah')
			closing("Menarik Dana")

		break
	else:
		print('PIN SALAH')
print('program end...')		














	
