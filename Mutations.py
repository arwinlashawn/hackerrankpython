def mutate_string(string, position, character):
    l = list(string)
    print(l)
    l[position] = character
    new_string = ''.join(l)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)






