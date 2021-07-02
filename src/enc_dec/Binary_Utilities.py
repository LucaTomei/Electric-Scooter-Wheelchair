from struct import pack, unpack

class Binary_Utilities(object):
	def __init__(self):
		pass	

	def xor(self, s1, s2):
		res = bytearray()
		for i in range(8):	res.append(s1[i] ^ s2[i])
		return res

	# check autenticity of the data
	def checksum(self, data):
		s = 0
		for i in range(0, len(data), 4):	s += unpack('<L', data[i:i+4])[0]
		return (((s >> 16) & 0xFFFF) | ((s & 0xFFFF) << 16)) ^ 0xFFFFFFFF


	# ECB
	# The simplest of the encryption modes is the electronic codebook (ECB) mode 
	# (named after conventional physical codebooks[19]). The message is divided into blocks, 
	# and each block is encrypted separately.

	# ecb encryption
	def ecb_enc(self, block, key):
		y, z = unpack('<LL', block)
		k = unpack('<LLLL', key)
		s = 0

		for i in range(32):
			s = (s + 0x9E3779B9) & 0xFFFFFFFF
			y = (y + (((z << 4) + k[0]) ^ (z + s) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF
			z = (z + (((y << 4) + k[2]) ^ (y + s) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF
		return pack('<LL', y, z)

	# ecb decryption
	def ecb_dec(self, block, key):
		y, z = unpack('<LL', block)
		k = unpack('<LLLL', key)
		s = 0xC6EF3720

		for i in range(32):
			z = (z - (((y << 4) + k[2]) ^ (y + s) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF
			y = (y - (((z << 4) + k[0]) ^ (z + s) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF
			s = (s - 0x9E3779B9) & 0xFFFFFFFF
		return pack('<LL', y, z)



	# The data which will be encrypted must be 8 byte aligned!
    # We also have to write a checksum to the last 4 bytes.
    # Zero pad for 4-byte aligning first:
	def pad(self, data):
		sz = len(data)
		if sz % 4:
			o = (4 - (sz % 4))
			data += b'\x00' * o
			sz += o
		
		# If we're 8-byte aligned now then add 4 zero pad bytes
		if (sz % 8) == 0:	data += b'\x00\x00\x00\x00'

		# so we can add our 4 checksum bytes and be 8-byte aligned
		return data + pack('<L', self.checksum(data))

	def unpad(self, data):
		chk = unpack('<L', data[-4:])[0]
		s = self.checksum(data[:-4])
		assert s == chk, 'checksum does not match!'
		return data[:-4]

