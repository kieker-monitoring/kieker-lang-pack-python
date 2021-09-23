# -*- coding: utf-8 -*-

import examples.aspectl.bookstore as bs
import sys
def main():

    bookstore = bs.Bookstore()

    try:
        num_traces = sys.argv[1]
        if not isinstance(num_traces, int):
            raise TypeError
    except IndexError:
        num_traces = 1
    bookstore.search_book()
    print("Finished!")


if __name__ == '__main__':
    main()