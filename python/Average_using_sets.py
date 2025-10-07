
def Unique_Average(Array):
    set1 = set(Array)

    print(type(set1))

    addition = 0

    for i in set1:
        addition = addition + i

    Avg = addition/len(set1)

    return Avg


def main():

    print("How many numbers you want in a list1: ")
    n = int(input())

    print("Enter the numbers in list1 one by one")
    Arr = []
    
    for i in range(1,n+1):
        print(f"Enter num {i} of {n}")
        num = int(input())
        Arr.append(num)

    print(Arr)

    iRet = Unique_Average(Arr)
    print(f"The average of given numbers is {iRet}")


if __name__ == "__main__":
    main()