# num = int(input("Enter number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)

# //two sum
# a = [2, 7, 11, 15]
# target = 9

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] == target:
#             print("Indexes:", i, j)


# //pow
# x = float(input("Enter x: "))
# n = int(input("Enter n: "))

# result = 1

# if n < 0:
#     x = 1 / x
#     n = -n

# for i in range(n):
#     result = result * x

# print("Answer:", result)  


# //linear search

# n=int("enter the size")
# a=[]
# for i in range(n):
#     x=int(input("enter the element"))
#     a.append(x)
# key=int(input("enter the element to search"))
# found=False
# for i in range(n):
#     if a[i]==key:
#         print("Element found at index:",i)
#         found=True
#         break    
#     if found==False:
#         print("Element not found")


# //binary serach
# a.sort()
# low = 0
# high = len(a) - 1
# while low <= high:
#     mid = (low + high) // 2
#     if a[mid] == key:
#         print("Element found at index:", mid)
#         break
#     elif key>a[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1

# //array input

# n=int(input("Enter the size of the array: "))
# a=[0]*n
# for i in range(n):
#     a[i]=int(input("Enter element: "))
# print("Array elements are:", a)

# //palindrome check

# num = int(input("Enter number: "))
# original = num
# reverse = 0
# while num>0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")


# //fibonacci series

# n = int(input("Enter the number of terms: "))
# a=0
# b=1
# for i in range(n):
#     print(a, end=' ')
#     c = a + b
#     a = b
#     b = c


# //factorial

# num = int(input("Enter number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is", factorial)


# //prime number check
# num = int(input("Enter number: "))
# count=0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
#     if count == 2:
#         print(num, "is a prime number.")
#     else:
#         print(num, "is not a prime number.")


# //sum of digits
# num = int(input("Enter number: "))
# total=0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num // 10
# print("Sum of digits:", total)

# //reverse number

# num=int(input("Enter number: "))
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print( reverse)

# //leap year check
# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")

        