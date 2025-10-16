API
===

.. _data-format:

Data format
-----------

Most of the functions work with a sudoku grid in form of a string containing rows after rows.

The Sudoku

.. code-block::

   -------------------------
   | 1 1 1 | 1 1 1 | 1 1 1 |
   | 2 2 2 | 2 2 2 | 2 2 2 |
   | 3 3 3 | 3 3 3 | 3 3 3 |
   -------------------------
   | 4 4 4 | 4 4 4 | 4 4 4 |
   | 5 5 5 | 5 5 5 | 5 5 5 |
   | 6 6 6 | 6 6 6 | 6 6 6 |
   -------------------------
   | 7 7 7 | 7 7 7 | 7 7 7 |
   | 8 8 8 | 8 8 8 | 8 8 8 |
   | 9 9 9 | 9 9 9 | 9 9 9 |
   -------------------------

is represented as a string

.. code-block::

   '111111111222222222333333333444444444555555555666666666777777777888888888999999999'

Modules
-------
.. autosummary:: 
   :toctree: generated

   libs.mixing
   libs.arguments
   libs.plot

