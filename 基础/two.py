#coding=utf-8

# Funtion
# defind a compare function
def cmp(x,y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0

print(cmp(2,1))