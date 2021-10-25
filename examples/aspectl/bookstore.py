# -*- coding: utf-8 -*-

import time






class Catalog:

    def __init__(self):
        pass

    def get_book(self, complex_query):
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
    while True:
        bookstore.search_book()
def hello():
    return 'World'

