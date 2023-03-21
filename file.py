def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
         return file.read()

def read_line(path):
    with open(path, encoding='utf-8') as file:
        return file.readline()

def write_line(path, list):
    line=""
    for i in list:
        line+=i+";"
    line=line[:-1:]
    with open(path, 'a', encoding='utf-8') as file:
        file.write("\n"+line)
