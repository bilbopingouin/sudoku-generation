import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/libs')

import arguments
import mixing
import plot

# ============================
# Main function
# ============================
def main():
    args = arguments.parse()
    #print('Original')
    #print(args)
    #plot.graph(args['input'])
    mysudoku = args['input']
    mysudoku = mixing.change_numbers(mysudoku)
    #plot.graph(mysudoku)
    mysudoku = mixing.flip_rows(mysudoku)
    #plot.graph(mysudoku)
    mysudoku = mixing.flip_cols(mysudoku)
    #plot.graph(mysudoku)
    mysudoku = mixing.rotate(mysudoku)
    plot.graph(mysudoku)


# ============================
if '__main__' == __name__:
    main()
