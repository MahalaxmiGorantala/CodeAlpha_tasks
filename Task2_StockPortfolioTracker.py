stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found!")

print("Total Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))

print("Result saved in portfolio.txt")