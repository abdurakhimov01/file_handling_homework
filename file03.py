import string
def main(filename):
    f = open(filename, 'r')
    p=f.read()
    l=[]
    d=string.digits
    i=0
    while i <len(p):
        j=0
        while j<len(d):
            if d[j]==p[i]:
                l.append(p[i])
            j+=1
        i+=1
    return l
print(main("data/data03.txt"))