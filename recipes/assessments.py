import zipfile
import xlrd
import io
import glob
import os

# unzip all of the archive files in the provided path

def unzip_archive(path):
    
    # Check everything with the file extension 'zip' in the provided path
    files = glob.glob(path+'\\*.zip')
    
    # Extract all the files inside the archive
    
    for f in files:
        zf = zipfile.ZipFile(f, mode='r')
        output = input('Please provide the full path to store the unzipped files: ')
        zf.extractall(path=output)
        zf.close()
    return get_ext(files,output)


# To get an overview of the file types extracted from the archive file
def get_ext(file_ext,outpath):
    files=[]
    count=0
    for file_ext in os.listdir(outpath):
        file_ext = file_ext.split('.')[1]
        if file_ext not in files:
            files.append(file_ext)
    print('Here are the file types extracted from the archive file: ',files)
    return summ_stat(outpath)  



# To get the summary of the stastistic of all the file extracted from the archive file
def summ_stat(out):
    for file in os.listdir(out):
        print('File Name: ',file)
        num_lines=0
        if file.endswith('txt'):
            for line in file:
                num_lines += 1
            print('number of lines in the text file: ', num_lines)
        elif file.endswith('xls') or file.endswith('xlsx'):
            workbook = xlrd.open_workbook(out+'\\'+file)
            for sheet in workbook.sheets():
                print('The number of Rows: ',sheet.nrows)
                print('The number of Columns: ',sheet.ncols)
                        
        else:
            pass

def get_rows(file_path):
    """Returns the sum of newlines from the total blocks
    
    This function does not work with non text based files as far as testing goes.
    Erros seems to be cause by count of newline while reading file.
    More work needs to be done on reading different file types.
    """
    with open(file_path, "r") as f:
        size = sum(bl.count("\n") for bl in blocks(f))
        
                

def blocks(files,size = 65536):
    "Read file by defined sizes and returns a generator"
    while True:
        b = files.read(size)
        if not b: break
        yield b
        
