import math
import os
import matplotlib.pyplot as plt
import numpy as np
import csv
from pylab import *

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

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed3node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed3node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed3node50.txt")  

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed4node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed4node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed4node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed5node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed5node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed5node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed6node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed6node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed6node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed7node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed7node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed7node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed8node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed8node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed8node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed9node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed9node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed9node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed10node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed10node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed10node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed12node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed12node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed12node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed15node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed15node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed15node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed17node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed17node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed17node50.txt")

  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed20node10.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed20node30.txt")
  os.remove("/home/charles/Desktop/synctopotests/line/resultsseed20node50.txt")

  Comput_data("/home/charles/Desktop/synctopotests/line/seed3node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed3node10.txt", "seed3node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed3node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed3node30.txt", "seed3node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed3node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed3node50.txt", "seed3node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed4node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed4node10.txt", "seed4node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed4node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed4node30.txt", "seed4node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed4node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed4node50.txt", "seed4node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed5node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed5node10.txt", "seed5node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed5node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed5node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed5node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed5node50.txt", "seed5node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed6node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed6node10.txt", "seed6node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed6node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed6node30.txt", "seed6node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed6node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed6node50.txt", "seed6node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed7node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed7node10.txt", "seed7node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed7node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed7node30.txt", "seed7node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed7node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed7node50.txt", "seed7node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed8node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed8node10.txt", "seed8node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed8node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed8node30.txt", "seed8node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed8node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed8node50.txt", "seed8node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed9node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed9node10.txt", "seed9node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed5node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed9node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed5node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed9node50.txt", "seed5node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed10node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed10node10.txt", "seed10node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed10node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed10node30.txt", "seed10node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed10node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed10node50.txt", "seed10node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed12node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed12node10.txt", "seed12node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed12node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed12node30.txt", "seed12node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed12node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed12node50.txt", "seed12node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed15node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed15node10.txt", "seed5node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed15node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed15node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed15node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed15node50.txt", "seed15node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed17node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed17node10.txt", "seed5node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed17node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed17node30.txt", "seed5node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed17node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed17node50.txt", "seed17node50",50)

  Comput_data("/home/charles/Desktop/synctopotests/line/seed20node10.txt","/home/charles/Desktop/synctopotests/line/resultsseed20node10.txt", "seed20node10",10)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed20node30.txt","/home/charles/Desktop/synctopotests/line/resultsseed20node30.txt", "seed20node30",30)
  Comput_data("/home/charles/Desktop/synctopotests/line/seed20node50.txt","/home/charles/Desktop/synctopotests/line/resultsseed20node50.txt", "seed20node50",50)

  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed3node10.txt",3, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed4node10.txt",4, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed5node10.txt",5, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed6node10.txt",6, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed7node10.txt",7, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed8node10.txt",8, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed9node10.txt",9, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed10node10.txt",10, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed12node10.txt",12, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed15node10.txt",15, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed17node10.txt",17, 10)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed20node10.txt",20, 10)
  plt.figure(1)
  plt.plot(seed,pdr,'v',markersize = 15)
  plt.plot(seed,delay,'o',markersize = 15)
  plt.tick_params(axis='x', labelsize=15)
  plt.tick_params(axis='y', labelsize=15)
  plt.ylabel('PDR(b) , delay(r)')
  plt.xlabel('Seed')
  plt.title('Impact of Seed on PDR and delay for line topology (n =10)',fontsize=20)
  plt.savefig('SeedInfluence_10nodes.png')
  del delay[:]
  del seed[:]
  del node[:]
  del pdr[:]
  
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed3node30.txt",3, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed4node30.txt",4, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed5node30.txt",5, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed6node30.txt",6, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed7node30.txt",7, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed8node30.txt",8, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed9node30.txt",9, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed10node30.txt",10, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed12node30.txt",12, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed15node30.txt",15, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed17node30.txt",17, 30)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed20node30.txt",20, 30)
  plt.figure(2)
  plt.plot(seed,pdr,'v',markersize = 15)
  plt.plot(seed,delay,'o',markersize = 15)
  plt.tick_params(axis='x', labelsize=15)
  plt.tick_params(axis='y', labelsize=15)
  plt.ylabel('PDR(b) , delay(r)')
  plt.xlabel('Seed')
  plt.title('Impact of Seed on PDR and delayfor line topology (n =30)',fontsize=20)
  plt.savefig('SeedInfluence_30nodes.png')
  del delay[:]
  del seed[:]
  del node[:]
  del pdr[:]


  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed3node50.txt",3, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed4node50.txt",4, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed5node50.txt",5, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed6node50.txt",6, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed7node50.txt",7, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed8node50.txt",8, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed9node50.txt",9, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed10node50.txt",10, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed12node50.txt",12, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed15node50.txt",15, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed17node50.txt",17, 50)
  plotFunction("/home/charles/Desktop/synctopotests/line/resultsseed20node50.txt",20, 50)
  plt.figure(3)
  plt.plot(seed,pdr,'v',markersize = 15)
  plt.plot(seed,delay,'o',markersize = 15)
  plt.tick_params(axis='x', labelsize=15)
  plt.tick_params(axis='y', labelsize=15)
  plt.ylabel('PDR(b) , delay(r)')
  plt.xlabel('Seed')
  plt.title('Impact of Seed on PDR and delay for line topology (n = 50)',fontsize=20)
  plt.savefig('SeedInfluence_50nodes.png')
  plt.show()
  del delay[:]
  del seed[:]
  del node[:]
  del pdr[:]
