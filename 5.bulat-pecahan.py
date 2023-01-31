print('Program Python Menentukan Bilangan Bulat-Pecahan')
print('=====================================================')
print()
 
x = input('Input sebuah angka : ')
 
if (x.isdecimal()): #jika bilangan merupakan bilangan desimal tanpa . (0.0)
   print(x,'adalah bilangan bulat')
else: 
     print(x,'adalah bilangan pecahan')
 
