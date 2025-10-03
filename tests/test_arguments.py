import os
import pytest
import random
import re
import sys

# Adding path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../libs')

# Library to test
import arguments  # noqa: E402


# ======================
def test_parse_defaults(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['sudoku'])
    output = arguments.parse()

    # Get the output
    out, err = capsys.readouterr()

    assert 2 == len(output)

    assert 'debug' in output
    assert output['debug'] is False

    assert 'input' in output
    def_grid = '35062700006980320700050401073090056'
    def_grid += '1800000400600001300020309045000075'
    def_grid += '800573200006'
    assert def_grid == output['input']

    assert '' == err
    assert '' == out


# ======================
def test_parse_debug_2(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['sudoku', '--debug'])
    output = arguments.parse()

    # Get the output
    out, err = capsys.readouterr()

    assert 2 == len(output)

    assert 'debug' in output
    assert output['debug'] is True

    assert 'input' in output
    def_grid = '35062700006980320700050401073090056'
    def_grid += '1800000400600001300020309045000075'
    def_grid += '800573200006'
    assert def_grid == output['input']

    assert '' == err

    expected_out = 'debug: True\ninput: {}\n'.format(def_grid)
    assert expected_out == out


# ======================
def test_parse_help(monkeypatch, capsys):
    '''
    We trust that argparse does its job correctly, so we just
    check that we get some result
    '''
    monkeypatch.setattr(sys, 'argv', ['sudoku', '--help'])

    with pytest.raises(SystemExit):
        arguments.parse()

    # Get the output
    out, err = capsys.readouterr()
    assert '' == err

    assert re.match('usage: *', out) is not None


# ======================
def test_parse_input(monkeypatch, capsys):
    rnd_input = ''.join(['{}'.format(random.randint(0, 9)) for n in range(81)])
    monkeypatch.setattr(sys, 'argv', ['sudoku', '--input', rnd_input])

    output = arguments.parse()

    out, err = capsys.readouterr()

    assert '' == err
    assert '' == out

    assert 2 == len(output)

    assert 'debug' in output
    assert output['debug'] is False

    assert 'input' in output
    assert rnd_input == output['input']
