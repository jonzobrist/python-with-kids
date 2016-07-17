#!python
""" This is my first python program, it says hello world! """
from collections import defaultdict
from collections import OrderedDict


# List of people
# no longer needed!
my_peoples = ['Claire', 'Alex', 'Blake', 'Dad','Mom', 'Mom', 'Mom', 'Mom']
alex_peoples = ['Alex', 'Blake', 'Dad','Mom', 'Barthomule', 'Ashur']
# Dictionary of their favorite items

peoples = set(my_peoples + alex_peoples)
only_in_alex = set(alex_peoples) - set(my_peoples)
all_our_people = set(alex_peoples) | set(my_peoples)

favorite_items = OrderedDict({'Claire':'Pokemon','Alex':'Magic Cards',
                  'Blake':'His spot on the couch',
                  'Mom':'Napping'})
def fetch_missing_data(person='Alex'):
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
