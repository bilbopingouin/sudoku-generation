### Table of Contents

 * [1.0 SR001](#10-sr001-sr001)
    * [1.1 SR002](#11-sr002-sr002)
    * [1.2 SR003](#12-sr003-sr003)
    * [1.3 SR004](#13-sr004-sr004)
    * [1.4 SR005](#14-sr005-sr005)
    * [1.5 SR006](#15-sr006-sr006)

# 1.0 SR001 {#SR001}

Generate random sudoku
The program shall be able to generate random sudokus.

This means that running the same program several times after another should generate a different sudoku grid each time.

*Child links:* [DR001](DR.md#10-dr001-dr001)

## 1.1 SR002 {#SR002}

Provide a grid
The program shall provide a generated sudoku to the user.
In some form, the user shall be able to visualise the generated sudoku.

*Child links:* [DR005](DR.md#14-dr005-dr005)

## 1.2 SR003 {#SR003}

Symmetries
The program shall use the sudoku mathematical symmetries to generate a sudoku grid.

*Child links:* [DR006](DR.md#15-dr006-dr006)

## 1.3 SR004 {#SR004}

Start grid
The program shall allow the user to enter a given start sudoku.

*Child links:* [DR002](DR.md#11-dr002-dr002)

## 1.4 SR005 {#SR005}

Default grid
If the user does not specify a start grid, the program shall provide a default option.

*Child links:* [DR002](DR.md#11-dr002-dr002)

## 1.5 SR006 {#SR006}

Quality
The project shall ensure the quality of the code by various methods

*Child links:* [CG001](CG.md#10-cg001-cg001), [CG002](CG.md#11-cg002-cg002), [CG003](CG.md#12-cg003-cg003)

