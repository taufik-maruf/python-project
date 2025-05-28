# CALCULATOR
print('Masukan Pilihan:')
print('A. Perkalian')
print('B. Pembagian')
print('C. Penambahan')
print('D. Pengurangan')

pilihan = input('Pilihan Anda: ')

nilai1 = int(input('Masukan Nilai Pertama:'))
nilai2 = int(input('Masukan Nilai Kedua:'))
jawaban = 0
if pilihan == 'A' or 'a':
    jawaban = nilai1*nilai2
elif pilihan == 'B' or 'b':
    jawaban = nilai1/nilai2
elif pilihan == 'C' or 'c':
    jawaban = nilai1+nilai2
elif pilihan == 'D' or 'd':
    jawaban = nilai1-nilai2

print(f'Hasil = {jawaban}')
