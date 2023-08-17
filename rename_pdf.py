
import fitz

from os import DirEntry, curdir, getcwd, chdir, rename
from glob import glob as glob

directory = 'PDF_FILES'
chdir(directory)

pdf_list = glob('*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[81].get_text()
        last_word = text.split()
        arrsize = len(last_word)
        arrsize2=arrsize-1
    print(arrsize2)
    while arrsize2>=0:
        x=last_word[arrsize2].isdigit()
        if x:
            numberlength =len(last_word[arrsize2])
            if (numberlength==6):
                print(numberlength,last_word[arrsize2])
    arrsize2=arrsize2-1
    rename(pdf, last_word[arrsize2] + '-Employee_Handbook.pdf')
            #print (x)
            
         #  
       