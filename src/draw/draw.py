import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def getFileContent(filename):
	file = open(filename, "r")
	content = file.read()
	file.close()
	return content

def parseDate(datestr):
	"09.08.2021 10:28:17.542"
	datestr = ".".join(datestr.split(".")[:3])
	return datetime.datetime.strptime(datestr, "%d.%m.%Y %H:%M:%S")

def getCSVTuple(content):
	list1 = []
	list2 = []
	content = content.split("\n")
	for i in content:
		if ',' in i:
			item = i.split(",")
			if item[0] != "" or item[1] != "":
				if "." in item[0]: 
					date = parseDate(item[0])
					list1.append(date)
				else:
					pass
					#list1.append(item[0])
				if "." in item[1]:
					list2.append(float(item[1]))
	return list1, list2

def mergeDates(batt1, corr1, dr1, pot1, temp1, volt1):
	content_batt1 = getFileContent(batt1)
	b1l1, b1l2 = getCSVTuple(content_batt1)
	
	content_corr1 = getFileContent(corr1)
	c1l1, c1l2 = getCSVTuple(content_corr1)
	
	content_dr1 = getFileContent(dr1)
	d1l1, d1l2 = getCSVTuple(content_dr1)
	
	content_pot1 = getFileContent(pot1)
	p1l1, p1l2 = getCSVTuple(content_pot1)
	
	content_temp1 = getFileContent(temp1)
	t1l1, t1l2 = getCSVTuple(content_temp1)
	
	content_volt1 = getFileContent(volt1)
	v1l1, v1l2 = getCSVTuple(content_volt1)
	
	iteration_len = min(len(b1l2), len(c1l1))
	iteration_len = min(iteration_len, len(d1l1))
	iteration_len = min(iteration_len, len(p1l1))
	iteration_len = min(iteration_len, len(t1l1))
	iteration_len = min(iteration_len, len(v1l1))

	b1l1o = []
	b1l2o = []
	c1l1o = []
	c1l2o = []
	d1l1o = []
	d1l2o = []
	p1l1o = []
	p1l2o = []
	t1l1o = []
	t1l2o = []
	v1l1o = []
	v1l2o = []
	for i in range(iteration_len):
		if b1l1[i] in c1l1 and b1l1[i] in d1l1 and b1l1[i] in p1l1 and b1l1[i] in t1l1 and b1l1[i] in v1l1 and b1l1[i] not in b1l1o:
			b1l1o.append(b1l1[i])
			b1l2o.append(b1l2[i])
			c1l1o.append(c1l1[i])
			c1l2o.append(c1l2[i])
			d1l1o.append(d1l1[i])
			d1l2o.append(d1l2[i])
			p1l1o.append(p1l1[i])
			p1l2o.append(p1l2[i])
			t1l2o.append(t1l2[i])
			t1l1o.append(t1l1[i])
			v1l1o.append(v1l1[i])
			v1l2o.append(v1l2[i])
	return b1l1o, b1l2o, c1l1o, c1l2o, d1l1o, d1l2o, p1l1o, p1l2o, t1l1o, t1l2o, v1l1o, v1l2o


def makeXTicks(a_list):
	# ret = []
	# for i in range(len(lista)):
	# 	if i % 2 == 0:
	# 		ret.append(lista[i])
	# return ret
	ret = []
	ret.append(a_list[0])
	ret.append(a_list[-1])
	length = len(a_list)
	
	middle = int(len(a_list) / 2)
	ret.append(a_list[middle])
	
	
	first_half = a_list[:len(a_list)//2]
	second_half = a_list[len(a_list)//2:]

	tmp = int(len(first_half) / 2)
	ret.append(a_list[tmp])
	# tmp = int(len(second_half) / 4)
	# ret.append(a_list[tmp])

	ret.append(datetime.datetime(2021, 8, 9, 10, 15, 37))
	return ret


def drawPlot(master_title, index, batt_file, corr_file, dr_file, pot_file, temp_file, volt_file):
	index = "output/"+index
	b1l1o, b1l2o, c1l1o, c1l2o, d1l1o, d1l2o, p1l1o, p1l2o, t1l1o, t1l2o, v1l1o, v1l2o = mergeDates(batt_file, corr_file, dr_file, pot_file, temp_file, volt_file)

	# PLOT 1
	plt.rcParams["legend.loc"] = 'lower left' # positioning legend
	plt.rcParams["figure.figsize"] = (15,7) # plot size
	

	
	ax = plt.gca()

	
	fig = plt.figure()

	plt.plot(c1l1o, c1l2o, label="Current (A)", color="orange")
	plt.plot(t1l1o, t1l2o, label="Temperature (°C)", color="red")


	x_ticks = makeXTicks(b1l1o)
	plt.xticks(rotation=30)
	ax.set_xticks(x_ticks)       

	
	plt.legend()
	dtFmt = mdates.DateFormatter("%H:%M") # define the formatting
	plt.gca().xaxis.set_major_formatter(dtFmt) 
	
	#plt.show()	
	plt.title(master_title + " (Current and Temperature)", fontsize=14, color="red")
	plt.tight_layout()
	plot_name = index +'_curr+temp.png'
	fig.savefig(plot_name, dpi=300)


	# PLOT 2
	plt.rcParams["legend.loc"] = 'lower left' # positioning legend
	plt.rcParams["figure.figsize"] = (15,7) # plot size
	
	
	ax = plt.gca()
	
	fig = plt.figure()

	plt.plot(b1l1o, b1l2o, label="Battery (%)", color="blue")
	plt.plot(d1l1o, d1l2o, label="Remaining distance (Km)", color="green")
	plt.plot(v1l1o, v1l2o, label="Voltage (V)", color="purple")


	x_ticks = makeXTicks(b1l1o)
	plt.xticks(rotation=30)
	ax.set_xticks(x_ticks)       

	plt.legend()
	dtFmt = mdates.DateFormatter("%H:%M") # define the formatting
	plt.gca().xaxis.set_major_formatter(dtFmt) 

	#plt.show()	
	plt.title(master_title + " (Battery, Remaining distance and Voltage)", fontsize=14, color="red")
	plt.tight_layout()
	plot_name = index + '_batt+dist+volt.png'
	fig.savefig(plot_name, dpi=300)



	# PLOT 3
	plt.rcParams["legend.loc"] = 'lower left' # positioning legend
	plt.rcParams["figure.figsize"] = (15,7) # plot size
	
	
	ax = plt.gca()
	

	fig = plt.figure()

	plt.plot(p1l1o, p1l2o, label="Power (W)")


	x_ticks = makeXTicks(b1l1o)
	plt.xticks(rotation=30)
	ax.set_xticks(x_ticks)       

	plt.legend()
	dtFmt = mdates.DateFormatter("%H:%M") # define the formatting
	plt.gca().xaxis.set_major_formatter(dtFmt) 

	#plt.show()	
	plt.title(master_title + " (Power)", fontsize=14, color="red")
	plt.tight_layout()
	
	plot_name = index + '_power.png'
	fig.savefig(plot_name, dpi=300)


def main():
	# Electric Scooter è Wheelchair
	batt1 = "/Users/lucasmac/Downloads/draw/data/2_carrozzina/Batteria (1 ora).csv"
	corr1 = "/Users/lucasmac/Downloads/draw/data/2_carrozzina/Corrente (1 ora).csv"
	dr1 = "/Users/lucasmac/Downloads/draw/data/2_carrozzina/Distanza Rimanente (1 ora).csv"
	pot1 = "/Users/lucasmac/Downloads/draw/data/2_carrozzina/Potenza (1 ora).csv"
	temp1 = "/Users/lucasmac/Downloads/draw/data/2_carrozzina/Temperatura (1 ora).csv"
	volt1 = "/Users/lucasmac/Downloads/draw/data/2_carrozzina/Voltaggio (1 ora).csv"
	master_title = "Electric Scooter + Wheelchair"
	index = "1"
	drawPlot(master_title, index, batt1, corr1, dr1, pot1, temp1, volt1)


	# Only Electric Scooter
	batt1 = "/Users/lucasmac/Downloads/draw/data/only_scooter/Batteria (1 ora).csv"
	corr1 = "/Users/lucasmac/Downloads/draw/data/only_scooter/Corrente (1 ora).csv"
	dr1 = "/Users/lucasmac/Downloads/draw/data/only_scooter/Distanza Rimanente (1 ora).csv"
	pot1 = "/Users/lucasmac/Downloads/draw/data/only_scooter/Potenza (1 ora).csv"
	temp1 = "/Users/lucasmac/Downloads/draw/data/only_scooter/Temperatura (1 ora).csv"
	volt1 = "/Users/lucasmac/Downloads/draw/data/only_scooter/Voltaggio (1 ora).csv"
	master_title = "Electric Scooter Stock Firmware"
	index = "2"
	drawPlot(master_title, index, batt1, corr1, dr1, pot1, temp1, volt1)

	#print(b1l2)

if __name__ == '__main__':
	main()



# # make up some data
# # Datetime list
# x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]

# y = [i+random.gauss(0,1) for i,_ in enumerate(x)]

# # plot
# plt.plot(x,y)
# # beautify the x-labels
# plt.gcf().autofmt_xdate()

# plt.show()