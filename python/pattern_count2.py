def Pattern_Count(string, pattern):
    iCount = 0
    i = len(pattern)
    new_str = string

    while len(new_str) >= i:
        # take the last i characters
        if new_str[-i:] == pattern:#stroke
            iCount += 1
        # remove the last character for next iteration
        new_str = new_str[:-1]#masterstroke

    return iCount


def main():
    strr = input("Enter the string: ")
    patt = input("Enter the pattern you want to check in string: ")

    iRet = Pattern_Count(strr, patt)
    print(f"The '{patt}' occurs {iRet} times in '{strr}'")


if __name__ == "__main__":
    main()

