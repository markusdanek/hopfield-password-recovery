# Import libraries
from __future__ import division, print_function
from collections import OrderedDict
from operator import itemgetter
from tqdm import tqdm
from neupy import algorithms
import random
import pprint
import string
import numpy as np


def str2bin(text, max_length=30):
    if len(text) > max_length:
        raise ValueError("Text can't contain more than {} symbols".format(max_length))

    text = text.rjust(max_length)

    bits_list = []
    for symbol in text:
        bits = bin(ord(symbol))
        # Cut `0b` from the beggining and fill with zeros if they are missed
        bits = bits[2:].zfill(8)
        bits_list.extend(map(int, bits))

    return list(bits_list)
