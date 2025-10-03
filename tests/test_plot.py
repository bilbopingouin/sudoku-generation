import os
import random
import sys

# Adding path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../libs')

# Library to test
import plot  # noqa: E402


# ======================
def test_graph_random(capsys):
    # A random "grid"
    dummy_grid = ['{}'.format(random.randint(0, 9)) for i in range(81)]

    # Run the function
    plot.graph(''.join(dummy_grid))

    # Get the output
    out, err = capsys.readouterr()

    # Rebuild the output
    exp_out = '=============\n'
    for n in range(len(dummy_grid)):
        if 0 == n % 27:
            exp_out += '-------------------------\n'
        if 0 == n % 3:
            exp_out += '| '

        c = dummy_grid[n]
        if '0' == c:
            exp_out += '_ '
        else:
            exp_out += '{} '.format(c)
        if 8 == n % 9:
            exp_out += '|\n'

    # Check the output
    assert out == exp_out
