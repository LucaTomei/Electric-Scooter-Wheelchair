#!/usr/bin/python3
from binascii import hexlify
import struct, keystone, sys
from enc_dec import EncDec

from Firmware_Utils import Firmware_Utils


# https://web.eecs.umich.edu/~prabal/teaching/eecs373-f10/readings/ARMv7-M_ARM.pdf
MOVW_T3_IMM = [*[None]*5, 11, *[None]*6, 15, 14, 13, 12, None, 10, 9, 8, *[None]*4, 7, 6, 5, 4, 3, 2, 1, 0]
MOVS_T1_IMM = [*[None]*8, 7, 6, 5, 4, 3, 2, 1, 0]



## Firmware Patcher Main class
class FirmwarePatcher():
    def __init__(self, data):
    	self.Firmware_Utils_OBJ = Firmware_Utils()
    	self.data = bytearray(data)

        # Keystone is a lightweight multi-platform, multi-architecture assembler framework
        # Keystone compile in this case arch arm assembly instruction to thumb (thumbs are set of 16 bit instructions)
        # https://gist.github.com/aquynh/d7cf8788b4e16a8c3078
    	self.ks = keystone.Ks(keystone.KS_ARCH_ARM, keystone.KS_MODE_THUMB)

    def encrypt(self):
        self.data = EncDec.EncDec().encrypt(self.data)
    def decrypt(self):
        self.data = EncDec.EncDec().decrypt(self.data)
    
    # Disable electric scooter automatic DRV updates on firmware changes
    def version_spoofing(self):
        sig = [0x4F, 0xF4, 0x93, 0x70, 0xA0, 0x86, 0x12, 0x48, 0x00, 0x78]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig)
        pre = self.data[ofs:ofs+4]
        post = bytes(self.ks.asm('MOVW   R0, #0x526')[0])
        self.data[ofs:ofs+4] = post
        return [(ofs, pre, post)]
    
	
	# Minimum speed below which the kers is activated
    def kers_min_speed(self, kmh):
        val = struct.pack('<H', int(kmh * 390))
        sig = [0x25, 0x68, 0x40, 0xF6, 0x24, *[None]*2, 0x42]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 2
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 4, val, MOVW_T3_IMM)
        return [(ofs, pre, post)]


    # Motor start speed
    def motor_start_speed(self, kmh):
        ret = []
        val = int(kmh * 390)
        val = val - (val % 16)
        assert val.bit_length() <= 12, 'bit length overflow'
        sig = [0x4B, 0x01, None, None, 0x48, 0x00, None, None, None, 0xB6, 0xF5, 0xC5, 0x6F, 0x0D, 0xDB]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 9
        pre = self.data[ofs:ofs + 4]
        post = bytes(self.ks.asm('CMP.W R6, #{:n}'.format(val))[0])
        self.data[ofs:ofs + 4] = post
        ret.append((ofs, pre, post))
        ofs += 4

        pre, post = self.data[ofs:ofs + 1], bytearray((0x0D, 0xDB))
        self.data[ofs:ofs + 2] = post
        ret.append((ofs, pre, post))
        return ret

    # If you plan to use the Ninebot Max G30 lock functionality from the 
    # application and you do not want the scooter to turn off after a few hours, 
    # you need to flag this field.
    def stay_on_locked(self):
        sig = [0x03, 0xF0, None, None, 0xF0, 0x7B]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig)
        pre = self.data[ofs:ofs+4]
        post = bytes(self.ks.asm('NOP;NOP')[0])
        self.data[ofs:ofs+4] = post
        return [(ofs, pre, post)]
    
    # This option removes the ignition when connecting the charger and allows
    # you to connect additional batteries in parallel to increase autonomy.
    def remove_charging_mode(self):
        sig = [0x20, 0xB1, 0x84, 0xF8, 0x38, 0x60, 0xE0, 0x7B, 0x18, 0xB1]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig)
        pre = self.data[ofs:ofs+2]
        post = bytes(self.ks.asm('NOP')[0])
        self.data[ofs:ofs+2] = post
        return [(ofs, pre, post)]
	

	# This type of algorithm replace the linear throttle curve with a quadratic one.
	# With the quadratic curve, the power delivery works on a logarithmic scale, 
	# sweet at the low end and then soaring on the final.
    def throttle_alg(self):
        sig = [0xF0, 0xB5, 0x25, 0x4A, 0x00, 0x24, 0xA2, 0xF8, 0xEC, 0x40, 0x24, 0x49]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
        pre, post = self.data[ofs:ofs + 1], bytearray((0x01, 0x24))
        self.data[ofs:ofs + 2] = post
        return [(ofs, pre, post)]

        return ret
    
    # Speed parameters
    def speed_params(self, normal_kmh, normal_phase, normal_battery):
        ret = []
        sig = [0x95, 0xF8, 0x4F, 0x80, 0x4D, 0xF2, 0xD8, 0x63, 0xB8, 0xF1, 0x01, 0x0F, 0x0A, 0xD0]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
        pre = self.data[ofs:ofs+4]
        post = bytes(self.ks.asm('MOVW R3, #{:n}'.format(normal_phase))[0])
        self.data[ofs:ofs+4] = post
        ret.append([ofs, pre, post])

        sig = [0x46, 0xF2, 0xA8, 0x12, 0xFB, 0xB1, 0x22, 0xE0, 0x95, 0xF8]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig)
        pre = self.data[ofs:ofs+4]
        post = bytes(self.ks.asm('MOVW R2, #{:n}'.format(normal_battery))[0])
        self.data[ofs:ofs+4] = post
        ret.append([ofs, pre, post])

        sig = [0x90, 0x42, 0x01, 0xD2, 0xE0, 0x85, 0x00, 0xE0, 0xE2, 0x85, 0x21]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig)
        pre = self.data[ofs:ofs+2]
        post = bytes(self.ks.asm('CMP R2, R2')[0])
        self.data[ofs:ofs+2] = post
        ret.append([ofs, pre, post])

        ofs += 10
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 2, struct.pack('<B', normal_kmh), MOVS_T1_IMM)
        ret.append([ofs, pre, post])
        self.data[ofs:ofs+2] = post
        ret.append([ofs, pre, post])

        return ret
    

    # Motor Power Constant represents the ability of the motor to convert electrical power 
    # into mechanical power. The motor constant is given by:
    #		k_m = T/\sqrt(P), where
    #  - k_m = motor constant (Nm / √ Watt)
    #  - T = torque (Nm)
    #  - P = resistive power losses (also known as I^2\cdot R losses) (W)

    # therefore The Motor Power constant is a value that increases the power delivered
    # in an inversely proportional way to the set number, ie the lower this number the higher the power will be.


    # lower value = more power
    # original = 51575 (~500 Watt)
    # DYoC = 40165 (~650 Watt)
    # CFW W = 27877 (~850 Watt)
    # CFW = 25787 (~1000 Watt)
    def mpc(self, val):
        val = struct.pack('<H', int(val))
        ret = []
        sig = [0x31, 0x68, 0x2A, 0x68, 0x09, 0xB2, 0x09, 0x1B, 0x12, 0xB2, 0xD3, 0x1A, 0x4C, 0xF6, 0x77, 0x12]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 12
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 4, val, MOVW_T3_IMM)
        ret.append((ofs, pre, post))
        ofs += 4
 
        ofs += 4
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 4, val, MOVW_T3_IMM)
        ret.append((ofs, pre, post))
 
        sig = [0xD3, 0x1A, 0x4C, 0xF6, 0x77, 0x12]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig, None, ofs, 100) + 2
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 4, val, MOVW_T3_IMM)
        ret.append((ofs, pre, post))
        ofs += 4
 
        ofs += 4
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 4, val, MOVW_T3_IMM)
        ret.append((ofs, pre, post))
 
        sig = [0xC9, 0x1B, 0x4C, 0xF6, 0x77, 0x13]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig, None, ofs, 100) + 2
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 4, val, MOVW_T3_IMM)
        ret.append((ofs, pre, post))
        return ret

    def bypass_BMS(self):
        sig = [0x06, 0x49, 0x4A, 0x78, 0x82, 0x42, 0x02, 0xD8, 0x4A, 0x78]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig)
        pre = self.data[ofs:ofs+2]
        post = bytes(self.ks.asm('BX LR')[0])
        self.data[ofs:ofs+2] = post
        return [(ofs, pre, post)]

	
    # After how many seconds at constant speed the cruise control will start working, 
    # the standard value is 5 seconds and can be set in a range from 1 to 10 seconds.
    def cc_delay(self, delay):
        delay = int(delay * 200)
        assert delay.bit_length() <= 12, 'bit length overflow'
        sig = [0x48, 0xB0, 0xF8, 0xF8, None, 0x33, 0x4A, 0x4F, 0xF4, 0x7A, 0x71, 0x01, 0x28]
        mask = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xF8, 0xFE, 0xFF, 0xFF, 0xFF, 0xFE, 0xFF, 0xFE]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig, mask) + 7
        pre = self.data[ofs:ofs+4]
        post = bytes(self.ks.asm('MOV.W R1, #{:n}'.format(delay))[0])
        self.data[ofs:ofs+4] = post
        return [(ofs, pre, post)]


    # Maximum speed value
    def max_speed(self, kmh):
        ret = []
        val = struct.pack('<B', int(kmh))
        sig = [None, 0xF8, 0x34, 0xC0, None, None, 0x43, 0xF2]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 2, val, MOVS_T1_IMM)
        ret.append((ofs, pre, post))

        sig = [None, None, None, None, 0x17, None, None, 0x83, 0x46, 0xF6, 0x60]
        ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
        pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 2, val, MOVS_T1_IMM)

        ret.append((ofs, pre, post))

        if self.data[0x7BAA] == 0x33 and self.data[0x7BAB] == 0x11:
            sig = [None, 0xF8, 0x2E, 0xE0, 0x22, 0x20, 0xE0, 0x83, 0x1B, 0xE0, 0x95]
            ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
            pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 2, val, MOVS_T1_IMM)
        elif (self.data[0x8242] == 0xA8 and self.data[0x8243] == 0x71) or \
             (self.data[0x8246] == 0x51 and self.data[0x8247] == 0x11):
            sig = [0xDE, 0xD0, 0x11, 0xE0, 0x22, None, None, 0x83, 0xDE, 0xE7, 0x95]
            ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
            pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 2, val, MOVS_T1_IMM)
        else:
            sig = [0x52, 0xC0, 0x4F, 0xF0, 0x22, 0x0E, 0x4C, 0xF2, 0x50, None, None]
            ofs = self.Firmware_Utils_OBJ.GetPattern(self.data, sig) + 4
            pre, post = self.Firmware_Utils_OBJ.Patch(self.data, ofs, 2, val, MOVS_T1_IMM)

        ret.append((ofs, pre, post))
        return ret


if __name__ == "__main__":
	modality = 0
	if len(sys.argv) != 3:
		default_input_file = "files/input/DRV126.bin"
		default_output_file = "files/output/FIRM.bin.enc"

		to_print = "[*] Automatic mode [*]\n- Input file = %s\n - Output file = %s\n\n\t Custom Firmware Created Successfully!" %(default_input_file, default_output_file)
		print(to_print)

		with open(default_input_file, 'rb') as fp:	data = fp.read()
	else:
		modality = 1
		with open(sys.argv[1], 'rb') as fp:	data = fp.read()

	cfw = FirmwarePatcher(data)
	cfw.motor_start_speed(6)
	cfw.cc_delay(2)
	cfw.throttle_alg()
	cfw.stay_on_locked()

	cfw.encrypt()

	output_filename = default_output_file if modality == 0 else sys.argv[2]

	with open(output_filename, 'wb') as fp:	fp.write(cfw.data)
