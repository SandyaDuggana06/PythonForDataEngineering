# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
'''
You will encounter lists everywhere:

customers = [...]
orders = [...]
files = [...]
columns = [...]
api_records = [...]
1. Creating a list
customers = [
    "John",
    "Mary",
    "David"
]

You can access elements using indexes:

print(customers[0])

Output:

John
2. List indexing
orders = [1001, 1002, 1003, 1004]
print(orders[0])
print(orders[2])
print(orders[-1])

Result:

1001
1003
1004

Same indexing concept as strings.

3. List slicing
orders = [1001, 1002, 1003, 1004, 1005]
print(orders[0:3])

Result:

[1001, 1002, 1003]
4. Adding elements
append()
orders = [1001, 1002]

orders.append(1003)

print(orders)

Result:

[1001, 1002, 1003]
insert()
orders.insert(0, 999)
5. Removing elements
orders.remove(1002)

Or:

orders.pop()

pop() removes the last element.

You can also:

orders.pop(1)

to remove the element at index 1.

6. List length
len(orders)

Very useful when checking how many records you received from an API:

print(f"Received {len(orders)} records")
7. Checking membership
if 1003 in orders:
    print("Order exists")

Very useful for validation.

Transformation
[expression for item in list]

Transformation + filtering
[expression for item in list if condition]

'''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#print First product Last product and Number of products

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

print(products)
#print(f'first product is {products[0]} last product is {products[-1]} and length of products is {len(products)}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ADD Headphones
products.append('head phones')
print(products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#remove mouse
products.remove('Mouse')
print(products)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#create a list and print first price, last price, first 3 prices, number of prices

prices = [100, 250, 75, 500, 120]

print(f'first price is {prices[0]}')
print(f'last price is {prices[-1]}')
print(f'first 3 prices are {prices[0:3]}')
print(f'Number of prices are {len(prices)}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Data engineering exercise
#create a new list cleaned countries

countries = [
    " germany ",
    "GERMANY",
    " India ",
    "INDIA",
    " france "
]

cleaned_countries=[]

for country in countries:
    cleaned_country=country.strip().title()
    cleaned_countries.append(cleaned_country)
print(cleaned_countries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# try ,except blocks
raw_prices = [
    "100.50",
    "250",
    "75.25",
    "invalid",
    "500"
     ]
valid_prices=[]
for price in raw_prices:
    try:

        price=float(price)
        valid_prices.append(price)
    
    except ValueError:
        price=0

print(valid_prices)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#list comprehensions
numbers = [1, 2, 3, 4, 5]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)
    
# using list comprehension

squared_numbers=[number **2 for number in numbers]
print(squared_numbers)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#cleaning names using list comprehensions
raw_names = [
    " john smith ",
    "MARY JONES",
    " david brown ",
    "SARAH WILSON"
]

cleaned_names=[ name.strip().title() for name in raw_names]
print(cleaned_names)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Create a list containing only the valid numeric values.
raw_quantities = [
    "10",
    "25",
    "invalid",
    "50",
    "100"
]

valid_quantities =[ quantity for quantity in raw_quantities if(quantity.isdigit())]
print(valid_quantities)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

amounts = [100, -50, 250, 0, 75, -20, 300]

valid_amounts=[amount for amount in amounts if amount>0]
print(valid_amounts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_amounts = [
    "100",
    "250",
    "invalid",
    "75",
    "abc",
    "500"
]

valid_amounts=[int(amount) for amount in raw_amounts if amount.isdigit()]
print(valid_amounts)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_names = [
    " john smith ",
    "",
    "MARY JONES",
    "   ",
    "david brown",
    "SARAH WILSON",
    " "
]

cleaned_names= [ name.strip().title() for name in raw_names if name.strip()]

print(cleaned_names)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_quantities = [
    "10",
    " 25 ",
    "invalid",
    "",
    " 50",
    "abc",
    "100 "
]

valid_values =[int(value.strip()) for value in raw_quantities if value.strip().isdigit()]

print(valid_values)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_prices = [
    "100.50",
    "250",
    " 75.25 ",
    "invalid",
    "",
    "500.75"
]

def is_valid_price(value):
    try:
        float(value.strip())
        return True
    except ValueError:
        return False

valid_prices =[ float(price.strip()) for price in raw_prices if is_valid_price(price)]



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_quantities = [
    "10",
    "25",
    "invalid",
    "50",
    "100"
]

new_quantities = [int(value) for value in raw_quantities if value.isdigit()]
print(new_quantities)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_amounts = [
    "100.50",
    "250",
    "invalid",
    " 75.25 ",
    "",
    "500.75",
    "abc"
]

def clean_amount(amount):
   try:
    return float(amount.strip())
    
   except ValueError:
    return None

new_values =[value 
for value in [clean_amount(amount) for amount in raw_amounts]
if value is not None]
print(new_values)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_ages = [
    "25",
    " 30 ",
    "invalid",
    "42",
    "",
    "35",
    "unknown"
]

def clean_ages(value):
    try:
        return int(value.strip())
    except ValueError:
        return None

cleaned_ages =[age 
for age in [clean_ages(value) for value in raw_ages]
if age is not None

]
print(cleaned_ages)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_scores = [
    "95",
    " 88 ",
    "invalid",
    "72",
    "",
    "100",
    "abc",
    " 65 "
]

def clean_scores(value):
    try:
        return int(value.strip())
    except:
        return None
score_value =[clean_scores(value) for value in raw_scores]
clean_scores= [score for score in score_value if score is not None]
print(clean_scores)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_ages = [
    "25",
    " 17 ",
    "42",
    "invalid",
    "65",
    "0",
    " 30 ",
    "-5"
]

def clean_scores(value):
    try:
        return int(value.strip())
    except:
        return None
score_value =[clean_scores(value) for value in raw_ages]
clean_scores= [score for score in score_value if score is not None and score >=18]
print(clean_scores)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
