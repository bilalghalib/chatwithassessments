import os
import argparse
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger
from reportlab.lib.pagesizes import letter

def text_to_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 10)
    for line in text.split('\n'):
        if not line:
            height -= 15
        else:
            height -= 15
            c.drawString(10, height, line)
    c.save()

def merge_pdfs(filenames, output_filename):
    merger = PdfMerger()

    for filename in filenames:
        merger.append(filename)
    
    merger.write(output_filename)
    merger.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder', help='The folder containing the text files.')
    parser.add_argument('output_folder', help='The folder to save the output PDF.')
    args = parser.parse_args()

    text_files = [f for f in os.listdir(args.input_folder) if f.endswith('.txt')]
    temp_pdfs = []

    for text_file in text_files:
        with open(os.path.join(args.input_folder, text_file), 'r') as file:
            data = file.read()
            temp_filename = os.path.join(args.input_folder, f'{os.path.splitext(text_file)[0]}_temp.pdf')
            text_to_pdf(data, temp_filename)
            temp_pdfs.append(temp_filename)

    output_filename = os.path.join(args.output_folder, 'output.pdf')
    merge_pdfs(temp_pdfs, output_filename)

    for pdf in temp_pdfs:
        os.remove(pdf)

if __name__ == "__main__":
    main()
