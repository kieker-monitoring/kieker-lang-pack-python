# -*- coding: utf-8 -*-
import time
import sys
import threading
from tools.Aspect import Instrumental, instrument

def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        result=func(*args, **kwargs)
        print (result)
        print("world")
        return result
    return wrapper
class Catalog:
   # __metaclass__=Instrumental
    def __init__(self):
        pass
    #@instrument
    def get_book(self,complex_query):
        try:
            if complex_query:
                time.sleep(10)
            else:
                time.sleep(1)
        except InterruptedError:
            pass


class CRM:
   #__metaclass__=Instrumental
    def __init__(self, catalog):
        self.catalog = catalog
    
    
    def get_offers(self):
        self.catalog.get_book(False)


class Bookstore:
   
   
    def __init__(self):
        self.catalog = Catalog()
        self.crm = CRM(self.catalog)
   
    def search_book(self):
        self.catalog.get_book(False)
        self.crm.get_offers()


def run_bookstore(bookstore):
    bookstore.search_book()


def main():
  
    bookstore = Bookstore()
   
    try:
        num_traces = sys.argv[1]
        if not isinstance(num_traces, int):
            raise TypeError
    except IndexError:
        num_traces = 1
        
    bookstore.search_book()
    print("Starting trace number %s")
       # threading.Thread(target=run_bookstore, args=(bookstore,)).start


if __name__ == '__main__':
    main()
