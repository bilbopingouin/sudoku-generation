### Table of Contents

 * [1.0 DR001](#10-dr001-dr001)
    * [1.1 DR002](#11-dr002-dr002)
    * [1.2 DR003](#12-dr003-dr003)
    * [1.3 DR004](#13-dr004-dr004)
    * [1.4 DR005](#14-dr005-dr005)
    * [1.5 DR006](#15-dr006-dr006)
    * [1.6 DR007](#16-dr007-dr007)
    * [1.7 DR008](#17-dr008-dr008)
    * [1.8 DR009](#18-dr009-dr009)
    * [1.9 DR010](#19-dr010-dr010)

# 1.0 DR001 {#DR001}

The output shall be the result of one or more random function(s).

*Parent links:* [SR001](SR.md#10-sr001-sr001)

## 1.1 DR002 {#DR002}

User Interface
The program shall contain a user interface

*Parent links:* [SR004](SR.md#13-sr004-sr004), [SR005](SR.md#14-sr005-sr005)

## 1.2 DR003 {#DR003}

UI default grid
The user interface shall provide a default start grid if the user did not set one

*Parent links:* [DR002](DR.md#11-dr002-dr002)

## 1.3 DR004 {#DR004}

UI set grid
The user interface should implement a method for the user to set a start sudoku grid.

*Parent links:* [DR002](DR.md#11-dr002-dr002)

## 1.4 DR005 {#DR005}

Print out
The programm shall provide at least one method for a graphical visualisation of the final sudoku

*Parent links:* [SR002](SR.md#11-sr002-sr002)

## 1.5 DR006 {#DR006}

Symmetries
The program shall contain a software module implementing one or more transformation on the start grid, using the sudoku symmetries.

*Parent links:* [SR003](SR.md#12-sr003-sr003)

## 1.6 DR007 {#DR007}

Symmetries
The transformation module shall include a function which can exchange the digits. E.g. from 123456789 to 352689147.

*Parent links:* [DR006](DR.md#15-dr006-dr006)

## 1.7 DR008 {#DR008}

Symmetries
The transformation module shall include a function to rotate a sudoku grid with 90°, 180° or 270°.

*Parent links:* [DR006](DR.md#15-dr006-dr006)

## 1.8 DR009 {#DR009}

Symmetries
The transformation module shall include a function to exchange the stacks rows.

*Parent links:* [DR006](DR.md#15-dr006-dr006)

## 1.9 DR010 {#DR010}

Symmetries
The transformation module shall include a function to exchange the stacks columns.

*Parent links:* [DR006](DR.md#15-dr006-dr006)

