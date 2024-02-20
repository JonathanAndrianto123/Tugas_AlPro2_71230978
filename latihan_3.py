gaji = float(input('Berapa gaji yang anda ingin per jam? \n'))
jam = int(input('Berapa jam jumlah jam kerja yang anda ingin dalam seminggu? \n'))

#Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak.
gaji_sebelum = gaji * (jam * 5)

#Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak.
gaji_setelah = gaji_sebelum - (gaji_sebelum * 14 / 100)

#Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris.
pakaian = (gaji_setelah * 10 / 100)

#Jumlah uang yang akan Budi habiskan untuk membeli alat tulis.
alat = (gaji_setelah * 1 / 100)

#Jumlah uang yang akan Budi sedekahkan.
sedekah = (gaji_setelah - (alat + pakaian)) * 25 / 100

#Jumlah uang yang akan diterima anak yatim.
yatim = (sedekah) * 30 / 100

#Jumlah uang yang akan diterima kaum dhuafa.
dhuafa = (sedekah) * 70 / 100

print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah Rp.{gaji_sebelum}")
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah Rp.{gaji_setelah}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris adalah Rp.{pakaian}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis adalah Rp.{alat}")
print(f"Jumlah uang yang akan Budi sedekahkan adalah Rp.{sedekah}")
print(f"Jumlah uang yang akan diterima anak yatim adalah Rp.{yatim}")
print(f"Jumlah uang yang akan diterima kaum dhuafa adalah Rp.{dhuafa}")