#!python

# Fizz Buzz:
# Iterate over numbers printing Fizz if the numbers
# is divisble by 3 you say Fizz
# if it's divisible by 5 you say Buzz
# both? FizzBuzz
# neither? Just say the number, punk!

for number in xrange(1,16):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if len(result) == 0:
        result = number
    print result
