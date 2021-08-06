# def merge_the_tools(string, k):
#     for i in range(0,len(string), k):
#         #slice string upto k characters
#         line = string[i:i+k]
#         seen = set()
#         for i in line:
#             #only print if we haven't already seen this character
#             if i not in seen:
#                 print(i,end="")
#                 seen.add(i)
#         #prints a new line
#         print()
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

#--------------------------------------------------------------------------------------
#OR:
def merge_the_tools(string, k):
    str=''
    count=0
    for i in string:
        if i not in str:
            str=str+i
        count+=1
        if i==k:
            count=0
            print(str)
            str=''