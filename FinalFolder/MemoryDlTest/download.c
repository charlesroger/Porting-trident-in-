/*During the execution of trident we store 8 differente structure, in order to identify all the structure we use a label in the memory we store the label before all storing in the flash
->logRecordstats : 1
->logRecordRx : 2 
->logRecordRxError : 3
->logRecordTx : 4
->logRecordTxError : 5
->logRecordNewExp : 6
->RoundStartMsg : 7
->ExpDescriptor : 8

What remains to be done : 
->The sending to the gateway unicast. I recommend to use a broadcast communication with an identifier
->Some debug
*/ 


#include "contiki.h"
#include "dev/leds.h"
#include "dev/button-sensor.h"
#include "dev/light-sensor.h"
#include "dev/sht11/sht11-sensor.h"
#include "net/rime/rime.h"
#include "node-id.h"
#include "sys/rtimer.h"
#include "random.h"
#include <stdio.h>
#include "sync.h"
#include "cfs-coffee.h"
#include "cfs.h"
#include "contiki-conf.h"

#define MAX_FLASH_SIZE 1048576     //the flash is 1024kB
#define SAMPLE_NUMBER 10

static int offsetTest = 0;
static int * currentOffset = &offsetTest;
static int flashUse;
static int fd_write,fd_read;
static int writedBytes;
static uint8_t seqn = 255; //to start from 0

int i = 0;
int j = 0;
int k = 0;
int l = 0;
int m = 0;
int n = 0;

static uint8_t requester;
static uint32_t start_cookie;
static uint8_t data_size;

static uint16_t readedBytes = 0;

static int identificator = 0;
static int readIdentificator = 0; 

static LogDownlReq* r;

static LogRecordStats readStats;
static LogRecordRx readRxStats;
static LogRecordRxError readRxErrorStats;
static LogRecordNewExp readNewExp;
static LogRecordTx readTxStats;
static LogRecordTxError readRxErrorStats;

static LogRecordStatsDownload readStatsDl[SAMPLE_NUMBER];
static LogRecordRxDownload readRxStatsDl[SAMPLE_NUMBER];
static LogRecordRxErrorDownload readRxErrorStatsDl[SAMPLE_NUMBER];
static LogRecordNewExpDownload readNewExpDl[SAMPLE_NUMBER];
static LogRecordTxDownload readTxStatsDl[SAMPLE_NUMBER];
static LogRecordTxErrorDownload readRxErrorStatsDl[SAMPLE_NUMBER];

static int logWrite(const uint8_t * const record, int length, int * offset)
{
	fd_write = cfs_open("write.txt", CFS_WRITE | CFS_APPEND);
	printf("currentOffset = %d\n",*offset);
	*offset = flashUse;
	if((flashUse + length) > MAX_FLASH_SIZE) // we will exceeded the maximum size of the memory
	{
		return -1;
		printf("flash to small");
	}
	else
	{
		flashUse += length;
		writedBytes = cfs_write(fd_write, record, length);

    if(writedBytes == length)
    {
      printf("writing endend with the good number of bytes\n");
    }

		if(writedBytes != length)
		{
			printf("we dont wrote the entire data\n");
			return -1;			
		}

		cfs_close(fd_write);
		return fd_write;
	}
}
static void fillData()
{
  stats.record_type = 1;
  rxStats.record_type = 2;
  rxErrorStats.record_type = 3;
}

static void ReadMemory(uint8_t dataSise)
{
	fd_read = cfs_open("write.txt", CFS_READ);
  while(readedBytes < dataSize-8 ) //while there is still a data structure in the memory (8 because its the size of the smallest structure)
  {
    cfs_read(fd_read, &readIdentificator, sizeof(int));

    if(readIdentificator == 1)//we read logRecordstats
    {
      cfs_read(fd_read, &readStats, sizeof(LogRecordStats));
      readStatsDl[i].record_type = readStats.record_type;
      readStatsDl[i].record_seqn = seqn
      readStatsDl[i].volume_id = volume_id;
      readStatsDl[i].session_id = r->session_id;
      readStatsDl[i].avgTemperature = readStats.avgTemperature;
      readStatsDl[i].avgHumidity = readStats.avgHumidity;
      readStatsDl[i].initBattery = readStats.initBattery;
      readStatsDl[i].endBattery = readStats.endBattery;
      memcpy(&readStatsDl[i].rx_packets,&readStats.rx_packets,MAX_NR_NODES);
      memcpy(&readStatsDl[i].rx_rssi,&readStats.rx_rssi,MAX_NR_NODES);
      memcpy(&readStatsDl[i].rx_lqi,&readStats.rx_lqi,MAX_NR_NODES);
      memcpy(&readStatsDl[i].rx_noise,&readStats.rx_noise,MAX_NR_NODES);
      i += 1;
    }

    if(readIdentificator == 2)//we read logRecordRx  
    {
      cfs_read(fd_read, &readRxStats, sizeof(LogRecordRx));

      readRxStatsDl[i].record_type = readRxStats.record_type;
      readRxStats[i].record_seqn = seqn
      readRxStatsDl[i].volume_id = volume_id;
      readRxStatsDl[i].session_id = r->session_id;
      readRxStatsDl[i].node_id = readRxStats.node_id;
      readRxStatsDl[i].noise = readRxStats.noise;
      readRxStatsDl[i].msgseqn = readRxStats.msg_seqn;
     	readRxStatsDl[i].rssi = readRxStats.rssi;
			readRxStatsDl[i].lqi = readRxStats.lqi;

      j += 1;
    }

    if(readIdentificator == 3)//We read logRecordRxError 
    {
      cfs_read(fd_read, &readRxErrorStats, sizeof(LogRecordRxError));

      readRxErrorStatsDl[i].record_type = readRxErrorStats.record_type;
      readRxErrorStatsDl[i].record_seqn = seqn
      readRxErrorStatsDl[i].volume_id = volume_id;
      readRxErrorStatsDl[i].session_id = r->session_id;
      readRxErrorStatsDl[i].node_id = readRxErrorStats.node_id;
      readRxErrorStatsDl[i].msg_seqn = readRxErrorStats.msg_seqn;
      readRxErrorStatsDl[i].rssi = readRxErrorStats.rssi;
      readRxErrorStatsDl[i].lqi = readRxErrorStats.lqi;
			readRxErrorStatsDl[i].trident_status = readRxErrorStats.trident_status;
      
      k += 1;
    }

    if(readIdentificator == 4)//we read logRecordTx 
    {
      cfs_read(fd_read, &txStats, sizeof(LogRecordTx));

      readTxStatsDl[i].record_type = readTxStats.record_type;
      readTxStatsDl[i].record_seqn = seqn
      readTxStatsDl[i].volume_id = volume_id;
      readTxStatsDl[i].session_id = r->session_id;
      readTxStatsDl[i].node_id = readTxStats.node_id;
      readTxStatsDl[i].noise = readTxStats.noise;
      readTxStatsDl[i].msgseqn = readTxStats.msg_seqn;

      l += 1;
    }

    if(readIdentificator == 5)//we read logRecordTxError
    {
      cfs_read(fd_read, &readTxErrorStats, sizeof(LogRecordTxError));

      readTxErrorStatsDl[i].record_type = readTxErrorStats.record_type;
      readTxErrorStatsDl[i].record_seqn = seqn
      readTxErrorStatsDl[i].volume_id = volume_id;
      readTxErrorStatsDl[i].session_id = r->session_id;
      readTxErrorStatsDl[i].node_id = readTxErrorStats.node_id;
      readTxErrorStatsDl[i].noise = readTxErrorStats.noise;
      readTxErrorStatsDl[i].msgseqn = readTxErrorStats.msg_seqn;

      m +=1;
    }

    if(readIdentificator == 6)//we read logRecordNewExp
    {
      cfs_read(fd_read, &readNewExp, sizeof(LogRecordNewExp));

      readNewExpDl[i].record_type = readNewExp.record_type;
      readNewExpDl[i].record_seqn = seqn
      readNewExpDl[i].volume_id = volume_id;
      readNewExpDl[i].session_id = r->session_id;
			memcpy(&readNewExpDl[i].marker,&readNewExp.marker,8);
      readNewExpDl[i].config_id = readNewExp.config_id;
      readNewExpDl[i].run_id = readNewExp.run_id;
      readNewExpDl[i].round_seqn = readNewExp.round_seqn;
			readNewExpDl[i].round_node_id = readNewExp.node_id;

      n +=1;
    }
  }
    cfs_read(fd_read, &readStats, sizeof(LogRecordStats));    
    printf(" record type = %d\n",readStats.record_type);
    readedBytes += sizeof(LogRecordStats);

    cfs_read(fd_read, &readIdentificator, sizeof(int));
    printf("identificator equal %d its a LogRecordRx structure we have to read %d octets\n ",readIdentificator,sizeof(LogRecordRx));
    cfs_read(fd_read, &readRxStats, sizeof(LogRecordRx));
    printf(" record type = %d\n",readRxStats.record_type);
    readedBytes += sizeof(LogRecordRx);

    cfs_read(fd_read, &readIdentificator, sizeof(int));
    printf("identificator equal %d its a LogRecordRxError structure we have to read %d octets\n ",readIdentificator,sizeof(LogRecordRxError));
    cfs_read(fd_read, &readRxErrorStats, sizeof(LogRecordRxError));
    printf(" record type = %d\n",readRxErrorStats.record_type);
    readedBytes += sizeof(LogRecordRxError);
}

static void sendData()	//we send all the array in broadcast so we have to target the gateway id 1000
{
	//this function need to be finishe
	readStatsDl[SAMPLE_NUMBER];
	readRxStatsDl[SAMPLE_NUMBER];
	readRxErrorStatsDl[SAMPLE_NUMBER];
	readNewExpDl[SAMPLE_NUMBER];
	readTxStatsDl[SAMPLE_NUMBER];
	readRxErrorStatsDl[SAMPLE_NUMBER];








}
broadcast_recv(struct broadcast_conn *c, const linkaddr_t *from)
{
  r = packetbuf_dataptr(); 
  volume_id = r->volume_id;
  requester = from->u8[0];
  data_size = r->data_size;
  start_cookie = r->start_cookie;
}

static const struct broadcast_callbacks broadcast_call = {broadcast_recv};
static struct broadcast_conn broadcast;
/*---------------------------------------------------------------------------*/
PROCESS(flashTest_process, "Flash test");
AUTOSTART_PROCESSES(&flashTest_process);
/*---------------------------------------------------------------------------*/

PROCESS_THREAD(flashTest_process, ev, data)
{
  PROCESS_EXITHANDLER(broadcast_close(&broadcast);)
	PROCESS_BEGIN();

  broadcast_open(&broadcast, 129, &broadcast_call);

	printf("process begin\n");
	fillData();
  identificator = 1;
	logWrite((uint8_t*)&identificator, sizeof(int),currentOffset);
  logWrite((uint8_t*)&stats, sizeof(LogRecordStats),currentOffset);	
  identificator = 2;
	logWrite((uint8_t*)&identificator, sizeof(int),currentOffset);
  logWrite((uint8_t*)&rxStats, sizeof(LogRecordRx),currentOffset);	
	identificator = 3;
	logWrite((uint8_t*)&identificator, sizeof(int),currentOffset);
  logWrite((uint8_t*)&rxErrorStats, sizeof(LogRecordRxError),currentOffset);	
  ReadMemory();

  cfs_close(fd_write);
  PROCESS_END();
}

