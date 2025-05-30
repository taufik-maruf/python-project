# CALCULATOR
print('Masukan Pilihan:')
print('A. Perkalian')
print('B. Pembagian')
print('C. Penambahan')
print('D. Pengurangan')

pilihan = input('Pilihan Anda: ').upper()

nilai1 = int(input('Masukan Nilai Pertama:'))
nilai2 = int(input('Masukan Nilai Kedua:'))
jawaban = 0
if pilihan == 'A':
    jawaban = nilai1*nilai2
elif pilihan == 'B':
    jawaban = nilai1/nilai2
elif pilihan == 'C':
    jawaban = nilai1+nilai2
elif pilihan == 'D':
    jawaban = nilai1-nilai2

print(f'Hasil = {jawaban}')
