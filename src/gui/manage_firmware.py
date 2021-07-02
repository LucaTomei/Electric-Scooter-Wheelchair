import requests, os, zipfile




class Manage_Firmware(object):
	def __init__(self):
		self.firmware_url = "https://cfw-cdn-max.scooterhacking.org/?output=zip2&version=DRV126&compat_patches=on&region=G30P&version_spoofing=on&showbatt=on&boot_workmode=3&beep_lock=1&beep_unlock=1&beep_reboot=2&beep_shutdown=2&beep_cruise_control=2&beep_charger_in=1&beep_charger_out=3&voltage=36&p_sports=33000&p_drive=25000&i_sports=55000&i_drive=28000&i_eco=23000&max_speed_us=26&max_speed_eu=26&max_speed_de=26&direct_power_control=dyn&direct_power_control_curve=quadratic&current_raising_coefficient=1800&motor_start_speed=0&brake_limit=120&brake_i_min=6000&brake_i_max=35000&kers_min_speed=6&no_kers=on&brake_current_raising_coefficient=500&brake_light_mode=stock&brake_light_flash_frequency=235&cruise_control_delay=3&no_cruise_control=on&error_raising_level=1&no_overspeed_alarm=on&stay_on_locked=on&wheel_size=10.0"

		self.download_dir = os.path.join(os.path.expanduser('~'), 'downloads')
		self.zip_filename = self.download_dir + "/" + "cfw.zip"

		self.cfw_dir = self.download_dir + "/cfw"

		self.params = """
			- Firmware Version: DRV126
			- Max speed: 25
			- Nominal draw: 33.0A
			- Max current: 55.0A
			- Stay on when scooter is locked
			- Wheel size: 10.0 inches
			- NO KERS
			- Throttle current coefficient: 1800
			- NO Cruise Control
			- Motor start speed: 0 km/h
			- Version spoofing
			"""

	def write_bin_file(self, filename, content):
		file = open(filename, "wb")
		file.write(content)
		file.close()

	def download_firmware(self):
		response = requests.get(self.firmware_url)
		content = response.content

		self.write_bin_file(self.zip_filename, content)

	def extract_zip_file(self, filename, extract_to):
		with zipfile.ZipFile(filename, 'r') as zip_ref:	zip_ref.extractall(extract_to)

	def make_folder(self, folder_name):
		if os.path.exists(folder_name): os.system("rm -rf " + folder_name)
		os.mkdir(folder_name)

	def remove_tmp_files(self):
		os.system("rm -rf " + self.cfw_dir + "/*.txt")
		os.system("rm -rf " + self.cfw_dir + "/*.json")


	def write_txt_file(self, filename, content):
		file = open(filename, "w")
		file.write(content)
		file.close()

	def make_params_file(self, params_dir):
		self.write_txt_file(params_dir + "/params.txt", self.params)


	def make_zip_file(self, path):
		ziph = zipfile.ZipFile(self.zip_filename, 'w', zipfile.ZIP_DEFLATED)
		for root, dirs, files in os.walk(path):
			for file in files:
				ziph.write(os.path.join(root, file), 
					os.path.relpath(os.path.join(root, file), 
						os.path.join(path, '..')))
		ziph.close()



		

	def main(self):
		if os.path.exists(self.zip_filename):	os.remove(self.zip_filename)
		self.make_folder(self.cfw_dir)
		self.download_firmware()
		self.extract_zip_file(self.zip_filename, self.cfw_dir)
		self.remove_tmp_files()
		self.make_params_file(self.cfw_dir)

		os.remove(self.zip_filename)

		self.make_zip_file(self.cfw_dir)

		if os.path.exists(self.cfw_dir):	os.system("rm -rf " + self.cfw_dir)




