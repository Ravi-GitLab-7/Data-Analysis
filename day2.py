
price = float(input("Enter the price of the product: "))

if price > 500:
    discount = 0.10 * price   
else:
    discount = 0.05 * price  
final_price = price - discount

print(f"Original Price: {price}")
print(f"Discount Applied: {discount}")
print(f"Final Price to Pay: {final_price}")
