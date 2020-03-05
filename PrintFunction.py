if __name__ == '__main__':
    n = int(input())

# i + 1 so '0' isn't printed. Not part of expected solution.
# end='' prints the loop outputs without newline. Outputs next to each other without space in between.
for i in range(n):
    print(i + 1, end='')

