
def Distinct_Values(values):

    distinct = set()# non empty use {}

    for value in values:
        distinct.add(value)

    return len(distinct)



def main():

    print("How many countries do you want to enter:")

    num = int(input())

    print("Enter the countries one by one: ")

    countries = []
    for n in range(1,num+1):
        print(f"Enter country {n} of {num}")
        country = input()
        countries.append(country)

    iRet = Distinct_Values(countries)

    print(f"The distinct values in countries are:{iRet}")
    
   



if __name__ == "__main__":
    main()