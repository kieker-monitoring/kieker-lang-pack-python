# -*- coding: utf-8 -*-

import examples.aspectl.instrument as inst
import aspectlib
import examples.aspectl.bookstore 

aspectlib.weave(examples.aspectl.bookstore.Bookstore, inst.wrapper)
print(2)