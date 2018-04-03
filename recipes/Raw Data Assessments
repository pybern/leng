def get_rows(file_path):
    '''
    Returns the sum of newlines from the total blocks
    '''
    with open(file_path, "r" ,errors = "ignore") as f:
        print (sum(bl.count("\n") for bl in blocks(f)))

def blocks(files,size = 65536):
    '''
    Read file by defined sizes and returns a generator
    '''
    while True:
        b = files.read(size)
        if not b: break
        yield b
