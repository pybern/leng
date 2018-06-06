#with intention to color code the highlighted text

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#preview function of words that are found withing a string object

def preview(string,keyword, case_sensitive = False, preview_range = 50):
    
    len_string = len(string)
    len_keyword = len(keyword)

    _string = string if case_sensitive else string.lower()
    _keyword = keyword if case_sensitive else keyword.lower()
    
    occurence = [i for i in re.finditer(_keyword,_string)]
    
    print(len(occurence))
    print('*************')

    for i in occurence:
        start,end = i.span()

        start = start-preview_range if start-preview_range > 0 else 0
        end = end+preview_range if end+preview_range <= len_string else len_string

        print(color.RED+string[start:end]+color.END)
        print('*************')
