# -*- coding: utf-8 -*-

import importlib.util
import os
import sys
import examples.automatic.Bookstore

def get_filename_from_path(filepath):
    return os.path.basename(filepath)[:-3]


def check_arguments():
    if len(sys.argv) < 3:
        print('Not enogh arguments')
        sys.exit()
    for i in range(1, 3):
        if not isinstance(sys.argv[i], str):
            print('Awaited string argument, but got another type')
            sys.exit()


def main():

    #check_arguments()
   # print(os.getcwd())
    # Read arguments
    program_to_instrument = ('C:/Users/Serafim Simonov/Desktop/'
                            +'job-2/kieker-lang-pack-python/examples/automatic/Bookstore.py')
    instrumentation_advices = ('C:/Users/Serafim Simonov/Desktop/'
                            +'job-2/kieker-lang-pack-python/examples/automatic/aop_config.py')
    print("advices "+instrumentation_advices)
    # Read advice file and instrumentize modules
    filename = os.path.basename(instrumentation_advices)[:-3]
    print("Filename - "+filename)
    print(instrumentation_advices)
    spec = importlib.util.spec_from_file_location(filename,
                                                  instrumentation_advices)
    print(spec)
    instrumentation_advice_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(instrumentation_advice_module)

    # Execute instrumnetized program
   # file = open(program_to_instrument, "r")
   # src = file.read()
    #exec(src, globals(), globals())
    examples.automatic.Bookstore.main()
    os.system("python"+program_to_instrument )  
if __name__ == '__main__':
    main()
