import math
import os
import matplotlib.pyplot as plt
import numpy as np

delay = []
seed = []
node = []
pdr = []

def plotFunction(f_in,seedNum, nodeNum): 
  f_inD = open(f_in,"r")
  for ligne in f_inD  :
    data = ligne.find('Average Delay')
    pdrdata = ligne.find('Average PDR')
    line = ligne.split(" ")
    if data != -1 :
      #print("toto:"+line[3])
      delay.append((float(line[3])*1000.0)+float(line[5]))
      seed.append(float(seedNum))
      node.append(float(nodeNum))
    if pdrdata != -1 :
      pdr.append(float(line[3]))
  f_inD.close()

def Comput_data(f_in,f_out, Simulation,node):
	
	f_inD = open(f_in,"r")
        f_outD = open(f_out,"a")
	maxNode = node
	offset = 0
	refMinute = 0
	refSecond = 0
	refMs = 0
	minute = 0
	seconde = 0
	ms = 0
	DelayMinute = 0
	DelaySeconde = 0
	DelayMs = 0

	previousId = 0

	errorCounter = 0
	countertest = 0
	Average = float(DelayMs)
        AverageSecond = float(DelaySeconde)
        AverageTab = []
        AverageSecTab = []
        AveragePDR = []
	PDR = 0
        countMaster = 0
        averageSimulation = 0
	averageSimulationSec = 0
	PDRAverage = 0
	Roundnumber = 0



	f_outD.write("/*****************" +Simulation+"********************/\n\n")
      
	for ligne in f_inD  :
	  Notification = ligne.find('Notification from node')
	  Master = ligne.find('Master initiated')

          if Master != -1 :
             countMaster += 1
             if countMaster > 1 :
               if previousId != maxNode :
                 errorCounter += int(maxNode) - int(previousId) 
	       PDR = (float(maxNode - errorCounter)/float(maxNode))*100
               AveragePDR.append(PDR)
               
               Average = float(Average)/float(maxNode - errorCounter)
               print(AverageSecond)
               AverageSecond = float(AverageSecond/(maxNode - errorCounter))
	       print (AverageSecond)

	       AverageSecTab.append(AverageSecond)
	       AverageTab.append(Average)
               f_outD.write("\nThe average delay is "+str(AverageSecond)+" seconde "+ str(Average) +" ms\n")
	       f_outD.write("\nThe PDR is : " +str(PDR)+ "\n")
	       f_outD.write("\nwe miss " +str(errorCounter)+" node \n")
	       f_outD.write("\n")


             f_outD.write("\nNew round\n")
             Roundnumber += 1
             errorCounter = 0
             previousId = 0
	     AverageSecond = 0
	     line = ligne.split(":")
	     refMinute = line[0]
             refSecond = line[1][0:2]
	     refMs = line[1][3:6]
             #print ("reference = "+str(refMinute) +":"+str (refSecond)+":"+str(refMs) )

	  if Notification != -1 :
	     lineId = ligne.split("\t")
	     Id = lineId[1][3:6]
             line = ligne.split(":")
	     minute = line[0]
	     seconde = line[1][0:2]
	     ms = line[1][3:6]
             #print ("Data  = "+str(minute) +":"+str (seconde)+":"+str(ms) )
	     DelayMinute = int(minute) - int(refMinute)
	     DelaySeconde = int(seconde) - int(refSecond) - int(Id)
             #print(DelaySeconde)
             AverageSecond += float(DelaySeconde) 
             if DelaySeconde < 0 :
               DelaySeconde = 0
	     DelayMs = int(ms) - int(refMs)
             if DelaySeconde > 0 :
               DelayMs = (1000 * int(seconde)) + int(ms)
               DelayMs = (int(DelaySeconde) - (1000 * int(refSecond) + int(refMs)))%1000
	     Average += DelayMs
	     f_outD.write("The delay is  \t" + str(DelayMinute) + " minutes\t" + str(int(DelaySeconde))+ " seconde\t" +str(DelayMs)+ " ms\n")

              
	     if Id != str(int(previousId)+1) : 
	       errorCounter += (int(Id) - int(previousId)-1)
               offset = Id
             previousId = Id

        for item in AverageTab :
          averageSimulation += float(item)
        averageSimulation = averageSimulation / float(Roundnumber)
	
	for item in AverageSecTab :
          averageSimulationSec += float(item)
        averageSimulationSec = averageSimulationSec / float(Roundnumber)

	for item in AveragePDR :
	  PDRAverage += float(item)
        PDRAverage = PDRAverage / float(Roundnumber)


        f_outD.write("\n/////////////////////////Average of the simulation////////////////////////\n")
        f_outD.write("Average Delay = "+str(averageSimulationSec)+" seconde "+str(averageSimulation)+" ms"+"\n")
        f_outD.write("Average PDR = " + str(PDRAverage) + "\n" )
	f_inD.close()
	f_outD.close()

if __name__ == "__main__":

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed3node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed3node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed3node49.txt")  

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed4node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed4node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed4node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed5node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed5node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed5node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed6node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed6node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed6node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed7node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed7node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed7node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed8node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed8node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed8node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed9node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed9node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed9node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed10node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed10node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed10node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed12node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed12node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed12node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed15node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed15node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed15node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed17node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed17node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed17node49.txt")

  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed20node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed20node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/grid/resultsseed20node49.txt")

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed3node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed3node10.txt", "seed3node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed3node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed3node30.txt", "seed3node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed3node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed3node49.txt", "seed3node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed4node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed4node10.txt", "seed4node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed4node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed4node30.txt", "seed4node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed4node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed4node49.txt", "seed4node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed5node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed5node10.txt", "seed5node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed5node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed5node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed5node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed5node49.txt", "seed5node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed6node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed6node10.txt", "seed6node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed6node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed6node30.txt", "seed6node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed6node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed6node49.txt", "seed6node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed7node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed7node10.txt", "seed7node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed7node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed7node30.txt", "seed7node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed7node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed7node49.txt", "seed7node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed8node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed8node10.txt", "seed8node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed8node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed8node30.txt", "seed8node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed8node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed8node49.txt", "seed8node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed9node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed9node10.txt", "seed9node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed5node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed9node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed5node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed9node49.txt", "seed5node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed10node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed10node10.txt", "seed10node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed10node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed10node30.txt", "seed10node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed10node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed10node49.txt", "seed10node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed12node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed12node10.txt", "seed12node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed12node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed12node30.txt", "seed12node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed12node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed12node49.txt", "seed12node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed15node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed15node10.txt", "seed5node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed15node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed15node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed15node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed15node49.txt", "seed15node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed17node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed17node10.txt", "seed5node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed17node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed17node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed17node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed17node49.txt", "seed17node49",49)

  Comput_data("/home/charles/Desktop/synctopotests/grid/seed20node10.txt","/home/charles/Desktop/synctopotests/grid/resultsseed20node10.txt", "seed20node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed20node30.txt","/home/charles/Desktop/synctopotests/grid/resultsseed20node30.txt", "seed20node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/grid/seed20node49.txt","/home/charles/Desktop/synctopotests/grid/resultsseed20node49.txt", "seed20node49",49)

  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed3node10.txt",3, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed4node10.txt",4, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed5node10.txt",5, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed6node10.txt",6, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed7node10.txt",7, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed8node10.txt",8, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed9node10.txt",9, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed10node10.txt",10, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed12node10.txt",12, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed15node10.txt",15, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed17node10.txt",17, 10)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed20node10.txt",20, 10)
  plt.figure(1)
  plt.plot(seed,pdr,'v',markersize = 15)
  plt.plot(seed,delay,'o',markersize = 15)
  plt.tick_params(axis='x', labelsize=15)
  plt.tick_params(axis='y', labelsize=15)
  plt.ylabel('PDR(b) , delay(r)',fontsize=15)
  plt.xlabel('Seed',fontsize=15)
  plt.title('Impact of Seed on PDR and delay for grid topology (n =10)',fontsize=20)
  plt.savefig('SeedInfluence_10nodes.png')
  del delay[:]
  del seed[:]
  del node[:]
  del pdr[:]
  
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed3node30.txt",3, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed4node30.txt",4, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed5node30.txt",5, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed6node30.txt",6, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed7node30.txt",7, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed8node30.txt",8, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed9node30.txt",9, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed10node30.txt",10, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed12node30.txt",12, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed15node30.txt",15, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed17node30.txt",17, 30)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed20node30.txt",20, 30)
  plt.figure(2)
  plt.plot(seed,pdr,'v',markersize = 15)
  plt.plot(seed,delay,'o',markersize = 15)
  plt.tick_params(axis='x', labelsize=15)
  plt.tick_params(axis='y', labelsize=15)
  plt.ylabel('PDR(b) , delay(r)',fontsize=15)
  plt.xlabel('Seed',fontsize=15)
  plt.title('Impact of Seed on PDR and delayfor grid topology (n =30)',fontsize=20)
  plt.savefig('SeedInfluence_30nodes.png')
  del delay[:]
  del seed[:]
  del node[:]
  del pdr[:]


  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed3node49.txt",3, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed4node49.txt",4, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed5node49.txt",5, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed6node49.txt",6, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed7node49.txt",7, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed8node49.txt",8, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed9node49.txt",9, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed10node49.txt",10, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed12node49.txt",12, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed15node49.txt",15, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed17node49.txt",17, 49)
  plotFunction("/home/charles/Desktop/synctopotests/grid/resultsseed20node49.txt",20, 49)
  plt.figure(3)
  plt.plot(seed,pdr,'v',markersize = 15)
  plt.plot(seed,delay,'o',markersize = 15)
  plt.tick_params(axis='x', labelsize=15)
  plt.tick_params(axis='y', labelsize=15)
  plt.ylabel('PDR(b) , delay(r)',fontsize=15)
  plt.xlabel('Seed',fontsize=15)
  plt.title('Impact of Seed on PDR and delay for grid topology (n = 49)',fontsize=20)
  plt.savefig('SeedInfluence_49nodes.png')
  plt.show()
  del delay[:]
  del seed[:]
  del node[:]
  del pdr[:]
