#!/usr/bin/env python3


def return_evens(num_list):
    even_elements = [n for n in num_list if n % 2 == 0]
    return even_elements
    pass


def make_exclamation(sentence_list):
    excalmation_list = [n + "!" for n in sentence_list]
    return excalmation_list
    pass
