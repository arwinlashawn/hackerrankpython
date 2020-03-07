# here, only the top line of the input from STDIN is considered. why?
for i in range(int(input())):
    a = int(input())
    # you wanna split the input first before making it a set. if you just convert it to set, the set function will
    # treat ' ' as an element and somehow only take one digit numbers as elements. Numbers with more than one digit
    # will be split into one digit numbers. remember, split() converts the input to 'list' type.
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    # .issubset() does what its name suggests
    print(A.issubset(B))






