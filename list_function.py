import file
def search_in_file(path,category, element):
    text=file.read_file(path).split('\n')
    for i in text:
        list = i.split(";")
        if (list[category]==element):
            return list
    return []

