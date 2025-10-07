def Check_Pattern(String):

    listt = list(String)# single word string to respective characters

    has_upper = has_lower = has_alphanumeric = has_digit = has_alphabet = False

    print(listt)

    for ch in listt:
        if ch.isupper():
             has_upper = True# has not used else condition,so once flag becomes true,it stays true
        if ch.islower():
            has_lower = True
        if ch.isalnum():
            has_alphanumeric = True
        if ch.isdigit():
            has_digit = True
        if ch.isalpha():
            has_alphabet = True
    
    return has_alphanumeric,has_alphabet,has_digit,has_lower,has_upper
        

def main():
    print("Enter the string: ")
    strr = input()

    iRet = Check_Pattern(strr)

    for i in iRet:
        print(i)


if __name__ == "__main__":
    main()