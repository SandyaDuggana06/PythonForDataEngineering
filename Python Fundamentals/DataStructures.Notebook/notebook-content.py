# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

'''
Lists
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
Tuples
count()
index()


Sets
add()
update()
remove()
discard()
pop()
clear()


union()
intersection()
difference()
symmetric_difference()


Dictionaries
get()
keys()
values()
items()
pop()
popitem()
update()
clear()
setdefault()
'''


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **Exercise 1**

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
'''
Print all customers.
Print the first and last customer.
Add "Michael".
Remove "John".
Count how many times "Anna" appears.
'''
customers = ["Anna", "Mark", "John", "Sarah", "Anna", "David"]
print(customers)
print(customers[0])
print(customers[-1])
customers.append('Michael')
customers.remove('John')
print(customers)
print(customers.count('Anna'))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Print all product names.
Print all prices.
Calculate the total value.
Find the most expensive product.
Add "headphones": 150.

max(dictionary) → largest key
max(dictionary.values()) → largest value
max(dictionary, key=dictionary.get) → key with the largest value
max(dictionary.items(), key=lambda x: x[1]) → key-value pair with the largest value
'''
products = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "monitor": 300
}

print(products)
print(products.keys())
print(products.values())
products['headphones']=150
print(products)
print(sum(products.values()))

item= max(products, key=products.get)
print(item)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Find all unique countries.
Count the unique countries.
Add "Netherlands".
Remove "Spain".
'''

countries = [
    "Germany", "France", "Germany",
    "Spain", "France", "Italy", "Germany"
]

unique_countries = set(countries)

print(unique_countries)

count_countries = len(unique_countries)
print(count_countries)

countries.append('Netherlands')
countries.remove('Spain')
print(countries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Print each employee's ID and name.
Find the employee with ID "E002".
Count employees.
Add a new employee.

'''

employees = [
    ("E001", "Anna", "Data Engineer"),
    ("E002", "Mark", "Developer"),
    ("E003", "John", "Data Analyst"),
]

# 1. Print each employee's ID and name
for employee_id,name, role in employees:
    print(employee_id,name)

# 2. Find employee with ID "E002"
for employee in employees:
    if employee[0] =='E002':
        print(employee)

# 3. Count employees
print(len(employees))

# 4. Add a new employee
employees.append(("E004", "Sarah", "Designer"))
print(employees)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''

Calculate:

total
average
minimum
maximum
number of transactions above 300'''

transactions = [120, 450, 80, 1200, 50, 300]
print(sum(transactions))
print(sum(transactions)/len(transactions))
print(min(transactions))
print(max(transactions))
trans_above_300 = [trans for trans in transactions if trans >300]
print(trans_above_300)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''

Write a function:

get_customer_name(customer_id)

It should return the customer's name or "Unknown" if the ID doesn't exist.
'''

customers = {
    101: "Anna",
    102: "Mark",
    103: "John",
    104: "Sarah"
}

def get_customer_name(customer_id):
    if customer_id in customers:
        print('id exists')
        print(customers[customer_id])
    else:
        print('unknown')

get_customer_name(101)
get_customer_name(110)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Create a new structure containing only unique order IDs.

Then preserve the original order.
list → set:   set(my_list)
set → list:   list(my_set)
'''
orders = [1001, 1002, 1001, 1003, 1004, 1002, 1005]
unique_orders= set(orders)
print(unique_orders)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
{
    "Electronics": ["Laptop", "Mouse", "Phone"],
    "Furniture": ["Desk", "Chair"]
}
'''

products = [
    ("Laptop", "Electronics"),
    ("Mouse", "Electronics"),
    ("Desk", "Furniture"),
    ("Chair", "Furniture"),
    ("Phone", "Electronics")
]

products_dict= dict(products)
print(products_dict)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


'''
seperate them into valid_transactions
invalid_transactions
'''

transactions = [100, -50, 200, 0, 500, -20]

valid_transactions= [trans for trans in transactions if trans>0]
invalid_transactions= [trans for trans in transactions if trans<=0]
print(valid_transactions)
print(invalid_transactions)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''Use a set to find unique email addresses.

Then determine how many duplicate emails existed.'''


emails = [
    "anna@example.com",
    "mark@example.com",
    "anna@example.com",
    "john@example.com",
    "mark@example.com"
]

emails_set=set(emails)
print(emails_set)
num_of_duplicates= len(emails)-len(emails_set)
print(num_of_duplicates)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Intermediate

# CELL ********************

'''Calculate total spending per customer.
{
    "C001": 550,
    "C002": 300,
    "C003": 450
}
'''

orders = [
    ("O001", "C001", 250),
    ("O002", "C002", 100),
    ("O003", "C001", 300),
    ("O004", "C003", 450),
    ("O005", "C002", 200)
]

totals = {}

for order_id,customer_id,amount in orders:
    # get customer_id and amount
    
    if customer_id in totals:
        totals[customer_id]=totals[customer_id]+amount
    else:
        totals[customer_id] = amount

print(totals)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Customer order count

#Using the same dataset, calculate the number of orders per customer.

orders = [
    ("O001", "C001", 250),
    ("O002", "C002", 100),
    ("O003", "C001", 300),
    ("O004", "C003", 450),
    ("O005", "C002", 200)
]

order_count={}
for order_id,customer_id,amount in orders:
    if customer_id in order_count:
        order_count[customer_id]+=1
    else:
        order_count[customer_id]=1

print(order_count)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Highest-spending customer

Using the orders dataset:

calculate total spending per customer
identify the highest-spending customer
return both customer ID and amount
'''
orders = [
    ("O001", "C001", 250),
    ("O002", "C002", 100),
    ("O003", "C001", 300),
    ("O004", "C003", 450),
    ("O005", "C002", 200)
]


customer_spend ={}

for order_id,customer_id,amount in orders:
    if customer_id in customer_spend:
        customer_spend[customer_id]+=amount
    else:
        customer_spend[customer_id]=amount


print(customer_spend)


max_spend= max(customer_spend.items(), key=lambda x:x[1])
print("Customer who spent the most",max_spend)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''Find:

products with inventory < 10
total inventory
product with highest inventory
product with lowest inventory


'''

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 20,
    "monitor": 5
}

prod_highest_inventory= max(inventory.items(), key=lambda x:x[1])
print(prod_highest_inventory)

prod_lowest_inventory= min(inventory.items(), key= lambda x:x[1])
print(prod_lowest_inventory)

sum_inventory=sum(inventory.values())
print(sum_inventory)

less_inventory=[key for key in inventory if inventory[key]<10]

print(less_inventory)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''create {
    "Data": ["Anna", "John"],
    "Engineering": ["Mark", "David"],
    "HR": ["Sarah"]
}'''

employees = [
    ("E01", "Anna", "Data"),
    ("E02", "Mark", "Engineering"),
    ("E03", "John", "Data"),
    ("E04", "Sarah", "HR"),
    ("E05", "David", "Engineering")
]


dept_dict= {}

for emp_id, emp_name, emp_dept in employees:
    if(emp_dept not in dept_dict):
        dept_dict[emp_dept]=[]
  
    dept_dict[emp_dept].append(emp_name)


print(dept_dict)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''Find:

customers in both systems
customers only online
customers only in stores
all customers

Operation	Symbol	Method
Union	|	.union()
Intersection	&	.intersection()
Difference	-	.difference()
Symmetric difference	^	.symmetric_difference()
Subset	<=	.issubset()
Superset	>=	.issuperset()
'''

online_customers = {"C001", "C002", "C003", "C005"}
store_customers = {"C002", "C003", "C004", "C006"}

customersinbothsystems =set(online_customers)& set(store_customers)
print(customersinbothsystems)

customersonlyonline =set(online_customers)- set(store_customers)
print(customersonlyonline)

customersonlyinstores =set(store_customers)& set(online_customers)
print(customersonlyinstores)

allcustomers =set(online_customers)| set(store_customers)
print(allcustomers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' Find:

records missing from B
records missing from A
records existing in both
total unique records'''
system_a = {1001, 1002, 1003, 1004, 1005}
system_b = {1002, 1003, 1004, 1006}
 
recordsmissinginB=system_a-system_b
recordsmissinginA=system_b-system_a
recordsexistinginboth= system_b&system_a
totaluniquerecords= system_b|system_a
print(recordsmissinginB)
print(recordsmissinginA)
print(recordsexistinginboth)
print(totaluniquerecords)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' Identify duplicate customer IDs.

Then create a deduplicated list.'''

customers = [
    ("C001", "Anna"),
    ("C002", "Mark"),
    ("C001", "Anna"),
    ("C003", "John"),
    ("C002", "Mark")
]
seen = set()
duplicates = set()
deduplicated = []


for customer_id,name in customers:
    if customer_id in seen:
        duplicates.add(customer_id)
    else:
        seen.add(customer_id)
        deduplicated.append((customer_id, name))

print("Duplicate IDs:", duplicates)
print("Deduplicated:", deduplicated)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' categorise <100       → small
100–499    → medium
500+       → large '''

transactions = [
    ("T001", 50),
    ("T002", 250),
    ("T003", 1000),
    ("T004", 25),
    ("T005", 700)
]
trans_dict={"small":[],
"medium":[],
"large":[]}

for trans_id, amount in transactions:
    if amount < 100:
        trans_dict['small' ].append(amount)
    elif amount>=100 and amount <=499:
        trans_dict['medium'].append(amount)
    else:
        trans_dict['large'].append(amount)

print(trans_dict)   



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' Customer 360 dictionary
 {
    "C001": {
        "name": "Anna",
        "country": "Germany"
    },
    ...
}'''

customers = [
    ("C001", "Anna", "Germany"),
    ("C002", "Mark", "France"),
    ("C003", "John", "Germany")
]

customer_360={}

for customer_id, customer_name , customer_country in customers:
    customer_360[customer_id]= {
        "name": customer_name,
        "country": customer_country
    }

print(customer_360)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Advanced

# CELL ********************

''' Order/customer join using dictionaries Create enriched orders:
[
    ("O001", "Anna", 500),
    ("O002", "Mark", 200),
    ("O003", "Anna", 300),
    ("O004", "UNKNOWN", 100)
] '''
customers = {
    "C001": "Anna",
    "C002": "Mark",
    "C003": "John"
}
orders = [
    ("O001", "C001", 500),
    ("O002", "C002", 200),
    ("O003", "C001", 300),
    ("O004", "C999", 100)
]


enriched_orders=[]

for order_id,customer_id,amount in orders:
    customer= customers.get(customer_id,"unknown")
    enriched_order = {
    "order_id": order_id,
    "customer_id": customer_id,
    "name": customer,
    "amount": amount}
    enriched_orders.append(enriched_order)

print(enriched_orders)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Build a data-quality report showing:

missing IDs
missing names
duplicate IDs
valid records
invalid records
'''

customers = [
    {"id": "C001", "name": "Anna"},
    {"id": "C002", "name": None},
    {"id": None, "name": "John"},
    {"id": "C002", "name": "Mark"},
    {"id": "C004", "name": "Sarah"}
]

invalid_cust=[]
for customer in customers:
    if(customer["id"] is None or customer["name"] is None):
        invalid_cust.append(customer)
print("invalid customers are ", invalid_cust)

missing_ids=[]
for customer in customers:
    if customer["id"] is None:
        missing_ids.append(customer)
print("customers with missing ids",missing_ids)

missing_names = []
for customer in customers:
    if customer["name"] is None:
        missing_names.append(customer)
print("customers with missing names",missing_names)

seen = set()
duplicates = set()

for customer in customers:
    customer_id = customer["id"]

    if customer_id in seen:
        duplicates.add(customer_id)
    else:
        seen.add(customer_id)


print("customers which are not duplicates ",seen)
print("customers which are duplicate ", duplicates)

valid_records=[]

for customer in customers:
    if customer["id"] is not None and customer["name"] is not None:
        valid_records.append(customer)

print("valid customers are  ",valid_records)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''
Deduplicate using email as the business key.

Keep the latest record.

'''
customers = [
    {"id": 1, "email": "a@test.com", "name": "Anna"},
    {"id": 2, "email": "b@test.com", "name": "Mark"},
    {"id": 3, "email": "a@test.com", "name": "Anna Updated"}
]

deduplicated = {}

for customer in customers:
    email = customer["email"]
    deduplicated[email] = customer

print(deduplicated)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' calculate product
total_quantity
total_revenue'''

sales = [
    ("Laptop", 2, 1200),
    ("Mouse", 10, 25),
    ("Laptop", 1, 1200),
    ("Keyboard", 5, 80),
    ("Mouse", 3, 25)
]

product_sales={}

for product, quantity,price in sales:
    if product not in product_sales:
        product_sales[product]={
            "total_quantity":0,
            "total_revenue":0
        }
        
        product_sales[product]["total_quantity"]+=quantity
        product_sales[product]["total_revenue"]+=quantity*price

print(product_sales)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' Calculate average salary by department.

Then identify the highest-paid employee in each department.'''

employees = [
    {"id": "E01", "name": "Anna", "department": "Data", "salary": 70000},
    {"id": "E02", "name": "Mark", "department": "Data", "salary": 80000},
    {"id": "E03", "name": "John", "department": "HR", "salary": 60000},
    {"id": "E04", "name": "Sarah", "department": "HR", "salary": 65000},
]

salary_total={}
employee_count={}
average_salary={}

for employee in employees:
    department=employee['department']
    salary=employee['salary']
    if department not in salary_total:
        salary_total[department]=salary
        employee_count[department]=1
    else:
        salary_total[department]=salary_total[department]+salary
        employee_count[department]=employee_count[department]+1
    
for department in salary_total:
    average_salary[department]=salary_total[department]/employee_count[department]

print("average salary in department",average_salary)

highest_paid={}



for employee in employees:
    department=employee['department']
    salary= employee['salary']
    employee_id= employee['id']
    name=employee['name']
    if department not in highest_paid:
        
        highest_paid[department]={
            "id":employee_id,
            "name":name,
            "salary":salary

        }
        
    elif salary > highest_paid[department]['salary']:
        highest_paid[department]={
             "id":employee_id,
            "name":name,
            "salary":salary

        }
    
      
print("highest paid employees are " ,highest_paid)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Multi-source reconciliation
'''  Determine:
customers in all three
customers in exactly two
customers appearing in only one system
master customer set '''

crm = {"C001", "C002", "C003", "C004"}
erp = {"C002", "C003", "C005"}
website = {"C001", "C003", "C006"}

all_three = crm & erp & website

exactly_two = (
    (crm & erp) |
    (crm & website) |
    (erp & website)
) - all_three

print(all_three)
print(exactly_two)

master = crm | erp | website
only_one = master - (
    (crm & erp) |
    (crm & website) |
    (erp & website)
)

print(only_one)

print(master)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **The pattern to remember ⭐
# When you want a dictionary of lists:
# data = {}
# 
# if key not in data:
#     data[key] = []
# 
# data[key].append(value)
# **

# CELL ********************

''' Transaction fraud detection
Flag transactions where:
amount > 1000
then produce
{
    customer_id: {
        "total_transactions": ...,
        "total_amount": ...,
        "fraud_count": ...
    }
}
'''
transactions = [
    {"customer": "C001", "amount": 100},
    {"customer": "C001", "amount": 150},
    {"customer": "C001", "amount": 5000},
    {"customer": "C002", "amount": 200},
    {"customer": "C002", "amount": 7000}
]

fraud_transactions={}
for transaction in transactions:
    customer= transaction['customer']
    amount= transaction['amount']
    if amount >1000:
        if customer not in fraud_transactions:
            fraud_transactions[customer]=[]
        fraud_transactions[customer].append(transaction)          
print("fraud transactions are ",fraud_transactions)

customer_report={}

for transaction in transactions:
    customer= transaction['customer']
    amount=transaction['amount']
    if customer not in customer_report:
        customer_report[customer]={
            "total_transactions":0,
            "total_amount":0,
            "fraud_count":0
        }
    
    customer_report[customer]["total_transactions"]=customer_report[customer]['total_transactions']+1
    customer_report[customer]["total_amount"]=customer_report[customer]['total_amount']+amount
    if amount > 1000:
            customer_report[customer]["fraud_count"] += 1

print(customer_report)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

'''Build a mini ETL pipeline
Extract
   ↓
Validate
   ↓
Deduplicate
   ↓
Transform
   ↓
Load
remove duplicates
reject negative amounts
calculate a 19% VAT field
produce clean records
produce rejected records
'''
orders = [
    {"id": 1, "customer": "C001", "amount": 100},
    {"id": 2, "customer": "C002", "amount": -50},
    {"id": 3, "customer": "C001", "amount": 300},
    {"id": 2, "customer": "C002", "amount": -50}
]

reject=[]
valid=[]

for order in orders:
    id=order['id']
    customer=order['customer']
    amount=order['amount']
    
    if amount<0:
        reject.append(order)
    else:
        valid.append(order)


#Deduplicate

seen=set()
clean_records=[]

for order in valid:
    if order['id'] not in seen:
        seen.add(order['id'])
        clean_records.append(order)
    

for order in clean_records:
    order["VAT"] = order["amount"] * 0.19

print("Clean records:", clean_records)
print("Rejected records:", reject)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

''' Incremental processing
Identify only new records.

Then extend the processed ID set.

Think about why a set is better than a list for this operation.

incremental data processing / ETL pipelines
new = set(incoming) - processed
processed.update(new)'''


processed_ids = {1001, 1002, 1003}

incoming_ids = [1002, 1003, 1004, 1005, 1006]

new_ids=set(incoming_ids)-processed_ids
print("new ids are ",new_ids)

processed_ids.update(new_ids)
print("processed ids are ", processed_ids)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
