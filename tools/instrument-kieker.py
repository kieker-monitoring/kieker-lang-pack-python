# -*- coding: utf-8 -*-

import importlib.util
import os
import sys


def get_filename_from_path(filepath):
    return os.path.basename(filepath)[:-3]


def check_arguments():
    if len(sys.args) < 3:
        print('Not enogh arguments')
        sys.exit()
    for i in range(1, 3):
        if not isinstance(sys.args[i], str):
            print('Awaited string argument, but got another type')
            sys.exit()


def main():

    check_arguments()

    # Read arguments
    program_to_instrument = sys.args[1]
    instrumentation_advices = sys.args[2]

    # Read advice file and instrumentize modules
    filename = os.path.basename(instrumentation_advices)
    spec = importlib.util.spec_from_file_location(filename,
                                                  instrumentation_advices)
    instrumentation_advice_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(instrumentation_advice_module)

    # Execute instrumnetized program
    file = open(program_to_instrument, "r")
    src = file.read()
    exec(src)


if __name__ == '__main__':
    main()
