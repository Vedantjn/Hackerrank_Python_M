# from itertools import groupby
# print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

from itertools import groupby
List=input()
for c, items in groupby(List):    
    print(tuple([len(list(items)),int(c)]), end=' ')