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
