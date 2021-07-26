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

    check_arguments()
    # Read arguments
    program_to_instrument = os.path.abspath(sys.argv[1])
    instrumentation_advices = os.path.abspath(sys.argv[2])

    # Read advice file and instrumentize modules
    
    # Delete extension
    filename = os.path.basename(instrumentation_advices)[:-3]

    spec = importlib.util.spec_from_file_location(filename,
                                                  instrumentation_advices)
    
    instrumentation_advice_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(instrumentation_advice_module)
    
    #Rewrite argumetns, such that another entrypoint is not hindered
    sys.argv=sys.argv[3:]
    instrumentation_advice_module.run_main()
    
   
if __name__ == '__main__':
    main()
