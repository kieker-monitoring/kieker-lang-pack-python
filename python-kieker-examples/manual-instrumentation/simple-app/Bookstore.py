# -*- coding: utf-8 -*-
import time
import sys
import threading


class Catalog:

    def get_book(complex_query):
        try:
            if complex_query:
                time.sleep(10)
            else:
                time.sleep(1)
        except InterruptedError:
            pass


class CRM:

    def __init__(self, catalog):
        self.catalog = catalog

    def get__offers(self):
        self.catalog.get_book(False)


class Bookstore:

    def __init__(self):
        self.catalog = Catalog(self)
        self.crm = CRM(self.catalog)

    def search_book(self):
        self.catalog.get_book(False)
        self.crm.get_offers()


def run_bookstore(bookstore):
    bookstore.search_book


def main():
    bookstore = Bookstore()

    try:
        num_traces = sys.argv[1]
        if not isinstance(num_traces, int):
            raise TypeError
    except IndexError:
        num_traces = 1

    for i in range(num_traces):
        print("Starting trace number %s", i+1)
        threading.start(run_bookstore, args=(bookstore,))


if __name__ == 'main':
    main()
