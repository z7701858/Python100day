#设计一个函数返回给定文件名的后缀名。

def returnfiletype(filename):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos 
        return filename[index:]
    else:
        return ''

print(returnfiletype("2.txt"))