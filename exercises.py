# Exercise 11
# Let's do our own Bitmaker version of FizzBuzz, which is the name of a classic job interview coding problem.
#
# Write a program that loops over the numbers from 1 to 100. If the number is a multiple of three, output the string "Bit". For multiples of five, output
# "Maker". For numbers which are multiples of both three and five, output "BitMaker". Otherwise output the number itself.

for num in range(1,101):
    if (num % 3 == 0) and (num % 5 == 0):
        print('BitMaker')
    elif (num % 3 == 0):
        print('Bit')
    elif (num % 5 == 0):
        print('Maker')
    else:
        print(num)

#Exercise 12
# PizzaMaker wants to handle bulk orders of pizzas, with varying amounts of toppings on each. Ask the user for a number of pizzas - call it quantity.
# We then want to ask the user for quantity more numbers - the number of toppings on that pizza - and print them out

print('How many pizzas do you want to order?')
quantity = int(input())

def how_many_toppings(pizza_num):
    print('How many toppings on pizza {}?'.format(pizza_num))
    num_toppings = int(input())
    print('You have ordered a pizza with {} toppings.'.format(num_toppings))

for num in range(1,quantity+1):
    how_many_toppings(num)
