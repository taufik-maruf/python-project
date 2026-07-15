# Sumber = folder that countain xxamountDoc.pdf
# Output = 1 page, 1 pdf, rename bas on first keyword and last keyword

import os
import openpyxl
import PyPDF2
import shutil

def extract_specific_text_from_pdf(file_path, start_keyword, end_keyword):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            start = page_text.find(start_keyword)
            end = page_text.find(end_keyword)
            if start != -1 and end != -1:
                text += page_text[start+len(start_keyword):end]
    return text

def ambil_niu(file_path, kata_awal, kata_akhir):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        niu = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            start = page_text.find(kata_awal)
            end = page_text.find(kata_akhir)
            if start != -1 and end != -1:
                niu += page_text[start+len(kata_awal):end]
    return niu

def rename_and_move_file(old_path, new_dir, new_name):
    # Membuat direktori baru jika belum ada
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Mengubah nama file
    base, ext = os.path.splitext(old_path)
    new_path = os.path.join(new_dir, 'SKPI_'+new_name + ext)

    # Memindahkan file ke direktori baru
    shutil.move(old_path, new_path)

def write_to_excel(file_path, data):
    wb = openpyxl.Workbook()
    ws = wb.active

    for i, row in enumerate(data, start=1):
        for j, value in enumerate(row, start=1):
            ws.cell(row=i, column=j, value=value)

    wb.save(file_path)

def process_pdfs(pdf_dir, output_excel, start_keyword, end_keyword,kata_awal,kata_akhir):
    data = [['File Name', 'Text']]
    for file_name in os.listdir(pdf_dir):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(pdf_dir, file_name)
            text = extract_specific_text_from_pdf(file_path, start_keyword, end_keyword)
            niu = ambil_niu(file_path, kata_awal, kata_akhir)
            data.append([file_name, text+niu])

            # Mengubah nama file dan memindahkannya ke direktori baru
            new_dir = 'C:/0 Files/CSDU/Python/SKPI/After'
            new_name = text.replace('\\', '').replace('/','').replace('/','').replace('-','').replace(':','').replace('(','').replace(')','').replace('\n','').replace('Place of Birth','').replace('Nomor Induk Mahasiswa','')+'_'+niu.replace('\n','').replace('/','') # Menghapus karakter "/"
            rename_and_move_file(file_path, new_dir, new_name)

    write_to_excel(output_excel, data)

# Contoh penggunaan:
process_pdfs('C:/0 Files/CSDU/Python/SKPI/Before', 'C:/0 Files/CSDU/Python/SKPI/Excel.xlsx', 'Name', 'Tempat Lahir','Student Number','Tanggal Lahir') #:\n00
