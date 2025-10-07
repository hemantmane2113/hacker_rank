# code 4
def Capitalise(s):

    result = ""
    Flag = True

    for ch in s:
        if ch.isalpha():
            if Flag == True:
                result = result + ch.upper()          
            else:
                result = result + ch

            Flag = False

        else:
            result = result + ch
            Flag = (ch == " ")
        
    return result
        
def main():
    print("Please enter the string: ")

    string = input()

    cRet = Capitalise(string)

    print(f"The capitalized version of {string} is {cRet}")


if __name__ == "__main__":
    main()

"""
-------------------------------------------------------------------------
code 3:

This code also works well but fails some condition

input:             1 w r 2 3g
expected output:   1 W R 2 3g
output of thi code:1 W R 2 3G

def solve(s):
     
    result = ""
    Flag = True

    for ch in s:
        if Flag == True and ch.isalpha():
            result = result + ch.upper()
            Flag = False
        else:
            result = result + ch
            if ch == " ":
                Flag = True
        
    return result

def main():
    print("Please enter the string: ")

    string = input()

    cRet = Capitalise(string)

    print(f"The capitalized version of {string} is {cRet}")


if __name__ == "__main__":
    main()

-------------------------------------------------------------------------------------------

  
Code 2:
This code works well on normal strings but fails when the strings have extra spaces between them
for eg
input:                 hello    world   lol
output with this code: Hello World Lol (it removes extra spaces) 
expected output      : Hello    World   Lol


def Capitalise(s):

    listt = s.split()

    for i in  range(len(listt)):
        word  = listt[i]
        if word[0].isalpha():
            if word[0].islower():
                word = word[0].upper() + word[1:]
                
        
        listt[i] = word
              
    String = " ".join(listt)

    return String

def main():
    print("Please enter the string: ")

    string = input()

    cRet = Capitalise(string)

    print(f"The capitalized version of {string} is {cRet}")


if __name__ == "__main__":
    main()

-----------------------------------------------------------------------------------------
code 1:(same as above with sliter efficiency)


here we could use another list to save the updated string,but instead we chose to 
put the updated string back to the same list



def Capitalise(s):

    listt = s.split()

    list2 = []

    for word in listt:
        if word[0].isalpha():
            if word[0].islower():
                word = word[0].upper() + word[1:]
                
        
        listt.append(word)
              
    String = " ".join(listt)

    return String

def main():
    print("Please enter the string: ")

    string = input()

    cRet = Capitalise(string)

    print(f"The capitalized version of {string} is {cRet}")


if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------------
"""