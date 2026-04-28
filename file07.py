import string
def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    o=open(data,'r')
    f=o.read()
    l=0
    for i in f:
        if i in string.digits:
            l+=int(i)
    return l
print(main('data/data07.txt'))
# Read data from file