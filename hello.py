#!python
# This is my first python program, it says hello world!

# List of people
# no longer needed!
# peoples = ['Claire', 'Alex', 'Blake', 'Jon','Lemon']
# Dictionary of their favorite items
favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'His spot on the couch'}
my_string = "{} really loves {}!"

for person in favorite_items:
    print(my_string.format(person, favorite_items[person]))
