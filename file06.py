def main(filename):
    o=open(filename, "r")
    f=o.read()
    p=f.split("\n")
    a=[]
    for i in p:
        a+=[len(i)]
    return a
print(main("data/data06.txt"))