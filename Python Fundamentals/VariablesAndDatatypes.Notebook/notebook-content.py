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
Level 1 — Variables & Data Types

1. Variables

A variable stores a value:

name = "Sandya"
age = 42
salary = 60000

Python determines the type automatically.

print(type(name))
print(type(age))
print(type(salary))

Output:

<class 'str'>
<class 'int'>
<class 'int'>

2. Main Python data types

String — str
customer_name = "John"
country = "Germany"

Integer — int
customer_id = 101
quantity = 5

Float — float
unit_price = 25.50

Boolean — bool
is_active = True
is_deleted = False

None — NoneType
Used when there is no value.
email = None

This is similar conceptually to SQL NULL, although Python None and SQL NULL behave differently.

3. Type conversion

This is extremely important when processing data.

quantity = "10"
quantity = int(quantity)
print(quantity)
print(type(quantity))

Now:

10
<class 'int'>

Other common conversions:

int("100")
float("25.50")
str(100)
bool(1)

For example, API data may contain:
quantity = "25"
while your database expects an integer.
You need to know how to convert it.

4. Basic arithmetic
quantity = 5
unit_price = 20
total = quantity * unit_price
print(total)

Output:

100

Operators you need:

+       addition
-       subtraction
*       multiplication
/       division
//      floor division
%       remainder
**      power

Example:
total = 105
quantity = 10
average = total / quantity

5. Comparison operators

These are essential for filtering data.

age = 30

age > 18
age < 18
age >= 18
age <= 18
age == 18
age != 18

They return:

True

or:

False

Notice:

=

means assignment

while:

==

means comparison.

This is extremely important.

6. Data Engineering example

Imagine you receive an order:

order_id = 1001
quantity = 4
unit_price = 25.50
discount = 10
shipping_cost = 5

Calculate the order value:

order_value = (
    quantity * unit_price
    + shipping_cost
    - discount
)

print(order_value)

Result:

97.0

'''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Variable Creation and printing
customer_id = 101
customer_name = "John"
country = "Germany"
age = 35
is_active = True

print(customer_id)
print(customer_name)
print(country)
print(age)
print(is_active)
print('datatype of customer_id ',type(customer_id))
print('datatype of customer_name ',type(customer_name))
print('datatype of country ',type(country))
print('datatype of age ',type(age))
print('datatype of is_active ',type(is_active))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#product 
product_id = 501
product_name = "Laptop"
unit_price = 899.99
stock_quantity = 25
is_active = True

inventory_value = unit_price * stock_quantity
print('Product: ', product_name)
print("Inventory Value ",inventory_value)   




# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# order calculation
quantity = 3
unit_price = 150
shipping_cost = 20
discount = 30

order_value = quantity * unit_price + shipping_cost - discount
print("Order Value", order_value)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Type Conversion

quantity = "5"
unit_price = "49.99"

quantity=int(quantity)
unit_price=float(unit_price)

sale_value= quantity* unit_price
print("Sale Value ",sale_value)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Boolean values

is_active = True
stock_quantity = 10
print(is_active)
print(stock_quantity)

is_available = is_active and stock_quantity > 0

print(is_available)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Data Engineering Challenge
#This is typical of raw data coming from an API/CSV where everything may arrive as strings.

order_id = "ORD1001"
customer_id = "C101"
quantity = "4"
unit_price = "125.50"
shipping_cost = "10"
discount = "20"

#converting quantity, unit_price,shipping_cost,discount to int and float
quantity=int(quantity)
unit_price=float(unit_price)
shipping_cost=int(shipping_cost)
discount=int(discount)

# print converted data types 
print("Data type of quantity ", type(quantity))
print("Data type of unit_price ", type(unit_price))
print("Data type of shipping_cost ", type(shipping_cost))
print("Data type of discount ", type(discount))

order_value =quantity * unit_price+ shipping_cost- discount

print('Order Id', order_id)
print('Customer Id', customer_id)
print('Order Value', order_value)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
