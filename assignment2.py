
#  Question 1

for i in range(30):
    while i%2!=0:
        i+=1
        print(i)

print("*"*50)

#  Question 2
for i in range(30):
    while i % 2 == 0:
        i += 1
        print(i)

print("*"*50)

#  Question 3
total_amount = int(input("How much money do you have?"))
marketing = total_amount * 0.25
op_ex = total_amount * 0.5
cust_acq = total_amount - (marketing + op_ex)
cust_cost = 5
num_cust = int(cust_acq/cust_cost)

print(f"The total number of customers you can acquire with this amount is: {num_cust}")
