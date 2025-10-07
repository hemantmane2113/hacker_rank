
def Combining_Sets(Array1,Array2):

    set1 = set(Array1)
    set2 = set(Array2)

    set3 = set()

    for i in set1:
        if i not in set2:
            set3.add(i)

    for i in set2:
        if i not in set1:
            set3.add(i)

    return sorted(set3)


# we can use inbuild function set3 = set1.symmetric_difference(set2)
# other functions set3 = set1.union(set2),set3 = set1.intersection(set2),set3 = set1.difference(set2)
#

def main():

    print("How many numbers you want in a list1: ")
    n1 = int(input())

    print("Enter the numbers in list1 one by one")
    Arr1 = []
    
    for i in range(1,n1+1):
        print(f"Enter num {i} of {n1}")
        num1 = int(input())
        Arr1.append(num1)

    print("How many numbers you want in a list2: ")
    n2 = int(input())

    print("Enter the numbers in list1 one by one")
    Arr2 = []
    
    for i in range(1,n2+1):
        print(f"Enter num {i} of {n2}")
        num2 = int(input())
        Arr2.append(num2)

    iRet = Combining_Sets(Arr1,Arr2)

    print(f"The new set after combining two sets is {iRet}")



if __name__ == "__main__":
    main()

# see the how the loop condtions change if we use list instead of set
    """
    def unique_elements_list(arr1, arr2):
    result = []

    # elements in arr1 but not in arr2
    for i in arr1:
        if i not in arr2 and i not in result:
            result.append(i)

    # elements in arr2 but not in arr1
    for j in arr2:
        if j not in arr1 and j not in result:
            result.append(j)

    return sorted(result)


arr1 = [1, 2, 2, 3, 4]
arr2 = [3, 4, 4, 5, 6]

print("List version unique elements:", unique_elements_list(arr1, arr2))

    
    
    
    
    
    
    """