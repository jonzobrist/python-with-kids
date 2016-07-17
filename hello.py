#!python
""" This is my first python program, it says hello world! """
from collections import defaultdict

# List of people
# no longer needed!
my_peoples = ['Claire', 'Alex', 'Blake', 'Dad','Mom', 'Mom', 'Mom', 'Mom']
alex_peoples = ['Alex', 'Blake', 'Dad','Mom', 'Barthomule', 'Ashur']
# Dictionary of their favorite items

for person in my_peoples:
    if person in alex_peoples:
        print("Yes")
    else:
        print("Missing {}".format(person))


peoples = set(my_peoples + alex_peoples)


favorite_items = {'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'His spot on the couch',
                  'Mom':'Napping'}
def fetch_missing_data():
    return "No likes found"
default_favorites = defaultdict(fetch_missing_data, favorite_items)
my_string = "{} really loves {}!"
favorites = []

def main():
    tally_the_data()

def tally_the_data():
    for person in sorted(peoples):
        try:
            favorites.append(my_string.format(person, favorite_items[person]))
        except KeyError:
            favorite_items[person] = fetch_missing_data(person)
        print(my_string.format(person, favorite_items[person]))


if __name__ == '__main__':
    main()
