n_customers = int(input('Enter number of customers: '))
total_income = 0
for i in range(1, n_customers + 1):
    print(f'Customer {i}')
    buying = True
    total_payment = 0
    while buying:
        product = input('Enter product name: ')
        price = float(input('Enter price: '))
        quantity = int(input('Enter quantity: '))
        payment = price * quantity
        total_payment += payment
        print(f'Payment for {product}: {payment}')

        answer = input('Do you want to buy more (y/n): ')
        buying = answer == 'y'
    
    print(f'Total payment: {total_payment}')
    total_income += total_payment

print(f'Total income: {total_income}')