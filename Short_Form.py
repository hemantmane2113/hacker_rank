# input : Hemant Dattaji Mane
# output: H.D.M.

# spliting: varible = iterable[list,tuple,set,string].split(separator),separator: on basis of what to split ( basis of separation)
#joining  : variale = seperator.join(iterable[list,tuple,set,string]),separator: join with what (what joint to be used)

#code 1 - By me

def Short_Form(sentence):

    list1 = sentence.split(" ")

    print(list1)

    list2 = []

    for word in list1:
        for i in range(len(word)):
            ch = word[0]
            list2.append(word[0].upper())
            break
    
    print(list2)

    shortform = ".".join(list2) + "." # keep in mind here list2 means each individual element
    # in the list,because in joins the algoritm is: variable =  separator.join(iterable)

    """
    so instead of doing

    shortform = "" 
    for ch in list2: 
        shortform = shortform + ch + "." 
    print(shortform) return shortform
    
    we can use above method

    """

    

    return shortform

def main():

    print("Please enter the string: ")

    string = input()

    cRet = Short_Form(string)

    print(f"The short form of {string} is {cRet}")


if __name__ == "__main__":
    main()



"""

# code2

def Short_Form(sentence):
    words = sentence.split()   # splits on spaces automatically
    initials = [] 
    for word in words:
        if word:   # take first letter of each word
            initials.append(word[0].upper())

    shortform = ".".join(initials) + "."

    return shortform


def main():
    print("Please enter the string: ")
    string = input()
    cRet = Short_Form(string)
    print(f"The short form of {string} is {cRet}")

if __name__ == "__main__":
    main()


"""


"""

# code3



def Short_Form(sentence):
    words = sentence.split()   # splits on spaces automatically
    initials = [word[0].upper() for word in words if word]   # take first letter of each word
    shortform = ".".join(initials) + "."   # join with dots and add a trailing dot
    return shortform

def main():
    print("Please enter the string: ")
    string = input()
    cRet = Short_Form(string)
    print(f"The short form of {string} is {cRet}")

if __name__ == "__main__":
    main()

"""