# API

<a id="data-format"></a>

## Data format

Most of the functions work with a sudoku grid in form of a string containing rows after rows.

The Sudoku

```default
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
```

is represented as a string

```default
'111111111222222222333333333444444444555555555666666666777777777888888888999999999'
```

## Modules

| [`libs.mixing`](generated/libs.mixing.md#module-libs.mixing)          | Provide functions to shuffle the sudoku using mathematical symmetries   |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`libs.arguments`](generated/libs.arguments.md#module-libs.arguments) | This library handles the command-line user interface.                   |
| [`libs.plot`](generated/libs.plot.md#module-libs.plot)                | Provide a single function to print the sudoku in the shell              |
