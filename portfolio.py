stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 320
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("Enter Stock Name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter Quantity: "))
        value = stocks[stock] * qty
        total += value
        print(f"{stock} Value = ${value}")
    else:
        print("Stock Not Found!")

print("\nTotal Investment = $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment = ${total}")

print("Portfolio saved in portfolio.txt")