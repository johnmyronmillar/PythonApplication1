print ('Hello World')

# 2-18
# Get the desired future value
future_value = float(input('Enter the desired future value: '))
# Get the annual interst rate
rate = float(input('Enter the annual interest rate: '))
# Get the number of years that the money will appreciate.
years = float(input('Enter the number of years the money will grow: '))
# Calculate the amount needed to deposit
present_value = future_value / (1.0 + (rate/100))**years
# Display the amount needed to deposit
present_value = '${:,.2f}'.format(present_value)
print('You will need to deposit the amount:', present_value)
