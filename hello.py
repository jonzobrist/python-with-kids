#!python
# This is my first python program, it says hello world!

# List of people
peoples = ['Claire', 'Alex', 'Blake', 'Jon','Lemon']
# Dictionary of their favorite items
favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'Osama Bin Laden'}

for number in xrange(len(peoples)):
    print "{}'s favorite item is {}'".format(peoples[number],
                                      favorite_items[peoples[number]])
