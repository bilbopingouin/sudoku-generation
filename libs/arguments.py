import argparse

# ============================
def parse():
    parser = argparse.ArgumentParser(
            description='Sudoku generator')

    parser.add_argument('-i',
                        '--input',
                        help='Input Sudoku String',
                        default='350627000069803207000504010730900561800000400600001300020309045000075800573200006',
                        type=str,
                        required=False)

    options = parser.parse_args()

    params = {}

    params['input'] = options.input

    return params

