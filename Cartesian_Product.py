
def Cartesian_Product(L1,L2):
    List3 = []
    for i in L1:
        for j in L2:
            cp = (i,j)
            List3.append(cp)# can also write List3.append((i,j)) directly instead of using cp variable

    return List3

    # can use just list compreshension given below instead of above code
    
    # return [(i, j) for i in L1 for j in L2]




def main():

    print("Enter how many elements you need in list 1: ")

    num1= int(input())

    List1 = []

    for i in range(1,num1+1):
        print(f"Enter element {i} of {num1}")
        n = int(input())
        List1.append(n)

    print(List1)

    print("Enter how many elements you need in list 2: ")

    num2= int(input())

    List2 = []

    for i in range(1,num2+1):
        print(f"Enter element {i} of {num2}")
        n = int(input())
        List2.append(n)

    print(List2)

    '''

    Instead of the above code to take inputs ,we can use just the below 2 lines:

    List1 = list(map(int, input("Enter elements of List 1 separated by space: ").split()))
    List2 = list(map(int, input("Enter elements of List 2 separated by space: ").split()))

                                            OR

    these 4 lines

    print("Enter elements of list 1 separated by space:")
    List1 = list(map(int, input().split()))

    print("Enter elements of list 2 separated by space:")
    List2 = list(map(int, input().split()))
                                      

    ###
    keep in mind that if the code has indentation than the triple quotes also must be in 
    indentation or else the code will throw IndentationError or SyntaxError.
    ###

    '''
    

    iRet  = Cartesian_Product(List1,List2)
    print(f"The cartesian product of {List1} and {List2} is: ")
    for cp in iRet:
        print(cp,end = " ")
        print()


if __name__ == "__main__":
    main()