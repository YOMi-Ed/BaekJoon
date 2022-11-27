#import sys
#input = sys.stdin.readline
# 내가 한 부분은 오류가 발생했다....(반례를 못찾겠음..)
mo = ['a','e','i','o','u']
result = False
while True :
    string = input()

    if string == "end" :
        break
    if len(string) > 2 :
        for i in range(len(string)-2) :
            store = string[i]
            if string[i] not in mo :
                if string[i+1] not in mo and string[i+1] != store :
                    if string[i+2] not in mo :
                        result = False
                        break
                    else :
                        result = True               
                elif string[i+1] not in mo and string[i+1] == store :
                    result = False
                    break
            else :
                if string[i+1] in mo and store == string[i+1]:
                    if store == "e" or store=='o' :
                        if string[i+2] in mo :
                            result = False
                            break
                        else :
                            result = True
                    else :
                        result = False
                        break
                elif string[i+1] in mo and store != string[i+1]:
                    if string[i+2] in mo :
                        result = False
                        break
                elif string[i+1] not in mo :
                    if string[i+1] == string[i+2] :
                        result = False
                        break
                    else :
                        result = True
    else :
        if len(string) == 1 :
            if string in mo :
                result = True
        else :
            if string in mo :
                if string[0] in mo  and string[1] not in mo :
                    result = True
                elif string[0] not in mo  and string[1] in mo :
                    result = True
                elif (string[0] and string[1]) =='e' or (string[0] and string[1]) =='o' :
                    result = True
                else :
                    result = False
            else :
                result = False
    if result == True :
        print("<"+string+">"+ " is acceptable.")
    elif result == False :
        print("<"+string+">"+ " is not acceptable.")

# 다른 사람이 푼 것 확실히 내 코드보다 깔끔해 보임...
aeiou = "aeiou"

while True:
    s = input()
    if s == "end" :
        break

    flag = True
    if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s :
        z_cnt = 0
        m_cnt = 0
        dup = ""
        for i in range(len(s)) :
            if s[i] not in aeiou :
                m_cnt = 0
                z_cnt += 1
                if z_cnt >= 3 :
                    flag = False
                if dup == s[i] :
                    flag = False
            else :
                z_cnt = 0
                m_cnt += 1
                if m_cnt >= 3:
                    flag = False
                if dup == s[i] :
                    if s[i] != 'e' and s[i] != 'o' :
                        flag = False
            dup = s[i]
        if flag :
            print("<"+s+">"+ " is acceptable.")
        else :
            print("<"+s+">"+ " is not acceptable.")
    else :
        print("<"+s+">"+ " is not acceptable.")