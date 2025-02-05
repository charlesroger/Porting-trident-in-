import math

f_CReceiver = open("/home/charles/Desktop/CoojaData/Ctimer/ProperDataReceiver.txt", "r")
f_CSender = open("/home/charles/Desktop/CoojaData/Ctimer/ProperDataSender.txt")
f_EReceiver = open ("/home/charles/Desktop/CoojaData/Etimer/ProperDataReceiver.txt")
f_ESender = open ("/home/charles/Desktop/CoojaData/Etimer/ProperDataSender.txt")
f_RReceiver = open ("/home/charles/Desktop/CoojaData/realTimer/ProperDataReceiver.txt")
f_RSender = open ("/home/charles/Desktop/CoojaData/realTimer/ProperDataSender.txt")


f_Average = open("/home/charles/Desktop/CoojaData/Average.txt", "w")
counter = 0
data = 0
t_max = 0
t_min = 10000

average_CReceiver = 0
average_CSender = 0
average_EReceiver = 0
average_ESender = 0
average_RReceiver = 0
average_RSender = 0
standardDeviationCtimerReceiver = 0
standardDeviationEtimerReceiver = 0
standardDeviationRtimerReceiver = 0
standardDeviationCtimerSender = 0
standardDeviationEtimerSender = 0
standardDeviationRtimerSender = 0


for ligne in f_CReceiver:
	line = ligne.split(" ")
	data = int(line[4])
	average_CReceiver = average_CReceiver + data
	counter = counter + 1
	if t_max < data:
		t_max = data
	if t_min > data:
		t_min = data 

average_CReceiver = average_CReceiver/counter
counter = 0

f_CReceiver.seek(0)
for ligne in f_CReceiver:
	line = ligne.split(" ")
	data = int(line[4])
	standardDeviationCtimerReceiver = standardDeviationCtimerReceiver + math.pow((data-average_CReceiver),2)
	counter = counter + 1
standardDeviationCtimerReceiver = standardDeviationCtimerReceiver/counter
standardDeviationCtimerReceiver = math.sqrt(standardDeviationCtimerReceiver)
counter = 0
f_Average.write("/***********Ctimer****************/" + "\n")
f_Average.write("->	Receiving" + "\n")
f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average_CReceiver)+ " Standard deviation = "+str(standardDeviationCtimerReceiver)+ "\n")
print(" SD = %d",standardDeviationCtimerReceiver)


for ligne in f_CSender:
	line = ligne.split(" ")
	data = int(line[4])
	average_CSender = average_CSender + data
	counter = counter + 1
	if t_max < data:
		t_max = data
	if t_min > data:
		t_min = data 

average_CSender = average_CSender/counter

counter = 0
f_CSender.seek(0)
standardDeviationCtimerSender = 0
for ligne in f_CSender:
	line = ligne.split(" ")
	data = int(line[4])
	standardDeviationCtimerSender = standardDeviationCtimerSender + math.pow(( data-average_CSender ),2)
	counter = counter + 1
standardDeviationCtimerSender = standardDeviationCtimerSender/counter 
standardDeviationCtimerReceiver = math.sqrt(standardDeviationCtimerReceiver)
counter = 0

f_Average.write("->	Sending" + "\n")
f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average_CSender)+ " Standard deviation = " + str(standardDeviationCtimerSender)+ "\n")




for ligne in f_EReceiver:
	line = ligne.split(" ")
	data = int(line[4])
	average_EReceiver = average_EReceiver + data
	counter = counter + 1
	if t_max < data:
		t_max = data
	if t_min > data:
		t_min = data 

average_EReceiver = average_EReceiver/counter
counter = 0
f_EReceiver.seek(0)

for ligne in f_EReceiver:
	line = ligne.split(" ")
	data = int(line[4])
	standardDeviationEtimerReceiver = standardDeviationEtimerReceiver + math.pow((data-average_EReceiver),2)
	counter = counter + 1
standardDeviationEtimerReceiver = standardDeviationEtimerReceiver/counter
standardDeviationEtimerReceiver = math.sqrt(standardDeviationEtimerReceiver)
counter = 0 

f_Average.write("/***********Etimer****************/" + "\n")
f_Average.write("->	Receiving" + "\n")
f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average_EReceiver)+ " Standard deviation = "+str(standardDeviationEtimerReceiver)+ "\n")

for ligne in f_ESender:
	line = ligne.split(" ")
	data = int(line[4])
	print(line)
	print(ligne)
	average_ESender = average_ESender + data
	counter = counter + 1
	if t_max < data:
		t_max = data
	if t_min > data:
		t_min = data 
average_ESender = average_ESender/counter
counter = 0
f_ESender.seek(0)


for ligne in f_ESender:
	line = ligne.split(" ")
	data = int(line[4])
	standardDeviationEtimerSender = standardDeviationEtimerSender + math.pow(( data-average_ESender ),2)
	counter = counter + 1
standardDeviationEtimerSender = standardDeviationEtimerSender/counter
standardDeviationEtimerSender = math.sqrt(standardDeviationEtimerSender)
counter = 0 

f_Average.write("->	Sending" + "\n")
f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average_ESender)+ " Standard deviation = "+str(standardDeviationEtimerSender)+ "\n")

for ligne in f_RReceiver:
	line = ligne.split(" ")
	data = int(line[4])
	average_RReceiver = average_RReceiver + data
	counter = counter + 1
	if t_max < data:
		t_max = data
	if t_min > data:
		t_min = data 

average_RReceiver = average_RReceiver/counter
counter = 0
f_RReceiver.seek(0)

for ligne in f_RReceiver:
	line = ligne.split(" ")
	data = int(line[4])
	standardDeviationRtimerReceiver = standardDeviationRtimerReceiver + math.pow((data-average_RReceiver),2)
	counter = counter + 1
standardDeviationRtimerReceiver = standardDeviationRtimerReceiver/counter 
standardDeviationRtimerReceiver = math.sqrt(standardDeviationRtimerReceiver)
counter = 0

f_Average.write("/***********Rtimer****************/" + "\n")
f_Average.write("->	Receiving" + "\n")
f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average_RReceiver)+ " Standard deviation = "+str(standardDeviationRtimerReceiver)+ "\n")

for ligne in f_RSender:
	line = ligne.split(" ")
	data = int(line[4])
	average_RSender = average_RSender + data
	counter = counter + 1
	if t_max < data:
		t_max = data
	if t_min > data:
		t_min = data 

average_RSender = average_RSender/counter
counter = 0
f_RSender.seek(0)

for ligne in f_RSender:
	line = ligne.split(" ")
	data = int(line[4])
	standardDeviationRtimerSender = standardDeviationRtimerSender + math.pow(( data-average_RSender ),2)
	counter = counter + 1
standardDeviationRtimerSender = standardDeviationRtimerSender/counter
standardDeviationRtimerSender = math.sqrt(standardDeviationRtimerSender)
counter = 0 

f_Average.write("->	Sending"+ "\n")
f_Average.write(" Time max = " +str(t_max)+ " Time min = " +str(t_min)+ " Time average = " +str(average_RSender)+ " Standard deviation = "+str(standardDeviationRtimerSender)+ "\n")


print("Conversion succesfull")

f_CReceiver.close()
f_CSender.close()
f_EReceiver.close()
f_ESender.close()
f_RReceiver.close()
f_RSender.close()
f_Average.close()


