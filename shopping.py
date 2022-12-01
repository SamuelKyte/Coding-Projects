product_1 = input('Please enter the name of a product: ')
price_product_1 = input('Please enter the price of this product(i.e. 1.00): ')
price_product_1 = float(price_product_1)
product_2 = input('Please enter the name of a second product: ')
price_product_2 = input('Please enter the price of this product(i.e. 1.00): ')
price_product_2 = float(price_product_2)
product_3 = input('Please enter the name of a third product: ')
price_product_3 = input('Please enter the price of this product(i.e. 1.00): ')
price_product_3 = float(price_product_3)
total = price_product_1 + price_product_2 + price_product_3
avg_price = (price_product_1 + price_product_2 + price_product_3) / 3
print(f'The total cost of {product_1}, {product_2}, and {product_3} is R {str(total)} and the average price of the items is R {avg_price}.')