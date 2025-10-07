def Reverse_String(sentence):

    List1 = sentence.split()

    print(List1)
    print(len(List1))

    Reversed = ""

    for i in range(len(List1)-1,-1,-1):# for reverse, step is very necessary (last wali value i.e -1)
        #Reversed = Reversed + " " + List1[i]
        Reversed = " ".join(List1[::-1])# for reverse, step is very necessary (last wali value i.e -1)
    # as default step size is always +1
    print(Reversed)

    return Reversed


def main():

    print("Enter the string: ")
    string = input()

    cRet = Reverse_String(string)

    print(f"The reverse of {string} is: {cRet}")


if __name__ == "__main__":
    main()