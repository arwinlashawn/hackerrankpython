if __name__ == '__main__':
    s = input()

one = False
two = False
three = False
four = False
five = False
for i in range(0, len(s)):
    if s[i].isalnum():
        one = True
    if s[i].isalpha():
        two = True
    if s[i].isdigit():
        three = True
    if s[i].islower():
        four = True
    if s[i].isupper():
        five = True

print(one)
print(two)
print(three)
print(four)
print(five)






