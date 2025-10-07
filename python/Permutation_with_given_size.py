def Permutation(word,size,current = ""):

    if len(current) == size:
        print(current)
        return
    for ch in word:# can use (sorted(word) to sort)
        if ch not in current:
            Permutation(word, size, current + ch)


def main():
    
    print("Please enter the string in upper case: ")

    string = input()

    if string.isupper():
        pass
    else:
        string = string.upper()

    print(string)

    print("Please enter the size of permutation: ")

    num = int(input())

    bRet = Permutation(string,num)


if __name__ == "__main__":
    main()