def Combinations(word, size, start=0, current="", results=None):
    if results is None:
        results = []

    # if current string has at least 1 character, add it
    if current:
        results.append(current)

    # generate further combinations
    for i in range(start, len(word)):
        if len(current) < size:  # don't exceed size
            Combinations(word, size, i + 1, current + word[i], results)

    return results


def main():
    print("Please enter the string in upper case: ")
    string = input().strip()

    if not string.isupper():
        string = string.upper()

    print(string)

    print("Please enter the size of combination: ")
    num = int(input())

    all_combs = Combinations(sorted(string), num)

    # print in order
    for c in all_combs:
        if len(c) == 2:
            print(c)


if __name__ == "__main__":
    main()
