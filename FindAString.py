def count_substring(string, sub_string):
    # notice that the substrings overlap with each other in the string, so can't use .count() function
    start = 0
    count = 0
    while start < len(string):
        found_index = string.find(sub_string, start)
        # remember, .find() function returns -1 if substring not found in string
        if found_index != -1:
            # adjusts start pointer to next to index where substring is found
            start = found_index + 1
            count = count + 1
        else:
            return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)






