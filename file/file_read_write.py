
filename = "file/text.txt"

def read_file(filename) :
    f = open(filename, mode="r", encoding="utf-8")
    data = f.read()
    f.close()
    print(data)

def write_file(filename) :
    f = open(filename, mode="w", encoding="utf-8")
    for i in range(1, 10) :
        data = "{}번째 줄 입니다\n".format(i)
        f.write(data)
    f.close()

def append_file(filename) :
    f = open(filename,mode="a", encoding="utf-8")
    for i in range(10,20) :
        data = "{}번쨰 줄 입니다\n".format(i)
        f.write(data)
    f.close()


write_file(filename)
read_file(filename)
append_file(filename)
read_file(filename)