# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    bill += 15
if size == "M":
    bill += 20 

if size == "L":        
    bill+= 25

if add_pepperoni == "Y" and size == "S": 
   bill+= 2
if add_pepperoni == "Y" and size == "M" or size == "L":
   bill+= 3
if extra_cheese == "Y": 
  bill += 1

print("your final bill is",bill)
