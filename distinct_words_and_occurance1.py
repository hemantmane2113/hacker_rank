def distinct_words(words):# time complexity = O(n)

    counter_dict = {}
    for word in words:
        counter_dict[word] = counter_dict.get(word, 0) + 1

    print(counter_dict)
    counter_dict_values = list(counter_dict.values())
    print("Word frequencies: ", counter_dict_values)
    print("Total distinct words: ", len(counter_dict))

    return len(counter_dict), counter_dict_values



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