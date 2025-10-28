# sudoku-generation

A sudoku generator script in python.

## Aims

### Main goal

Using the mathematical symmetries of sudokus, we can generate a large number of sudokus from a single board. This script implements those symmetries.

### Secondary

The second aim is to use that relatively simple code and adding many elements of process: requirements, documentation, automatic testing, CI, ... 

The status of the implementation can be found [here](docs/manual/process.md).

## Status

| Name | Result | Description |
| ---- | ------ | ----------- |
| Flake8 | [![Flake8](https://github.com/bilbopingouin/sudoku-generation/actions/workflows/flake8.yml/badge.svg?branch=main)](https://github.com/bilbopingouin/sudoku-generation/actions/workflows/flake8.yml) | Static analysis of the code |
| PyTest | [![PyTest](https://github.com/bilbopingouin/sudoku-generation/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/bilbopingouin/sudoku-generation/actions/workflows/pytest.yml) | Unit testing |
