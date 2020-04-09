def get_suffix(filename,has_dog):
    pos = filename.rfind('.')
    if 0<pos<len(filename):
        index = pos if has_dog ==False else pos + 1
        return filename[index:0]
    else:
        return ''