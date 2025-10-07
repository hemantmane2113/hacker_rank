
def Swap(s):
    
    listt = s.split()
    print(listt)
    
    list3  = []

    for word in listt:
        list2 = []
        for i in range(len(word)):
            if word[i] == word[i].lower():
                ch = word[i].upper()
            else:
                ch = word[i].lower()
            list2.append(ch)
        print(list2)
        wordd = "".join(list2)
        list3.append(wordd)
    print(list3)
    sentence = " ".join(list3)
    return sentence




def main():
    print("Enter the string: ")
    String = input()

    iRet = Swap(String)

    print(f"The swapcase for {String} is {iRet}")


if __name__ == "__main__":
    main()