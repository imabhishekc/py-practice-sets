"""
You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
"""

stock_prices = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160],
}

def print_operation():
    for stock_name, price_list in stock_prices.items():
        total = sum(price_list)
        average = total / len(price_list)
        print(f"{stock_name} ==> {price_list} ==> avg: {average:.2f}")


def add_operation():
    stock = input("Enter what stock you want to add: ")

    try:
        new_price = float(input(f"Enter price to add for {stock}: "))
        if stock in stock_prices:
            stock_prices[stock].append(new_price)
            print(f"Updated prices for {stock}: {stock_prices[stock]}")

        else:
            stock_prices[stock] = [new_price]
            print(f"{stock} ==> {stock_prices[stock]}")
    
    except ValueError:
        print("Invalid value entered. Please input number.")    


def main():
    prompt = input("Enter what you would like to do? 'print' to print stock prices, 'add' to add new data: ")

    if prompt == 'print':
        print_operation()
    
    elif prompt == 'add':
        add_operation()

main()