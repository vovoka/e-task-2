from task_2 import *
import pytest

def test_short_quation_positive_numbers_passed():
    assert humanise_equality('10 + 0 = 15') == 'ten plus zero equals fifteen'
    assert humanise_equality('+10 + 0 = +15') == 'ten plus zero equals fifteen'

def test_short_quation_negative_numbers_passed():
    assert humanise_equality('-10 * -1 = -1000000') == ('negative ten multiple'+
        ' negative one equals negative one million')

def test_short_quation_negative_numbers_passed():
    assert humanise_equality('-10 * 1 = -1000000') == ('negative ten multiple'+
        ' one equals negative one million')

def test_big_numbers_passed():
    assert humanise_equality('1000000000000000 * 1 = -1000') == ('one '+
        'quadrilion multiple one equals negative one thousand')

def test_long_quation_passed():
    assert humanise_equality('10 + 1 - 12 * 100 / 49 = 0') == ('ten plus one ' +
        'minus twelve multiple one hundred divide forty nine equals zero')

def test_underscores_numeric_literals_failed():
    assert humanise_equality('-10 * -1 = -1000_000') == 'invalid input'

def test_short_quation_failed():
    assert humanise_equality('6 = 6') == 'invalid input'

def test_wrong_operator_failed():
    assert humanise_equality('10 ^ 5 = 15') == 'invalid input'

def test_no_space_separator_failed():
    assert humanise_equality('10 +5 = 15') == 'invalid input'

def test_multiple_space_separator_failed():
    assert humanise_equality('10 +    5 = 15') == 'invalid input'

def test_alternative_space_separator_failed():
    assert humanise_equality('10_+_5_=_15') == 'invalid input'

def test_char_in_quation_failed():
    assert humanise_equality('10 + a = 15') == 'invalid input'

def test_random_text_failed():
    assert humanise_equality('Beautiful is better than ugly.' +
        'Explicit is better than implicit.') == 'invalid input'
