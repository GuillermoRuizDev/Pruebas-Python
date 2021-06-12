def read():
    numbers = []
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Nicolas","Luis","Jhon","Luigi","Pepe"]
    with open("./archivos/names.txt","w", encoding="utf-8") as f:
        for line in names:
            f.write(line)
            f.write("\n")    


def run():
    write()


if __name__ =="__main__":
    run()