#!/usr/bin/python
from sys import argv, exit
from os.path import getsize
from EncDec import EncDec

if len(argv) != 3:  exit('Usage: ' + argv[0] + ' <infile> <outfile>')

cry = EncDec()

hfi = open(argv[1], 'rb')
hfo = open(argv[2], 'wb')

hfo.write(cry.encrypt(hfi.read()))

hfo.close()
hfi.close()



# class Encrypt(object):
#     def __init__(self):
#         self.EncDec_OBJ = EncDec()

#     def main(self):
#         pass   