import string
def main(filename):
    f = open(filename, 'r')
    p=f.read()
    l=[]
    d=string.digits
    for i in p:
        if i in d:
            l.append(i)
    return l
print(main("data/data03.txt"))