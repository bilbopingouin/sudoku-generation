# Sudoku symmetries

As a mathematical object, a sudoku has many symmetries. Using those, it is possible to generate new sudokus from another one. They are fundamentally the same sudoku, but appears different.

The [publication](https://pi.math.cornell.edu/~mec/Summer2009/Mahmood/Symmetry.html) explains the symmetries in detail.

## Grid format

Note that those functions all work with a sudoku grid in a string format. More details can be found on another [section](api.md#data-format).

## Numbers

In a sudoku, the numbers are simply symbols and do not play any effective role. One can clearly see that replacing ‘1’s and ‘2’s would lead to an equally solvable sudoku. We have then a function to swap the numbers randomly.

### libs.mixing.change_numbers(string)

Shuffle the numbers

* **Parameters:**
  **string** (*str*) – input sudoku grid
* **Returns:**
  output sudoku grid
* **Return type:**
  str

The resulting grid appears exactly the same as the input, except that the symbols have been interchanged.

#### NOTE
This symmetry provide a large variation of “new” sudokus: 9! = 362880

## Rotation

If you take a sudoku printed on a piece of paper. You could as easily solve it if you rotate the piece of paper by quarter-turn(provided you can recognise the digits).

This is another symmetry: rotation. The function

### libs.mixing.rotate(string)

Rotate the sudoku by a random number of quarter turns

* **Parameters:**
  **string** (*str*) – Input sudoku grid
* **Returns:**
  Output sudoku grid
* **Return type:**
  str

applies a random rotation from 0°, 90°, 180° and 270°.

#### NOTE
This provide 4 different combinations.

## Stacks rows and columns

Sudokus are solved by having a unique digit from 1 to 9 in each row, each column and each “box”. Those “boxes” are called stacks. Representing a sudoku where each stack is represented as a letter, we can have

```default
A B C
D E F
G H I
```

We can swap two rows of stacks and come to

```default
B A C
E D F
H G I
```

Clearly, the distribution of the digits within the stacks are kept unchanged. The columns as well. The rows have been changed, but only the ordering. For example we could get from

```default
3 5 2 1 9 7 8 4 6
```

to

```default
1 9 7 3 5 2 8 4 6
```

The ordering of the distribution was modified, but the content actually stayed the same. And thus the new sudoku is equally valid.

This is the symmetry by stack columns swapping. This is implemented in the function;

### libs.mixing.flip_cols(string)

Random flip the stack columns

* **Parameters:**
  **string** (*str*) – Input sudoku grid
* **Returns:**
  Output sudoku grid
* **Return type:**
  str

Similarly, there is a symmetry by stack rows swapping, also in

### libs.mixing.flip_rows(string)

Random flip the stack rows

* **Parameters:**
  **string** (*str*) – Input sudoku grid
* **Returns:**
  Output sudoku grid
* **Return type:**
  str

#### NOTE
Each of those symmetries provide 3! = 6 variations.
