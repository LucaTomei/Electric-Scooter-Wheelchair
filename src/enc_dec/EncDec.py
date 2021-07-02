# With this module you can easily encode or decode Xiaomi-Ninebot firmware files or make ZIP archives
# It takes as input the binary file sniffed by the Ninebot / Xiaomi application and returns the 
# decrypted file for the subsequent modification of the parameters.

# We can use the same module to encrypt the previously modified and decrypted file

from struct import pack, unpack

try:
	from .Binary_Utilities import Binary_Utilities
except Exception as e:
	from Binary_Utilities import Binary_Utilities

class EncDec(object):
	def __init__(self):
		self.Binary_Utilities_OBJ = Binary_Utilities()
		
		UPDKEY = b'\xFE\x80\x1C\xB2\xD1\xEF\x41\xA6\xA4\x17\x31\xF5\xA0\x68\x24\xF0'
		self.key = UPDKEY
		self.iv = b'\x00' * 8
		self.offset = 0

	def _UpdateKey(self):
		k = bytearray()
		for i in range(16):	k.append((self.key[i] + i) & 0xFF)
		self.key = k

	def encrypt(self, data):
		data = self.Binary_Utilities_OBJ.pad(data)
		assert len(data) % 8 == 0, 'data must be 8 byte aligned!'
		res = bytearray()
		for i in range(0, len(data), 8):
			ct = self.Binary_Utilities_OBJ.encrypt_ecb(self.Binary_Utilities_OBJ.xor(self.iv, data[i:i+8]), self.key)
			res += ct
			self.iv = ct
			self.offset += 8
			if (self.offset % 1024) == 0:	self._UpdateKey()
		return res

	def decrypt(self, data):
		assert len(data) % 8 == 0, 'data must be 8 byte aligned!'
		res = bytearray()
		for i in range(0, len(data), 8):
			ct = data[i:i+8]
			res += self.Binary_Utilities_OBJ.xor(self.iv, self.Binary_Utilities_OBJ.decrypt_ecb(ct, self.key))
			self.iv = ct
			self.offset += 8
			if (self.offset % 1024) == 0:	self._UpdateKey()
		return self.Binary_Utilities_OBJ.unpad(res)



if __name__ == '__main__':
	EncDec_OBJ = EncDec()
