#unlimited postional arguments by using *args but the position matters 
def add (*args):
    sum = 0 
    for n in args:
        sum +=n
    return sum
print ( add(3,5,8,9,10) )
