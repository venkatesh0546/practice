# -*- coding: utf-8 -*-
"""BAISIC PROGRAMS IN PYTHON

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mVOuk61-eHZmeg-edPVhNRKNYw0B-Z3w
"""

a=int(input())                        # user input value
if a > 0:                                 #condition
  print("given number is positive")             #print statement
elif a < 0:                                        #elif above condition is not true otherwise " elif " is checking the statement
  print("given number is negative")
else:                                                 #the above " if " and " elif " is not true otherwise " else " is executed
  print("given value is zero")

n=int(input())
if n>0:
  print("given value is positive")
elif n<0:
  print('given value is negative')
else:
  print('given value is zero')

"""# **Given number is positive or negative or zero**"""

a=int(input())            # user input value
if a > 19:                    #condition
  print("he is elgible ")
elif a < 18:                     #elif above condition is not true otherwise " elif " is checking the statement
  print("he is not elgible")

"""# **The person are elgible to vote**"""

a=int(input())
b=int(input())
c=int(input())
if a > b and a > c:
  print("a is greater than b")
elif b > c and b > a:
  print(" b is greater c")
else:
  print(" c is largest number")

"""# **Largest **number** **"""

year=int(input("enter the number"))    #user input value
if((Year % 400 == 0) or                  # conditon
   (Year % 100 != 0) and
   (Year % 4 == 0)):
  print(" given year is leap year")          #print statement
else:                                            # we else condition an if condition is not true then else conditon will execute
  print(" given year is not leap year")               #print statement

n=int(input())
if ((n%400==0)or
    (n%100!=0)and
    (n%4==0)):
    print("given value is leap year")
else:
  print('given value is not leap year')

"""## ***Leap year ***"""

celcius=32
fahrnhit = (celcius *  1.8) + 32
print("%.2f celsius = %.2f fahrnhit"%(celcius,fahrnhit))

"""# **celsius to convert farhnhit**"""

for x in "prabhs":
  print(x)

balence= 3000
print("welcome to ATM name is SBI")
print("pleasen select an option")
print("1.balence")
print("2.withdra")
print("3.deposit")
print("4.thank you for using the ATM . bye")
while True:
 option=input("enter your choice(1-4).")
 if option == "1":
  print("your balence is $",balence)
 elif option == "2":
  amount = float(input("Enter the amount to withdraw: "))
 if amount > balence:
  print("funds is insufficiant")
  balence -= amount
  print("withdraw succesfully. remaining balence is $",balence)
 elif option == "3":
  amount=float(input("enter the amount to deposit"))
  balence+=amount
  print(" deposit succesfully. current balence $",balence)
 elif option == "4":
  print("Thank you for using the ATM.bye")
  break
 else:
  print("Invalid option. Please select a valid option.")

n=int(input())
m=int(input())
o='+-*/'
o_1='//'
o_2='**'

h=input()
if h==o[0]:
  print("{} + {} =".format(n,m),n+m)
elif h==o[1]:
  print(n-m)
elif h==o[2]:
  print(n*m)
elif h==o[3]:
  print(n/m)
elif h==o_1:
  print(n//m)
elif h==o_2:
  print(n**m)

import keyword

# Get all keywords
keywords = keyword.kwlist

# Pprint the keywords
for key in keywords:
    print(key)

a=int(input())
b=int(input())
if a > b:
  print("a is greater  b")
elif b > a:
  print("b is greater a ")

name="venkatesh"
age=22
print("name is {} and i am {} years old".format(name,age))

n=int(input())
# 'True Statement' if (condition) else 'False Stateme'
x= "even" if (n%2==0) else "mulitliple of 4" if (n%4==0) else "odd"   #odd
print(x)

n=int(input())
if n%2==0:
  print('given value is even')
else:
  print('given value is odd')

n=int(input())
a= "positive" if (n>1) else "negative"
print(a)

n=int(input()) # 'nput value given the user'
# 'true statement' if (conditin) else 'false statement'
a= "even" if (n%3) else "odd"
print(a)

hours=input("enter hours")
rateperhr = 5
print("your total rate is",int(hours*rateperhr))

Syntax of if-else:

if <exprression>:
    <statement>
    <statement>
else:
    <statement>
    <statement>

a = int(input("enter a number"))
b = int(input("enter another number"))
if a > b:
  print(" first number is largest")
else:
  print("second number is largest")

n1=int(input())
n2=int(input())

if n1>n2:
  print('given value is lorgest number')
else:
  print('given value is smalest number')



"""# **largest number**"""

amount=10000
print("welcome to ATM")
print("chooose your choice")
print("1.withdraw ")
print("2.deposit")
print("3.check balence ")
print("4.quite")
print("thank you using my ATM ")
option = input("choose your option(0-4)")
balance=1000
if option == "1":
  amount=int(input("enter the amount to witdraw"))
  if amount <= balance:
    balance=balance-amount
    print(f"amount withdrawl {amount} succesfully and the {balance}")

"""# **ATM withdraw program**"""

amount=10000
print("welcome to ATM")
print("chooose your choice")
print("1.withdraw ")
print("2.deposit")
print("3.check balence ")
print("4.quite")
print("thank you using my ATM ")
option = input("choose your option(0-4)")
balance=1000
if option == "1":
  amount=int(input("enter the amount to witdraw"))
  if amount <= balance:
    balance=balance-amount
    print(f"amount withdrawl : {amount} succesfully and the balance is : {balance}")
  else:
      print("Insufficient funds")
   #balance=balance
elif (option=='2'):
    amount=int(input("Enter your amount:"))
    balance=balance+amount
    print(f"Amount {amount} added Succesfully and the balance is {balance}")
elif option=='3':
    print(f"Remaining balance: {balance}")
elif option=='4':
    exit()
print("Thank you using my ATM")

"""# **palindrome program**"""

str = "JaVaJ"
str = "doo"

# This string is reverse.
rev = reversed(str)

if list(str) == list(rev):
   print("DOOR!")
else:
   print("NOT PALINDROME !")

str='mom'
str='annaa'
rev=reversed(str)
if list(str)==list(rev):
  print('given value is palindrome')
else:
  print('given value is not palindrome')

str = "MOM"
str = "dad"
rev = reversed(str)
if list(str) == list(rev):
  print("palindrome")
else:
  print("not palindrome")

string=input(("Enter a letter:"))
if(string==string[::-1]):
      print("The letter is a palindrome")
else:
      print("The letter is not a palindrome")

str=input("enter the string")
if (str==str[::-1]):
  print('is palindrome')
else:
  print('is not palindrome')

a="Venkatesh"
print(a[::-6])

a='prabhas'
print(a[::-1])

print(len("venkatesh"))

str=input(" ")
length=len(str)
print(length)

"""# **Slicing**
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""

a="venkatesh"
b="die hard fan of"
c="prabhas"
print(a[::2])
print(b[:8:4])
print(c[0:-1])

a="die hard fan of"
print(len(a))

"""# **new line create**"""

print("venkatesh\n prabhas")

"""# **FOR LOOPING**"""

list=[1,2,3,4,5,6,7,8,9]
for x in list:
  print(x)

for i in range (6,0,-1):
  for j in range(i,0,-1):
    print('*',end="")
  print()

"""# **each name separate**"""

str=["jai","shree","ram"]
for i in str:
  print(i)

st=[]
str=["venkatesh","mahendra"]
for i in str:
  for x in i:
    print(x)

"""# **range of (1,10)**"""

for i in range(1,10):
  print(i)

"""# **the even numbers for loop**"""

for i in range(1,20):
  if i%2==0:
    print(i)

"""# **sum of all numbers** 1 to **100**"""

a=0
for i in range(1,100):
  a=a+i
print(a)

a=0
for i in range (1,1000):
  a=a+i
print(a)

"""## product(*) of the all numbers bold text **bold text**"""

a=1
for i in range(1,10):
  a=a*i
print(a)

a=1
for i in range(1,10):
  a=a*i
print(a)

"""# **step for loop**"""

for i in range(1,10,2):
  print(i)

for i in range(1,100,10):
  print(i)

str=["venkatesh","mahendra"]
for i in str:
  print(i)

"""# **character by charecter in nested for loop**"""

str=[]
str="venkatesh","prabhas"
for i in str:
  for str in i:
    print(str)

for i in range(0,100,20):
    print(i)

"""# **quation ** : Write a short program that prints each number from 1 to 100 on a new line.

For each multiple of 3, print "Fizz" instead of the number.

For each multiple of 5, print "Buzz" instead of the number.

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number
"""

a=int(input())
print("\n")
for a in range (0,20):
  if a %2==0 and a%5==0:
    print('venkateshpranhas')
  elif a%2==0:
    print('venkatesh')
  elif a%5==0:
    print('prabhas')
  else:
    print(a)

a=int(input())

print("\n")
for num in range(1,100):
  if num % 3==0 and num % 5==0:
    print("Fizzbuzz")
  elif num % 3==0:
    print("fizz")
  elif num % 5==0:
    print("buzz")
  else:
    print(num)

a=int(input())
if 1<a<=100:
  print(a*10)
elif 100<=200:
  print(a*15)
elif 200<=300:
  print(a*20)

"""# **for loop syntax**

for val in sequence:
    # statement(s)
"""

languages = ['Swift', 'Python', 'Go', 'JavaScript']

# run a loop for each item of the list
for language in languages:
    print(language)

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

names="venkatesh","prabhas"
for x in names:
  print(x)
else:
  print("no name is there")

year=200
if

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

heros=["prabhas","rana"]
heroins=["anushka","trisha"]
for i in heros:
  for j in heroins:
    print(i,j)

for i in range(0,2000,100):
  print(i,"\n")

def print_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

print_pyramid(5)

def print_pyramid(row):
  for i in range(row):
    print(' '*(row-i-1)+"*"*(2*i+1))
print_pyramid(10)

n=int(input()) #user input
for i in range(n):
  for j in range(i+1):  #(i+1) this is the condition
    print("*",end="") # end parameter using in new line insert of print value
  -print()

for i in range(5):
  for j in range(i+1):
    print("*",end="")
  print()

for i in range(5,0,-1):
  for j in range(i,0,-1):
    print("*",end="")
  print("\n")

var="python"
for i in var:
  if i=='t' or i=='n':
    continue
    print(i)
  print(i)

var="python"
for i in var:
  if i=='t' or i=='n':
    print(i)
    continue
  print(i)

for i in range(10):
  if i== '5':
    continue
    print(i)
  print(i) # range is zero because range is low and the conditon will check given i value is high

n=int(input())
for i in range(n):
  for j in range (n-i-1):
    print(" ",end="")
  for j in range (2*i+1):
    print("*",end="")
  print()

num=5
while num <=100:
  print(num)
  num+=5

"""# **for loop series**"""

for i in range(0,300,10): #3
  print(i,end=" ")

"""# **revers numbers in for loop**"""

for i in range(10,0,-1):
  print(i,end=" ")

"""# **revers numbers in while loop**

"""

num = 123456789
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

"""# **even  numbers in while loop*
 1 . Write a program to print the following using while loop

a. First 10 Even numbers

b. First 10 Odd numbers

c. First 10 Natural numbers

d. First 10 Whole numbers

"""

num=0
while num<=10:
  if num%2==0:
    print(num)
  num+=1

"""# **ord numbers in while loop**"""

num=23
while num<=90:
  if num%3==0:
    print(num)
  num+=1

"""# **natural numbers in while loop**"""

n=int(input("enter the number"))
n1=0
n2=1
count=2
if n < 0:
  print("enter only +ve values")
elif n==1:
  print(n1)
else:
  print(n1)
  print(n2)
  while count<n:
    n3=n1+n2
    print(n3)
    count+=1
    n1=n2
    n2=n3

"""# **whole numbers in while loop**"""

num=1
while num<=10:
  if num%1==0:
    print(num)
  num+=1      #increament is there

"""4 . Write a while loop statement to print the following series :

105, 98, 91,......7.

"""

num=7
while num <=105:
  print(num,end=" ")
  num+=7

a=int(input())

print("\n")
for num in range (1,101):
  if num % 3==0 and num % 5==0:
    print("fizzbuzz")
  if num % 3==0:
    print("fizz")
  elif num % 5==0:
    print("buzz")

""":# **using while loop finde odd values\**
**# quation**:  Write a program to print only odd numbers from the given list using while loop. L [23, 45, 32, 25, 46, 33, 71, 90)

"""

list = [23, 45, 32, 25, 46, 33, 71, 90]
index = 0

while index < len(list):
    print(list[index])
    index += 1

"""# **fibonacci** **searies**
quation : "Write a program to find all Fibonacci numbers between a given range".
"""

n=int(input("enter the number"))
n1=0
n2=1
count=2
if n < 0:
  print("enter only +ve values")
elif n==1:
  print(n1)
else:
  print(n1)
  print(n2)
  while count<n:
    n3=n1+n2
    print(n3)
    count+=1
    n1=n2
    n2=n3

""" quation : Write for loop statement to print the following series:

10, 20, 30........ 300

"""

for x in range (0,300,10):
  print(x,end=" ")

""" 2 . Write a program to print first 10 integers and their squares using while loop.

1 1
2 4
3 9 and so on

"""

num=0
while num < 10:
  print(num,num**2)
  num+=1

""" 3 . Write for loop statement to print the following series:

10, 20, 30........ 300
"""

for x in range(0,310,10):
  print(x,end=" ")

"""4. Write a while loop statement to print the following series :

105, 98, 91,......7.
"""

num = 105

while num >= 7:
    print(num)
    num -= 7

"""5. Write a program to print first 10 natural number in reverse order using while loop.

"""

num = 10

while num >= 1:
    print(num)
    num -= 1

"""6. Write a program to print sum of first 10 Natural numbers.

"""

sum = 0
n = 10

for i in range(1, n+1):
    sum += i

print("The sum of the first 10 natural numbers is:", sum)

"""7.Write a program to print sum of first 10 Even numbers.

"""

num=0
sum = 0
while num<=10:
  if num%2==0:
    sum = sum + num
  num+=1

print("the sum first 10 even numbers{}.".format(sum))

"""8. Write a program to print table of a number entered from the user.

"""

n=int(input())
for i in range(1,11):
   print(n, 'x', i, '=', n*i)

"""# **[palindrome]
 Write a program to check whether a number is palindrome or not.


"""

str='104'
str='204'
rev=reversed(str)
if list(str) == list(rev):
  print("it is a palindrome")
else:
  print("it is not palindrome")

"""Write a Program to print all the characters in the string 'PYTHON' using while loop.

"""

string="PYTHON"
length=len(string)
index=0
while index < length:
  print(string[index])
  index+=1

list=["venkatesh","prabhas"]
length=len(list)
index=0
while index < length:
  print(list[index])
  index+=1

set=(1,2,3,4,5,6)
length=len(set)
index=0
while index < length:
  print(set[index])
  index+=1

a=int(input())
print(a*a)

n = 23
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)

a=int(input())
fact=1
for i in range(1,a+1):
  print(i)
  fact=fact*i
print("",end="")
print(fact)

for i in range(10,20):
  if i ==15:
    pass
  print(i)

"""**quation **  write a program to check weather a number is prime or not using while loop"""

a=int(input())
sum=0
for i in range (1,a+1):
  print(i)
  sum=sum+i
  print(" ",end=" ")
  print(sum)

a=10
b=15
if a < b:
  print(" a is less than b")
else:
  print(" b is grater trhan a ")

a=int(input())
if a >=1:
  print("given value is positive")
elif a<0:
  print("value is negative")
else:
  print("value is zero")

0<=0

1<2

2>1

2>=2

2>=1

"""1. Write a Python program to find the maximum of two numbers using the greater than operator.
2. Write a program to check if a given number is even or odd using the modulo operator.
3. Write a program to check if a given year is a leap year or not using logical operators.
4. Write a program to check if a given character is a vowel or a consonant using if-elif-else statements.
5. Write a program to calculate the total cost of purchasing a quantity of a particular item, considering a discount based on the quantity purchased.
6. Write a program to determine if a triangle is equilateral, isosceles, or scalene based on the lengths of its sides.
7. Write a program to check if a given number is positive, negative, or zero using if-elif-else statements.
8. Write a program to determine the largest among three numbers using nested if-else statements.
9. Write a program to calculate the sum, difference, product, and quotient of two numbers based on user input.
10. Write a program to determine the grade of a student based on their percentage marks using if-elif-else statements.

These questions can be solved using conditional statements without the need for any loops.

"""

#1 Write a Python program to find the maximum of two numbers using the greater than operator.

a=int(input("enter the number"))
b=int(input("enter the number"))
if a > b:
  print("a is greater tha b")
else:
  print("b is less than a")

#2Write a program to check if a given number is even or odd using the modulo operator.
a=int(input())
if a >=1:
  print("given value is positive")
elif a<0:
  print("value is negative")
else:
  print("value is zero")

#3Write a program to check if a given year is a leap year or not using logical operators.
Year=int(input("enter the year"))
if((Year% 400 == 0) or
   (Year % 100 != 0) and
   (Year % 4 == 0)):
   print("it is leap year")
else:
  print("it is not leap year")

#4 Write a program to check if a given character is a vowel or a consonant using if-elif-else statement
a="a,e,i,o,u,A,I,E,O,U"
n=input()
if n in a:
  print("vowles")
else:
  print("consonant")

"""5.Write a program to calculate the total cost of purchasing a quantity of a particular item, considering a discount based on the quantity purchased.

"""

item=int(input("enter the number of items"))
if item < 10:
  print("total cost=",item * 120,'RS')
elif 10<=item<=99:
  print("totalcost=",item*100,'RS')
else:
  print("total cost=",item*70,'RS')

"""7 Write a program to check if a given number is positive, negative, or zero using if-elif-else statements."""

a=int(input())
if a >=1:
  print("given value is positive")
elif a<0:
  print("value is negative")
else:
  print("value is zero")

"""8.Write a program to determine the largest among three numbers using nested if-else statements."""

a=int(input())
b=int(input())
c=int(input())
if a > b and a > c:
  print("a is greater than b")
  if b >c and b>a:
    print(" b is less than a")

else:
  print("c is largest number")

"""9. Write a program to calculate the sum, difference, product, and quotient of two numbers based on user input."""

a=int(input())
b=int(input())
print("sum",a+b)
print("difference",a-b)
print("product",a*b)
print("quotient",a//b)



"""10 Write a program to determine the grade of a student based on their percentage marks using if-elif-else statements."""

n=int(input())
if n>90:
  print("grade is A")
elif n>80:
  print("grade is B")
elif n>70:
  print("grade is C")
elif n>60:
  print(" grade is E")
else:
  print(" paas")

66*1000

"""# **SLICING **"""

str="python"
print(str[0:])
print(str[:len(str)])
print(str[:])
print(str[1:3])

str1="venkatesh"   #given string
del(str1)                         #this is delete module

"""# **concatination of strings**

1.   method 1


"""

str1="venkatesh"
str2="prabhas"
str3=str1+" "+"salaar"+" "+str2     #concatination of string
print(str3)

"""2. method 2"""

str1="venkatesh"
str2="prabhas"
print(str1+" "+str2)  #concatination of string

"""# **Reapition of string**"""

str="venkatesh salaar prabhas"
print(str*4)

"""# **captalize of string**"""

name="salaar"
print(name.capitalize())

name="amarendra bahubali"
print(name.capitalize())

"""# **count of string**"""

name="amarendra bahubali"
print(name.count("a"))

str="TCS conducts generally 3 rounds to select fresher as Software Developer in their organization"
count=str.count("t")
print(count)