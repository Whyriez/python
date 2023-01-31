print('Program Python Cek Angka Prima')
print('======================================')
print()
 
x = int(input('Input satu angka : '))
 
angka_prima = True
if((x == 0) or (x == 1)): #jika x sama dengan 0 dan x sama dengan 1 maka angkaprima false krna 0 dan 1 dalam matematika bukanlah angka prima
  angka_prima = False
else:
  for i in range(2,(x//2)): #perulangan memulai dari 2 hingga x dibagi 2 fungsi ini agar tidak semua bilangan x dibagi dengan 2 hanya sebagian saja
    if ((x % i) == 0): #cek apakah x habis dibagi dengan i, jika terpenuhi maka angkaprima false
       angka_prima = False
       break
 
if(angka_prima): #jika angka prima true
  print(x,'adalah angka prima')
else: #jika angka prima selain true
  print(x,'bukan angka prima')
