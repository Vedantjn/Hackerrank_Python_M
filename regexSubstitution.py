import re
N = int(input())

for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

# for _ in range(int(input())):
#     line = input()
    
#     while ' && ' in line or ' || ' in line:
#         line = line.replace(" && ", " and ").replace(" || ", " or ")
    
#     print(line)