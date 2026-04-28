def main(filename):
    f=open(filename, "r")
    p=f.readline()
    l=[]
    for i in p:
        l.append(i)
    return l
print(main("data/data04.txt"))