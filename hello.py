#!python
# This is my first python program, it says hello world!

# List of people
# no longer needed!
peoples = ['Claire', 'Alex', 'Blake', 'Dad','Mom']
# Dictionary of their favorite items
favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'His spot on the couch',
                  'Mom':'Napping'}

my_string = "{} really loves {}!"

for person in sorted(peoples):
    if person in favorite_items.keys():
        print(my_string.format(person, favorite_items[person]))
    else:
        print "Error, {} has no favorites".format(person)
