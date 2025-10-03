import os
import random
import sys

# Adding path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../libs')

# Library to test
import mixing  # noqa: E402


"""
Testing the numbers change
- No change
- Change the '1' into any digit ('0'-'9')
- A string '0123456789' to a random change
"""


# ======================
def test_change_numbers_0_nochange():
    # Not chaing numbers using a random grid
    start_string = ''.join(
        ['{}'.format(random.randint(0, 9)) for i in range(81)])
    mixing.random.shuffle = lambda s: 0
    result_string = mixing.change_numbers(start_string)
    assert start_string == result_string


# ======================
def test_change_numbers_1():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '0'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3206549870' == result_string


# ======================
def test_change_numbers_2():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '2'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3226549870' == result_string


# ======================
def test_change_numbers_3():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '3'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3236549870' == result_string


# ======================
def test_change_numbers_4():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '4'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3246549870' == result_string


# ======================
def test_change_numbers_5():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '5'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3256549870' == result_string


# ======================
def test_change_numbers_6():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '6'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3266549870' == result_string


# ======================
def test_change_numbers_7():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '7'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3276549870' == result_string


# ======================
def test_change_numbers_8():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '8'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3286549870' == result_string


# ======================
def test_change_numbers_9():
    # Overwrite shuffle
    def set_v(s):
        s[0] = '9'
    mixing.random.shuffle = lambda s: set_v(s)
    start_string = '3216549870'
    result_string = mixing.change_numbers(start_string)
    assert start_string != result_string
    assert '3296549870' == result_string


# ======================
def test_change_numbers_10():
    for n in range(10):  # We try 10 iterations, to ensure not to
        # fall into a lucky-case
        # Not chaing numbers using a random grid
        key = list('123456789')
        random.shuffle(key)

        # Overwrite shuffle
        def set_v(s):
            for n in range(9):
                s[n] = key[n]
        mixing.random.shuffle = lambda s: set_v(s)
        start_string = '123456789'
        result_string = mixing.change_numbers(start_string)
        assert ''.join(key) == result_string


"""
Testing flip_rows
"""


# ======================
def test_flip_rows_t0_constant():
    # No fliping rows using a random grid
    start_string = ''.join(
        ['{}'.format(random.randint(0, 9)) for i in range(81)])
    mixing.random.shuffle = lambda s: 0
    result_string = mixing.flip_rows(start_string)
    assert start_string == result_string


# ======================
def test_flip_rows_t1():
    # Set string
    start_string = ''.join(
        ['{}'.format(int(i/9)) for i in range(81)])

    # Overload the shuffle - 1
    def fake_shuffle_3(lst):
        lst[0] = 2
        lst[1] = 0
        lst[2] = 1
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_rows(start_string)
    expected_string = ''.join(
        ['{}'.format(int(i/9)) for i in range(54, 81)]
        + ['{}'.format(int(i/9)) for i in range(27)]
        + ['{}'.format(int(i/9)) for i in range(27, 54)]
    )
    assert expected_string == result_string


# ======================
def test_flip_rows_t2():
    # Set string
    start_string = ''.join(['{}'.format(int(i/9)) for i in range(81)])

    # Overload the shuffle - 2
    def fake_shuffle_3(lst):
        lst[0] = 2
        lst[1] = 1
        lst[2] = 0
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_rows(start_string)
    expected_string = ''.join(
        ['{}'.format(int(i/9)) for i in range(54, 81)]
        + ['{}'.format(int(i/9)) for i in range(27, 54)]
        + ['{}'.format(int(i/9)) for i in range(27)]
    )
    assert expected_string == result_string


# ======================
def test_flip_rows_t3():
    # Set string
    start_string = ''.join(['{}'.format(int(i/9)) for i in range(81)])

    # Overload the shuffle - 2
    def fake_shuffle_3(lst):
        lst[0] = 0
        lst[1] = 2
        lst[2] = 1
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_rows(start_string)
    expected_string = ''.join(
        ['{}'.format(int(i/9)) for i in range(27)]
        + ['{}'.format(int(i/9)) for i in range(54, 81)]
        + ['{}'.format(int(i/9)) for i in range(27, 54)]
    )
    assert expected_string == result_string


# ======================
def test_flip_rows_t4():
    # Set string
    start_string = ''.join(['{}'.format(int(i/9)) for i in range(81)])

    # Overload the shuffle - 2
    def fake_shuffle_3(lst):
        lst[0] = 1
        lst[1] = 0
        lst[2] = 2
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_rows(start_string)
    expected_string = ''.join(
        ['{}'.format(int(i/9)) for i in range(27, 54)]
        + ['{}'.format(int(i/9)) for i in range(27)]
        + ['{}'.format(int(i/9)) for i in range(54, 81)]
    )
    assert expected_string == result_string


# ======================
def test_flip_rows_t5():
    # Set string
    start_string = ''.join(['{}'.format(int(i/9)) for i in range(81)])

    # Overload the shuffle - 2
    def fake_shuffle_3(lst):
        lst[0] = 1
        lst[1] = 2
        lst[2] = 0
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_rows(start_string)
    expected_string = ''.join(
        ['{}'.format(int(i/9)) for i in range(27, 54)]
        + ['{}'.format(int(i/9)) for i in range(54, 81)]
        + ['{}'.format(int(i/9)) for i in range(27)]
    )
    print(expected_string)
    print(result_string)
    assert expected_string == result_string


# ======================
def test_flip_rows_constant():
    # No fliping rows using a random grid
    start_string = ''.join(
        ['{}'.format(random.randint(0, 9)) for i in range(81)])
    mixing.random.shuffle = lambda s: 0
    result_string = mixing.flip_rows(start_string)
    assert start_string == result_string


"""
Testing flip_cols
"""


# ======================
def test_flip_cols_t0():
    # Set string
    start_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)])

    # Overload the shuffle
    def fake_shuffle_3(lst):
        lst[0] = 0
        lst[1] = 1
        lst[2] = 2
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_cols(start_string)
    expected_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)]
    )
    assert expected_string == result_string


# ======================
def test_flip_cols_t1():
    # Set string
    start_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)])

    # Overload the shuffle
    def fake_shuffle_3(lst):
        lst[0] = 2
        lst[1] = 0
        lst[2] = 1
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_cols(start_string)
    expected_string = ''.join(
        ['{}'.format(1 + (3 + i) % 9) for i in range(81)]
    )
    assert expected_string == result_string


# ======================
def test_flip_cols_t2():
    # Set string
    start_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)])

    # Overload the shuffle
    def fake_shuffle_3(lst):
        lst[0] = 1
        lst[1] = 2
        lst[2] = 0
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_cols(start_string)
    expected_string = ''.join(
        ['{}'.format(1 + (6 + i) % 9) for i in range(81)]
    )
    assert expected_string == result_string


# ======================
def test_flip_cols_t3():
    # Set string
    start_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)])

    # Overload the shuffle
    def fake_shuffle_3(lst):
        lst[0] = 2
        lst[1] = 1
        lst[2] = 0
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_cols(start_string)
    expected_string = ''.join(
        ['7', '8', '9', '4', '5', '6', '1', '2', '3']*9
    )
    assert expected_string == result_string


# ======================
def test_flip_cols_t4():
    # Set string
    start_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)])

    # Overload the shuffle
    def fake_shuffle_3(lst):
        lst[0] = 1
        lst[1] = 0
        lst[2] = 2
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_cols(start_string)
    expected_string = ''.join(
        ['4', '5', '6', '1', '2', '3', '7', '8', '9']*9
    )
    assert expected_string == result_string


# ======================
def test_flip_cols_t5():
    # Set string
    start_string = ''.join(
        ['{}'.format(1 + i % 9) for i in range(81)])

    # Overload the shuffle
    def fake_shuffle_3(lst):
        lst[0] = 0
        lst[1] = 2
        lst[2] = 1
    mixing.random.shuffle = lambda s: fake_shuffle_3(s)

    # Get the result
    result_string = mixing.flip_cols(start_string)
    expected_string = ''.join(
        ['1', '2', '3', '7', '8', '9', '4', '5', '6']*9
    )
    assert expected_string == result_string


# ======================
def test_flip_cols_constant():
    # No fliping cols using a random grid
    start_string = ''.join(
        ['{}'.format(random.randint(0, 9)) for i in range(81)])
    mixing.random.shuffle = lambda s: 0
    result_string = mixing.flip_cols(start_string)
    assert start_string == result_string


"""
Testing the rotations
"""


# ======================
def test_rotate_0():
    start_string = ''.join(
        ['{}'.format(random.randint(0, 9)) for i in range(81)])
    mixing.random.randint = lambda s, e: 0
    result_string = mixing.rotate(start_string)
    assert start_string == result_string


# ======================
def test_rotate_90():
    # Using a fixed grid
    start_string = ''.join(['{}'.format(i % 9) for i in range(81)])
    mixing.random.randint = lambda s, e: 1
    result_string = mixing.rotate(start_string)
    expected_string = ''.join(['{}'.format(int(i/9)) for i in range(81)])
    assert expected_string == result_string


# ======================
def test_rotate_180():
    # Using a fixed grid
    start_string = ''.join(['{}'.format(i % 9) for i in range(81)])
    mixing.random.randint = lambda s, e: 2
    result_string = mixing.rotate(start_string)
    expected_string = ''.join(['{}'.format(8-i % 9) for i in range(81)])
    assert expected_string == result_string


# ======================
def test_rotate_270():
    # Using a fixed grid
    start_string = ''.join(['{}'.format(i % 9) for i in range(81)])
    # 270°
    mixing.random.randint = lambda s, e: 3
    result_string = mixing.rotate(start_string)
    expected_string = ''.join(['{}'.format(8-int(i/9)) for i in range(81)])
    assert expected_string == result_string
