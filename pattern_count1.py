def Pattern_Count(string,pattern):

    listt = string.split()
    new_string = "".join(listt)
    iCount = 0

    print(new_string)

    i = len(pattern)

    for j in range(len(new_string)-i+1):#stroke
        print(new_string[j:j+i])

        if new_string[j:j+i] == pattern:#masterstroke
            iCount = iCount + 1
        
    return iCount




def main():
    print("Enter the string: ")

    strr = input()

    print("Enter the pattern you want to check in string: ")
    patt = input()

    iRet = Pattern_Count(strr,patt)

    print(f"The {patt}  occurs {iRet} times in {strr}")
    



if __name__ == "__main__":
    main()