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
'''1. Creating strings
customer_name = "John Smith"
country = 'Germany'

Both are valid.

You can also use triple quotes for multiline strings:

message = """
Pipeline started
Records extracted
Pipeline completed
"""
2. String indexing

Each character has a position.

name = "Python"
P  y  t  h  o  n
0  1  2  3  4  5

So:

print(name[0])

gives:

P

And:

print(name[3])

gives:

h

Python also supports negative indexing:

print(name[-1])

Output:

n
print(name[-2])

Output:

o
Important

Python indexing starts at 0, not 1.

3. String slicing

You can extract part of a string.

name = "Python"
print(name[0:3])

Output:

Pyt

The general form is:

string[start:end]

The end position is not included.

For example:

name[0:3]

means:

positions 0, 1, 2
Useful slicing
name[:3]

First 3 characters.

name[3:]

Everything from position 3 onward.

name[:]

Entire string.

You can also use a step:

name[::2]
4. String length

Use:

len()

Example:

customer_name = "John Smith"

print(len(customer_name))

This counts spaces too.

5. Changing case

Very common in data cleaning.

country = "Germany"

print(country.upper())
print(country.lower())

Output:

GERMANY
germany

Also:

name = "john smith"

print(name.title())

Output:

John Smith
6. Removing whitespace

This is extremely important in Data Engineering.

Suppose your source contains:

country = "  Germany  "

Use:

country.strip()

Result:

Germany

You also have:

country.lstrip()

removes whitespace from the left.

country.rstrip()

removes whitespace from the right.

A very common cleaning operation is:

clean_country = country.strip().lower()

For:

"  Germany  "

you get:

germany
7. Replacing values

Use:

replace()

Example:

country = "United States"

country = country.replace(" ", "_")

print(country)

Result:

United_States

Another example:

email = "john@example.com"

email = email.replace("example.com", "company.com")
8. Splitting strings

This is extremely useful when processing raw data.

full_name = "John Smith"

parts = full_name.split(" ")

print(parts)

Output:

["John", "Smith"]

You can then access:

print(parts[0])
print(parts[1])
Data Engineering example

Suppose you receive:

email = "john.smith@gmail.com"

You can extract the domain:

domain = email.split("@")[1]

print(domain)

Result:

gmail.com
9. Joining strings

The opposite of split() is often join().

parts = ["John", "Smith"]

full_name = " ".join(parts)

print(full_name)

Result:

John Smith

Another example:

columns = ["customer_id", "customer_name", "country"]

result = ",".join(columns)

print(result)

Output:

customer_id,customer_name,country

This becomes useful when generating CSV-like data or dynamic SQL.

10. Checking whether a string contains something

Use:

"in"

Example:

email = "john@gmail.com"

print("@gmail.com" in email)

Result:

True

Another example:

country = "Germany"

print("Ger" in country)

Result:

True
11. startswith() and endswith()

Very useful when processing files.

filename = "orders_2026.csv"

print(filename.startswith("orders"))
True

And:

print(filename.endswith(".csv"))
True

For example:

if filename.endswith(".csv"):
    print("Process CSV file")

This becomes very useful when we start working with files.

12. Checking string content

Python gives you useful methods:

text.isdigit()
text.isalpha()
text.isalnum()
text.isspace()

Example:

quantity = "100"

print(quantity.isdigit())

Result:

True

This is useful when validating raw data.

For example:

quantity = "100"

if quantity.isdigit():
    quantity = int(quantity)
13. f-strings ⭐

You absolutely need to master this.

Instead of:

name = "John"
country = "Germany"

print("Customer " + name + " is from " + country)

use:

print(f"Customer {name} is from {country}")

Much cleaner.

You can also calculate inside an f-string:

quantity = 5
price = 20

print(f"Total: {quantity * price}")

Result:

Total: 100
14. Formatting numbers

For Data Engineering and reporting, this is useful.

amount = 123456.789

print(f"{amount:.2f}")

Result:

123456.79

You can also use commas:

print(f"{amount:,.2f}")

Result:

123,456.79
15. Strings are immutable ⭐

This is an important Python concept.

You cannot directly change one character of a string.

This will fail:

name = "John"

name[0] = "B"

Instead, create a new string:

name = "John"

name = "B" + name[1:]

print(name)

Result:

Bohn

Methods such as:

.upper()
.lower()
.strip()
.replace()

do not modify the original string.

They return a new string.

🔥 Data Engineering Example

Imagine a customer record arrives from an API:

customer_name = "  JOHN SMITH "
email = " JOHN.SMITH@GMAIL.COM "
country = " germany "

We want clean data.

customer_name = customer_name.strip().title()
email = email.strip().lower()
country = country.strip().title()

Now:

John Smith
john.smith@gmail.com
Germany

This is exactly the type of transformation you'll eventually perform with Pandas.

'''

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_name = "  sandya duggana  "
#Printing customer_name
print(customer_name)
# Capitalising customer_name
print(customer_name.upper())
# lower case
print(customer_name.lower())
# title
print(customer_name.title())
length
print(len(customer_name))
#removal of extra spaces
print(customer_name.strip())
customer_name= customer_name.strip()
#printing length after space removal
print(len(customer_name))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

email = "  JOHN.SMITH@GMAIL.COM  "
# cleaning the email id
print("before cleaning",email)
email=email.strip().lower()
print("after cleaning",email)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

email = "john.smith@gmail.com"
# extract email domain
email_parts=email.split("@")
print(email_parts)
print("domain is ",email_parts[1])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

customer_id = "DE-CUST-2026-00125"
#extract 2026 and 00125
customer_id_parts= customer_id.split("-")
print(customer_id_parts[2])
print(customer_id_parts[3])


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#File validation
filename = "orders_2026.csv"
if filename.endswith(".csv"):
    print("Process CSV file")
else:
    print('Not a CSV file')


filename = "orders_2026.json"
if filename.endswith(".csv"):
    print("Process CSV file")
else:
    print('Not a CSV file')


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

countries = [
    " germany ",
    "GERMANY",
    " Germany",
    "india ",
    " INDIA"
]

for i in countries:
    i=i.strip().title()
    print(i)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Create cleaned versions
customer_id = " CUST-00125 "
customer_name = "  JOHN SMITH  "
email = " JOHN.SMITH@GMAIL.COM "
country = " germany "
source_file = "customers_2026.csv"

customer_id=customer_id.strip()
customer_name=customer_name.strip().title()
email=email.strip().lower()
country= country.strip().title()

if(source_file.endswith('.csv')):
    print('process the file')
else:
    print("not a csv")

print(f'Customer {customer_id} | {customer_name}|{email} |{country}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
