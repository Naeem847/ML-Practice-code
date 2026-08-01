message="learning python is fun!!"
print(f"message: {message}")
x=12
y="hello world!"
z=3.14
print(f"x:{x},type of x:{type(x)}")
print(f"y:{y},type of y:{type(y)}")
print(f"z:{z},type of z:{type(z)}")
# basic arithmetic operations
a=10
b=5
print(f"a+b={a+b}")
print(f"a-b={a-b}")
print(f"a*b={a*b}")
print(f"a/b={a/b}")

# intiger datatypes
integer_variable=10
negative_integer_variable=-5
large_integer_variable=1000000000
print(f"integer_variable: {integer_variable}, type: {type(integer_variable)}")
print(f"negative_integer_variable: {negative_integer_variable}, type: {type(negative_integer_variable)}")
print(f"large_integer_variable: {large_integer_variable}, type: {type(large_integer_variable)}")
# floating point numbers
float_variable=3.14
negative_float_variable=-2.5
scientific_variable=3e4
print(f"float_variable: {float_variable}, type: {type(float_variable)}")
print(f"negative_float_variable: {negative_float_variable}, type: {type(negative_float_variable)}")
print(f"scientific_variable: {scientific_variable}, type: {type(scientific_variable)}")
# Strings (str)
# string is a sequence of characters enclosed in single or double quotes
string_variable="Hello, World!"
string_variable2='Python is fun!'
multiple_line_string="""This is a multi-line string.
It can span multiple lines."""
print(f"string_variable: {string_variable}, type: {type(string_variable)}")
print(f"string_variable2: {string_variable2}, type: {type(string_variable2)}")
print(f"multiple_line_string: {multiple_line_string}, type: {type(multiple_line_string)}")
# string cancatination
full_name="John"+" "+"Doe"
print(f"full_name: {full_name}, type: {type(full_name)}")
# complex numbers
complex_variable=2+3j
another_complex_variable=1-2j
print(f"complex_variable: {complex_variable}, type: {type(complex_variable)}")
print(f"real part of complex_variable: {complex_variable.real}, imaginary part of complex_variable: {complex_variable.imag}")
print(f"another_complex_variable: {another_complex_variable}, type: {type(another_complex_variable)}")
# boolean values
# boolean represents truth values and can be either True or False
boolean_variable=True
boolean_variables=False
print(f"boolean_variable: {boolean_variable}, type: {type(boolean_variable)}")
print(f"boolean_variables: {boolean_variables}, type: {type(boolean_variables)}")
# boolean operations
a=True
b=False
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")