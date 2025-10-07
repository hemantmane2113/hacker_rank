def distinct_words(words):# time complexity = O(n^2)
    counter_dict = {}
    counter = 0
    for i in range(len(words)):
        counter = 0
        for j in range(len(words)):
            if words[i] == words[j]:
                counter = counter + 1
        counter_dict[words[i]] = counter

    print(counter_dict)
    counter_dict_values = []
    for keys,values in counter_dict.items():
        counter_dict_values.append(values)
    print("Total distinct words: ",counter_dict_values)
    print("Total words: ",len(counter_dict))

    return len(counter_dict),counter_dict_values


def main():

    print("Enter how many words you want to enter: ")
    num = int(input())

    list_of_words = []
    for i in range(1,num+1):
        print(f"Enter word {i} of {num}: ")
        word = input()
        list_of_words.append(word)

    print(list_of_words)

    iRet1,iRet2 = distinct_words(list_of_words)
    print(iRet1)
    for i in iRet2:
        print(i,end = ' ')
    print()


if __name__ == "__main__":
    main()