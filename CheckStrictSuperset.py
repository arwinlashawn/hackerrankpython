A = set(input().split())

superset = None
for i in range(int(input())):
    B = set(input().split())
    if A.issuperset(B) is True:
        superset = True
    elif A.issuperset(B) is False:
        superset = False
        # once it is found that A is not a strict superset of a B, the output is for sure False, hence breaks here
        # important to break here or else, once the loop is executed again for the next B set, if A is a superset of
        # B, superset value will be replaced with True
        break

# printing here because you only want one output after considering all the B subsets
print(superset)






