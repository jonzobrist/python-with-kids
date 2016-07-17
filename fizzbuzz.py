#!python

# Fizz Buzz:
# Iterate over numbers printing Fizz if the numbers
# is divisble by 3 you say Fizz
# if it's divisible by 5 you say Buzz
# both? FizzBuzz
# neither? Just say the number, punk!

for number in xrange(1,16):
    if (number % 3 == 0) & (number % 5 == 0):
        print "FizzBuzz"
    elif number % 3 == 0:
        print "Fizz"
    elif number % 5 == 0:
        print "Buzz"
    else:
        print number
