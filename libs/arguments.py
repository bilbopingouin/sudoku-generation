"""
This library handles the command-line user interface.

The following options are available

.. code-block::

    usage: sudoku.py [-h] [-i INPUT] [-d]

    Sudoku generator

    options:
        -h, --help            show this help message and exit
        -i INPUT, --input INPUT
                              Input Sudoku String
        -d, --debug           Activate some output debug
"""
import argparse


# ============================
def parse():
    """
    Parse the input parameters based on `argparse`

    :return: List of parameters
    :rtype: dict
    """
    parser = argparse.ArgumentParser(
            description='Sudoku generator')

    parser.add_argument('-i',
                        '--input',
                        help='Input Sudoku String',
                        default='350627000'
                        '069803207'
                        '000504010'
                        '730900561'
                        '800000400'
                        '600001300'
                        '020309045'
                        '000075800'
                        '573200006',
                        type=str,
                        required=False)

    parser.add_argument('-d',
                        '--debug',
                        help='Activate some output debug',
                        required=False,
                        action='store_true')

    options = parser.parse_args()

    params = {}

    params['debug'] = options.debug

    params['input'] = options.input

    if params['debug']:
        for p in params:
            print('{}: {}'.format(p, params[p]))

    return params
