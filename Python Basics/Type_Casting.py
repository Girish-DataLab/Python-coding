# Type Casting
# Type casting is the process of converting one data type into another data type.

/* Integer to float */ 
# Converting an integer value into a string using the str() function.

x = 5
y = float(x)
print(y)
print(type(y))

#  5.0
<class 'float'>

/* Float to Integer */
# Converting a float value into an integer using the int() function (decimal part is removed).

a = 12.9
b = int(a)
print(b)
print(type(b))

#  12
<class 'int'>

/* Integer to string */

age=20
age_str=str(age)
print(age_str)
print(type(age_str))

#  20
<class 'str'>

/* String to Integer */
# Converting a numeric string into an integer using the int() function.

num="100"
num_int=int(num)
print(num_int)
print(type(num_int))

#  100
<class 'int'>

/* String to Float */
#Converting a numeric string with decimals into a float using the float() function.

value = "45.6"
value_float = float(value)
print(value_float)
print(type(value_float))

#  45.6
<class 'float'>


/* Combined Example */                          
   # Type casting 

student_name = "Girish"
roll_no = 12
marks = 85.5
passed = True

roll_no_str = str(roll_no)
marks_int = int(marks)

print("Student Name:", student_name)
print("Roll Number:", roll_no_str)
print("Marks:", marks_int)
print("Passed:", passed)

#   Student Name: Rahul
    Roll Number: 12
    Marks: 85
    Passed: True

# Another Example

product = "Laptop"
price = 55000
discount = 10.5
available = False

final_price = price - int(discount)

print("Product:", product)
print("Price:", price)
print("Discount:", int(discount))
print("Available:", available)
print("Final Price:", final_price)

#  Product: Laptop
   Price: 55000
   Discount: 10
   Available: False
   Final Price: 54990



