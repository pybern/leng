def get_rows(file_path):
    """Returns the sum of newlines from the total blocks
    
    This function does not work with non text based files as far as testing goes.
    Erros seems to be cause by count of newline while reading file.
    More work needs to be done on reading different file types.
    """
    with open(file_path, "r" ,errors = "ignore") as f:
        while True:
            size = print (sum(bl.count("\n") for bl in blocks(f)))
            if not size: print("error")
            print(size)
                

def blocks(files,size = 65536):
    "Read file by defined sizes and returns a generator"
    while True:
        b = files.read(size)
        if not b: break
        yield b
