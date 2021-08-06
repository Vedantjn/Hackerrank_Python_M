def minion_game(string):
    # your code goes here
    Kcount = 0;
    Scount = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            Kcount += (str_len)-i
        else :
            Scount += (str_len)-i
    
    if Kcount > Scount:
        print("Kevin", Kcount)
    elif Kcount < Scount:
        print("Stuart",Scount)
    elif Kcount == Scount:
        print("Draw")
    else :
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)