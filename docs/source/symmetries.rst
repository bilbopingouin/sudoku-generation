Sudoku symmetries
=================

As a mathematical object, a sudoku has many symmetries. Using those, it is possible to generate new sudokus from another one. They are fundamentally the same sudoku, but appears different.

The `publication <https://pi.math.cornell.edu/~mec/Summer2009/Mahmood/Symmetry.html>`_ explains the symmetries in detail.

Grid format
-----------

Note that those functions all work with a sudoku grid in a string format. More details can be found on another :ref:`section <data-format>`.


Numbers
-------

In a sudoku, the numbers are simply symbols and do not play any effective role. One can clearly see that replacing '1's and '2's would lead to an equally solvable sudoku. We have then a function to swap the numbers randomly.

.. autofunction:: libs.mixing.change_numbers(string)

The resulting grid appears exactly the same as the input, except that the symbols have been interchanged.

.. note::
   This symmetry provide a large variation of "new" sudokus: `9! = 362880`

Rotation
--------

If you take a sudoku printed on a piece of paper. You could as easily solve it if you rotate the piece of paper by quarter-turn(provided you can recognise the digits).

This is another symmetry: rotation. The function

.. autofunction:: libs.mixing.rotate(string)

applies a random rotation from 0°, 90°, 180° and 270°.

.. note::
   This provide 4 different combinations.

Stacks rows and columns
-----------------------

Sudokus are solved by having a unique digit from 1 to 9 in each row, each column and each "box". Those "boxes" are called stacks. Representing a sudoku where each stack is represented as a letter, we can have

.. code-block::

   A B C
   D E F
   G H I

We can swap two rows of stacks and come to

.. code-block::

   B A C
   E D F
   H G I

Clearly, the distribution of the digits within the stacks are kept unchanged. The columns as well. The rows have been changed, but only the ordering. For example we could get from

.. code-block::

   3 5 2 1 9 7 8 4 6

to

.. code-block::

   1 9 7 3 5 2 8 4 6

The ordering of the distribution was modified, but the content actually stayed the same. And thus the new sudoku is equally valid.

This is the symmetry by stack columns swapping. This is implemented in the function; 

.. autofunction:: libs.mixing.flip_cols(string)

Similarly, there is a symmetry by stack rows swapping, also in 

.. autofunction:: libs.mixing.flip_rows(string)

.. note::

   Each of those symmetries provide `3! = 6` variations.
