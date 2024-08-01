# -*- coding: utf-8 -*-
"""dictionaries_exercise

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PxJrzRxk5GXMnlc5dqN5xQWX9Lwdn_LP
"""

global digits
digits = ''
def dec_to_bin(decimals):
  global digits
  if decimals > 1:
    dec_to_bin(decimals//2)
  digits += str(decimals % 2)

def bin_dict(numbers):
  d = {}
  for n in range(numbers):
    global digits
    digits = ''
    dec_to_bin(n)
    d[n] = digits.rjust(4,'0')
  return d

bin_dict(15)

