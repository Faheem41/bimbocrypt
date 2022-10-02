"""
  Copyright (C) 2021-2022 Md. Faheem Hossain fmhossain2941@gmail.com
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""



#! /usr/bin/env python3
# bimbocrypt.py
# a code to encrypt and decrypt text



from math import ceil, floor
from time import sleep
import numpy as np
from secrets import randbelow
# 'Herr Rozwel' suggested the secrets module instead of random module
from privatefunc import PrivateFunc
privatefunc = PrivateFunc("bimbocrypt")



# defining exceptions

class DangerousInput(Exception):

    def __init__(self, mssg):
        self.mssg = mssg
        super().__init__(self.mssg)

    def __str__(self):
        return f'{self.mssg}'



# find number of rows from password

@privatefunc.private
def prepare(password):
    rowN = int(password)
    rollN = int(str(password)[-1])
    xT = int(str(password)[0])**2 % rowN \
         or 7 % rowN
    return rowN, rollN, xT



# encryption function

def encrypt(text, password):

    text = text.replace('', ' ').split(' ')
    del(text[0], text[-1])
    l = len(text)
    i = 0
    while i < l:
        if text[i] == '':
            if text[i+1] == '':
                del(text[i])
                text[i] = ' '
                l = len(text)
        i += 1

    try:
        p = int(password)
        assert(p < len(text))
    except ValueError:
        raise DangerousInput(
            "\nPASSWORD SHOULD CONTAIN ONLY NUMBERS"
        )
    except AssertionError:
        raise DangerousInput(
            "\nTRY USING A PASSWORD LESS THAN: " + str(len(text))
        )

    data = "aeiuAI.,bBzZfO0ertns" \
            .replace('', ' ') \
            .split(' ')
    del(data[0], data[-1])


    text += ['o']  # text separator

    # security check:
    # # number of column should not be equal to 0 or 1
    while True:
        l = len(text)
        rowN, rollN, xT = prepare(p)
        columnN = ceil(l / rowN)
        if columnN <= 1:
            text += ['e']
            continue
        break

    new_l = rowN * columnN
    # print(rowN, columnN, rollN, xT, 111)
    # print(text, 1)

    # preparing the data to fit in a matrix
    xTdata1 = [data[randbelow(20)] for _ in range(new_l - l)]
    # len(data) - 1 = 19
    text += xTdata1
    # print(text, 2)

    # let's start
    text = np.array(text) \
           .reshape(rowN, columnN) \
           .T \
           .reshape(1, new_l)
    # print(text, 3)
    text = np.roll(text, rollN)
    # print(text, 4)
    text = text.tolist()
    text = ''.join(text[0])

    # a technique adopted to make the length of the text unguessable
    xTdata2 = [data[randbelow(20)] for _ in range(xT)]
    xTdata2 = ''.join(xTdata2)
    text += xTdata2
    # print(text, 'end')

    return text



# decryption function

def decrypt(text, password):

    text = text.replace('', ' ').split(' ')
    del(text[0], text[-1])
    l = len(text)
    i = 0
    while i < l:
        if text[i] == '':
            if text[i+1] == '':
                del(text[i])
                text[i] = ' '
                l = len(text)
        i += 1

    try:
        p = int(password)
    except ValueError:
        raise DangerousInput(
            "\nWRONG PASSWORD"
        )

    sleep(1)
    # function takes at least 1s to complete

    l = len(text)
    rowN, rollN, xT = prepare(p)
    columnN = floor(l / rowN)
    # print(rowN, columnN, rollN, xT, 111)
    # print(text, 1)

    new_l = rowN * columnN
    text = text[:new_l]
    # print(text, 2)

    text = np.array(text)
    text = np.roll(text, -1*rollN)
    # print(text, 3)
    text = np.array(text) \
           .reshape(columnN, rowN) \
           .T \
           .reshape(1, new_l)
    # print(text, 4)
    text = text.tolist()
    text = ''.join(text[0])
    i = -1
    while True:
         if text[i] == 'o':
             i -= 1
             break
         i -= 1
    text = text[:i+1]
    # print(text, 5)

    return text

