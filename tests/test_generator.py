import unittest

from generator import choose_random_name

def test_random_choice_from_list():
    words = ['foo','bar','foobar']
    assert choose_random_name(words) in words

def test_random_choice_not_in_list():
    words = ['foo','bar','foobar']
    assert choose_random_name(words) != 'baz'
