# list
a=[1,2,3,4,5,6,7,8,9,10]
print(a[3:10])

# leap year 
year=int(input("Enter num to check leap year or not:"))
if(year%4==0 and year%100!=0):
    print("This is a leap year")
else:
    print("Not a leap year")

# Even or odd 
n=int(input("Enter a num"))
l=["even","odd"]
print(l[n%2])
 
# sum of integers
nums = [1, 2, 3, 4, 5, 8, 9, 10]
total = sum(nums)
print("Sum of integers:", total)

# swap num
num1=3
num2=9
temp=num1
num1=num2
num2=temp
print("Swap of two number is",num1,num2)

# rotate
l=[1,2,3,4,5,6]  
print( l [3:6] + l[0:3])

# * pattern
for i in range(1):
    pattern=""
    for j in range(4):
        pattern+="*" 
        print(pattern)

# square pattern
for i in range(0,4): 
    for j in range(0,4):
      print("*", end=" ") 
    print()  

#  pyradmid
    def print_pyramid(n):
     for i in range(n): 
        for j in range(n - i - 1):
            print(" ", end="") 
        for k in range(2 * i + 1):
            print("*", end="") 
        print() 
print_pyramid(5)

# inverted right triangle 
for i in range(4, 0, -1):
    print(" " * (4 - i) + "*" * i)

#  hollow square 
def hollow_square(n):
    for i in range(n):
        for j in range(n): 
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")   
        print()  
hollow_square(5)

# unique numbers
def unique(nums):
    unique = 0
    for num in nums:
        unique ^= num   
    return unique
nums = [1, 1, 2, 3, 5, 5, 4, 2, 3, 7, 7]   
print("The unique number is:", unique(nums))


 