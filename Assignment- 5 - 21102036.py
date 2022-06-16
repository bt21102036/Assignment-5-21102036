#Q1 Reverse a string
a=input("Enter the string:")
for i in range ((len(a)-1),-1,-1):
    print(a[i],end="")
print("\n")

#Q2 Range divisible by a number
n=int(input("Enter the number:"))
Lower_limit=int(input("Enter the lower limit:"))
Upper_limit=int(input("enter the upper limit:"))
for i in range (Lower_limit,Upper_limit+1):
    if (i%n==0):
        print(i)
print("\n")

#Q3 Heron's formula
def triangle(a,b,c):
    if(a+b>c and a+c>b and b+c>a):
        s=(a+b+c)/2
        Area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle using heron's formula:",Area)
    else:
        print("Triangle is invalid")

a=float(input("Enter the side a :"))
b=float(input("Enter the side b :"))
c=float(input("Enter the side c :"))
triangle(a,b,c)
print("\n")

#Q4 Nested For Loop

for i in range(0,6):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("\n")

#Q5 Triangular pattern of alphabets
def contalpha(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch,end="")
            num=num+1
        print("")

n=int(input("Enter the number of rows:"))

contalpha(n)
print("\n")

#Q6 Prime numbers
Lower_Range = int(input("Enter the lower limit:"))
Upper_Range = int(input("Enter the Upper limit:"))
print("The prime number between", Lower_Range, "and", Upper_Range, "are:")
for num in range(Lower_Range, Upper_Range + 1):
    k=0
    for i in range(2, num//2+1):
            if (num % i) == 0:
                k=k+1
    if(k<=0):
            print(num)
print("\n")

#Q7 Divisible by 7 & 11
print("Numbers multiple of 7 and divisible by 11 in the range 1-500 are:")
for num in range(1,500):
    if (num%7==0) and (num%11==0):
        print(num)
print("\n")


#Q8 List
list=[]
for i in range(0,10,1):
    n=int(input(f"Enter {i+1} number: "))
    list.append(n)
print(list)

#a)
print("Positive numbers are: ")
for i in range(10):
    if list[i]>0:
        print(list[i])

#b)
print("Negative numbers are: ")
for i in range(10):
    if list[i]<0:
        print(list[i])

#c)
print("Odd numbers are: ")
for i in range(10):
    if list[i]%2!=0:
        print(list[i])

#d)
print("Even numbers are: ")
for i in range(10):
    if list[i]%2==0:
        print(list[i])

#e)
count=dict()
for no in list:
    if no in count:
        count[no]+=1
    else:
        count[no]=1

print("No of times each number occurs in the List:")
print(count)
print()


#Question 9
#Count the number of occurrence of each word in the list input by the user

str=input("Enter a string: ")
#Empty dictionary is created to
counts = dict()
#We split the input string into words and store it in in a list
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)


