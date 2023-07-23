#variables & funtions
#variables are store data.
# functions are like print(),len(),sum(),int()
## 2
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#Python Program to Generate a Random Number
import random
n=random.random()
print(n)
#https://www.simplilearn.com/tutorials/python-tutorial/append-in-python append
import random  
rand_list = []  
for i in range(0,10):  
    n = random.randint(1,50)  
    rand_list.append(n)  
print(rand_list)  

#EXAMPLE
import random
n=random.randint(1,50)
print(n)


# ex
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
    
print("The sum is",sum)


#ifelse - decision making
a=int(input('enter:'))
if a<=50:
    print('c')
else:
    print('d')
