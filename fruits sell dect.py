#Create a dic of 5 fruits, where fruit name is the key and its price is value, assume that your have 5 items of each fruits
# then determine how much money you will earn if you sell all the fruits. 

fruits = {'Apple':8, 'Guava':6, 'Orange':5.5, 'Mangoe':7, 'Pear':4.5}
total_earnings = 0
for fruit, price in fruits.items():
    total_earnings += price * 12
    print("Total Earnings: ", total_earnings)
