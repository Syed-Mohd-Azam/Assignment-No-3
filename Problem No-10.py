# Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.
x,y='0o25','0x39'
print("Binary format of addition of two numbers (25 in octal and 39 in hexadecimal ) is : ",bin(int(x,8)+int(y,16)))