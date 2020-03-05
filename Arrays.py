import numpy

def arrays(arr):
    # [::-1] reverses the array
    # float converts the array to float type
    return numpy.array(arr[::-1], float)

# strip() deletes any white spaces at the beginning and end of the input string.
# you can pass a string into strip(), then the string will be removed from the input string from the beginning and end.
# REMEMBER, order doesn't matter for strip(), you can remove "an" and "na" if they're at the beginning and end of a
# string.
# split() splits a string. you can specify what to split the string by. in this case, a space. default does the same
# thing. also, split() converts a string into list!!!
arr = input().strip().split(' ')
result = arrays(arr)
print(result)





