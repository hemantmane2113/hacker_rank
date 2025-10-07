from itertools import product

def Combinations(string, size):
    char = list(string.upper())
    print("Characters:", char)

# will work for size = 2

#   for i in range(len(char)):
#      result = 0
#      for j in range(len(char)):
#          result = char[i]+char[j]
#          combinations.append(result)
#          j = j + 1


    # Generate all combinations of given(dynamic) size with repetition
    combinations = [''.join(p) for p in product(char, repeat=size)]
    print("All combinations:", combinations)
    

    sorted_combinations = sorted(combinations)

    print(sorted_combinations)

    unique = []
    duplicates = set()

    for comb in sorted_combinations:
        rev = comb[::-1]
        if rev in unique:
            duplicates.add(comb)
        else:
            unique.append(comb)

    
    print(unique)
    print(duplicates)

    return unique

def main():
    print("Enter the string: ")

    chars = input().upper()
    print(chars)

    print("Enter the size of combination: ")

    num = int(input())
    print(num)

    iRet = Combinations(chars,num)

    print(f"The all possible combinations of {chars} of size {num} are:  ")
    for i in iRet:
        print(i)



if __name__ == "__main__":
    main()