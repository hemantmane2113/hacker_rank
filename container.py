from collections import Counter

def Calculate_Price(shoe_size_with_price,shoe_size):
    

    stock = Counter(shoe_size)#thing tp learn
    print(stock)

    Total_price = 0

    for size,price in shoe_size_with_price:
        if stock[size]>0:
            Total_price = price + Total_price
            stock[size] = stock[size] -1

    return Total_price

  
def main():

    print("Enter the quantity of shoes: ")
    quantity = int(input())

    print("Enter the shoe sizes available: ")
    shoe_size = list(map(int,input().split()))

    print("Enter the total cutomer numbers; ")
    customer_number = int(input())

    print("Now enter the size and price of the shoe: ")
    size_price = []
    for i in range(1,customer_number+1):
        sizeandprice = list(map(int,input().split()))
        size_price.append(sizeandprice)

    print("qunatity:",quantity)
    print("shoe_size:",shoe_size)
    print("customer_number:",customer_number)
    print("Size&price:",size_price)

    iRet = Calculate_Price(size_price,shoe_size)

    print("The total price of the shoes is: ",iRet)





if __name__ == "__main__":
    main()