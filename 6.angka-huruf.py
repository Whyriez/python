print('Program Python Menentukan Angka-Huruf')
print('=====================================================')
print()
 
x = input('Input sebuah angka/huruf : ')
 
if (x.isalpha()): #jika inputan merupakan huruf tanpa angka maka tampilkan
  print(x,'adalah bilangan huruf')
else: #jika merupakan angka maka
  print(x,'adalah bilangan angka');
