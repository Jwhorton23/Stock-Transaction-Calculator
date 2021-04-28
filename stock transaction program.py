# stock transaction program 


# Amount of money paid for stock
stock = float(input('Enter the number of shares purchased: '))
stock_purchase_price = float(input('Enter the amount paid per stock: '))


# display total investment 
initial_investment = stock_purchase_price * stock
print('Initial investment value: ' , initial_investment)


# comission paid to broker when stock was purchased 3% of purchase price 
comission = initial_investment * .03 
print('Comission paid: ' , comission)
total_investment = initial_investment + comission
print('Total investment: ' , total_investment)


# amount stock was sold for 
exit_price = float(input('Enter the price you sold the stock for: '))
exit_stock_amount = float(input('Enter the number of shares sold: '))
exit_value = exit_price * exit_stock_amount
print('Sale of stock value: ', exit_value)


# commission paid on sale of stock 
sale_comission = exit_value * .03
print('Sale comission paid: ' , sale_comission)
value_after_broker_fees = exit_value - sale_comission - comission


# display the amount of money that joe had left after he sold the stock and paid the broker both times 
# if the amount is positive then he made money
final_value = value_after_broker_fees - initial_investment
print('You made: ' , final_value)

