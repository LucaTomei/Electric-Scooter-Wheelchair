#!/usr/bin/python
from sys import argv, exit
from os.path import exists, getsize
from EncDec import EncDec

class Encryption_Test(object):
	def __init__(self):
		self.encdec_obj = EncDec()

	def make_test(self, choice):
		assert choice == 1 or choice == 2, "\n\n\tchoice can be 1 or 2"
		if choice == 1:
			print("Insert binary to Encrypt")
			input_filename = input()
			if not exists(input_filename):
				print("Input filename doesn't exists!")
				exit(1)

			print("Insert output filename")
			output_filename = input()

			hfi = open(input_filename, 'rb')
			hfo = open(output_filename + ".bin", 'wb')

			hfo.write(self.encdec_obj.encrypt(hfi.read()))

			hfo.close()
			hfi.close()
		elif choice == 2:
			print("Insert binary to Decrypt")
			input_filename = input()
			if not exists(input_filename):
				print("Input filename doesn't exists!")
				exit(1)
			
			print("Insert output filename (withou '.enc')")
			output_filename = input()

			hfi = open(input_filename, 'rb')
			hfo = open(output_filename + ".bin.enc", 'wb')

			hfo.write(self.encdec_obj.decrypt(hfi.read()))

			hfo.close()
			hfi.close()

	def main(self):
		print("[*] Encryption/Decryption Test[*]")
		print("\t[1] for Encryption\n\t[2] for Decryption")
		choice = input()
		if choice.isnumeric():
			self.make_test(int(choice))
		else:
			print("The choice made is not correct")

if __name__ == '__main__':
	Encryption_Test_OBJ = Encryption_Test()
	Encryption_Test_OBJ.main()