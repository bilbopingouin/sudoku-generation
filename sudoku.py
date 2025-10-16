import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/libs')

import arguments  # noqa: E402
import mixing     # noqa: E402
import plot       # noqa: E402


# ============================
# Main function
# ============================
def main():
    """
    Main function of the program.

    :param None
    :return None

    """
    args = arguments.parse()

    # Get the original sudoku
    mysudoku = args['input']
    if args['debug']:
        plot.graph(mysudoku)
        print('Original')
        print(args)

    # Permutate the numbers
    mysudoku = mixing.change_numbers(mysudoku)
    if args['debug']:
        plot.graph(mysudoku)
        print('Numbers permutated')

    # Permutate stack rows
    mysudoku = mixing.flip_rows(mysudoku)
    if args['debug']:
        plot.graph(mysudoku)
        print('Stack rows permutated')

    # Permutate stack columns
    mysudoku = mixing.flip_cols(mysudoku)
    if args['debug']:
        plot.graph(mysudoku)
        print('Stack columns permutated')

    # Rotate sudoku
    mysudoku = mixing.rotate(mysudoku)
    if args['debug']:
        plot.graph(mysudoku)
        print('Rotated')

    # Print the final version
    plot.graph(mysudoku)


# ============================
if '__main__' == __name__:
    main()
