print('Program Python Cek Bilangan Positif/Negatif/0')
print('======================================')
print()
 
x = int(input('Input satu angka : '))

if(x > 0):   #jika x lebih besar dari 0 maka tampil bilangan positif
 print('bilangan positif')
elif(x == 0): #jika x sama dengan 0 maka tampil bilangan 0
  print('bilangan 0')
else: #selain dari kondisi di atas maka tampil bilangan negatif
    print('bilangan negatif')
