f_in = open("/home/charles/Desktop/CoojaData/realTimer/TestTime", "r")
f_outSender = open("/home/charles/Desktop/CoojaData/realTimer/ProperDataSender.txt", "w")
f_outReceiver = open("/home/charles/Desktop/CoojaData/realTimer/ProperDataReceiver.txt", "w")
tabReceiver = []
tabSender = []
IdleLine = 0
tata = 0
transmitting = False
receiving = False
for ligne in f_in:
	testTransmitting = ligne.find('Radio transmitting')
	testReceiving = ligne.find('Radio receiving')
	if testTransmitting != -1 or transmitting == True:
		if transmitting == False :
			transmitting = True
			IdleLine = 0
	  		line = ligne.split("\t")
			IdleLine = line[1]
		elif transmitting == True:
			transmitting = False
			tata = 0
			line = ligne.split("\t")
			tata = line[1]
			tabSender.append(str(int(tata)-int(IdleLine)))
	elif testReceiving != -1 or receiving == True:
		if receiving == False :
			receiving = True
			IdleLine = 0
	  		line = ligne.split("\t")
			IdleLine = line[1]
		elif receiving == True:
			receiving = False
			tata = 0
			line = ligne.split("\t")
			tata = line[1]
			tabReceiver.append(str(int(tata)-int(IdleLine)))
for item in tabReceiver :
	#print(item)
	f_outReceiver.write("Time for receiving : " + item + "\n")
for item in tabSender :
	#print(item)
	f_outSender.write("Time for sending : " + item + "\n")

print("Conversion succesfull")

f_outReceiver.close()
f_outSender.close()
f_in.close()

