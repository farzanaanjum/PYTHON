## Write a program to fetch only even values from a dictionary?


# Fetch only even values form a dictionary and append to a list

dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }

for i in dic.values():
    if i % 2 == 0:
        print(i, end = " ")
    else:
        pass



## output
# 10  20  22
