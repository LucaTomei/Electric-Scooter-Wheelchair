# Signature exception
class SgnException(Exception):
	pass

class Firmware_Utils(object):
	def __init__(self):
		pass

	def Patch(self, data, ofs, size, imm, signature):
		assert size % 2 == 0, 'size must be power of 2!'
		assert len(signature) == size * 8, 'signature must be exactly size * 8 long!'
		imm = int.from_bytes(imm, 'little')
		sfmt = '<' + 'H' * (size // 2)

		sigs = [signature[i:i + 16][::-1] for i in range(0, len(signature), 16)]
		orig = data[ofs:ofs+size]
		words = struct.unpack(sfmt, orig)

		patched = []

		for i, word in enumerate(words):
			for j in range(16):
				imm_bitofs = sigs[i][j]
				if imm_bitofs is None:	continue

				imm_mask = 1 << imm_bitofs
				word_mask = 1 << j

				if imm & imm_mask:	word |= word_mask
				else: word &= ~word_mask
			patched.append(word)

		packed = struct.pack(sfmt, *patched)
		data[ofs:ofs+size] = packed
		return (orig, packed)


    # To find the pattern
	def GetPattern(self, data, signature, mask=None, start=None, maxit=None):
		sig_len = len(signature)

		if start is None:	start = 0
		stop = len(data)

		if maxit is not None:	stop = start + maxit

		if mask:
			assert sig_len == len(mask), 'mask must be as long as the signature!'
			for i in range(sig_len):
				if signature[i] is not None:	signature[i] &= mask[i]

		for i in range(start, stop):
			matches = 0
			while signature[matches] is None or signature[matches] == (data[i + matches] & (mask[matches] if mask else 0xFF)):
				matches += 1
				if matches == sig_len:	return i

		raise SgnException('Pattern not found!')

