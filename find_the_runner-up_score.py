n = 5
arr = [2,3,6,6,5]

### THOUGHT PROCESS ###
# remove any duplicates using set()
# then sort the set using sorted(), ascending order by default
# access second last item using index

### SOLUTION ###
print(sorted(set(arr))[-2])

