#!/usr/bin/env python3
import ipdb;
from author import Author

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine
a1 = Author("Alice")
print(a1._name)
if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
