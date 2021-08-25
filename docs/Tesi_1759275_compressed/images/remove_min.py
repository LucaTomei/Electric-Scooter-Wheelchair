import os

this_dir = os.getcwd()
dir_content = os.listdir()

directories = ["finished_project", "graphs"]



for filename in dir_content:
	if 'min' in filename:
		this_filename = filename.replace("-min", "")
		os.rename(filename, this_filename)

for directory in directories:
	tmp_location = os.chdir(directory)
	dir_content = os.listdir()
	for filename in dir_content:
		if 'min' in filename:
			this_filename = filename.replace("-min", "")
			os.rename(filename, this_filename)
	os.chdir(this_dir)