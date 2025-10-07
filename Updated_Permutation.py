def Permutation(s, size, current=""):
    if len(current) == size:
        return [current]  # return a list containing this permutation

    result = []
    for ch in sorted(s):# for sorted manner
        if ch not in current:
            # recursively get permutations and extend result
            result.extend(Permutation(s, size, current + ch))
    return result

# Main
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

    print(f"The possible permutations of the string {string} of size {num} is as follows: ")

    for p in bRet:
        print(p)



if __name__ == "__main__":
    main()

