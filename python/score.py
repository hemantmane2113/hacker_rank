def main():
    print("Enter the number")
    n = int(input())
    data = []
    for i in range(n):
        name = input()
        score = float(input())
        data.append([name,score])

    data = list(set(data))
    print(data)



if __name__ == "__main__":
    main()