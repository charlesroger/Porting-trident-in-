/*

->logRecordstats : 1
->logRecordRx : 2 
->logRecordRxError : 3
->logRecordTx : 4
->logRecordTxError : 5
->logRecordNewExp : 6
->RoundStartMsg : 7
->ExpDescriptor : 8

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

#define FOPEN(fd,file,action)    \
			 fd = cfs_open(file,action); \
			 if(fd < 0)								 \
			   printf("erreur\n");

#define MAX_FLASH_SIZE 1048576     //the flash is 1024kB

static ExpDescriptor* exp_descriptor;
static int expDescOffset = 0;
static int fd_read, fd_write;
static int * exp_Desc_Offset = &expDescOffset;

static uint16_t next_round_seqn;

static int flashUse;
static int writedBytes;
static int counter = 0;
static int logWrite(const uint8_t * const record, int length, int * offset)
{
	if(counter == 0)
	{
		FOPEN(fd_write,"write.txt", CFS_WRITE);
		counter = 1;
		printf("we wrote a expdescriptor\n");
		ExpDescriptor* test = (ExpDescriptor*)record;
		printf("run_id = %d\n",test->run_id);
		printf("run_id = %d\n",test->num_rounds);
	}
	else
	{
		FOPEN(fd_write,"write.txt", CFS_WRITE | CFS_APPEND);
		printf("we wrote a roundstartmsg\n");
		RoundStartMsg* test2 = (RoundStartMsg*)record;
		printf("run_id = %d\n",test2->run_id);
	}
	printf("currentOffset = %d\n",*offset);
	*offset = flashUse;
	if((flashUse + length) > MAX_FLASH_SIZE)
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


static void UpdateData(void * ptr, int identificator)
{
	if(identificator == 8)	//we read the experiment descriptor
	{
		if(exp_descriptor->password == EXP_DESCRIPTOR_PASSWORD)
		{
			next_round_seqn = 0;
			if((exp_descriptor->run_id & 0xFF) != 0xFF)
			{
				exp_descriptor->run_id ++;
				logWrite((uint8_t*)&exp_descriptor, sizeof(ExpDescriptor),exp_Desc_Offset);
				exp_descriptor->run_id -= 1;
			}
		}
	}
	if(identificator == 7)	//we read a new round
	{
		RoundStartMsg* startmsg = (RoundStartMsg*)ptr;
		startmsg->round_seqn = next_round_seqn;
		startmsg->config_id = exp_descriptor->config_id;
		next_round_seqn ++;
	}

}

/*static void readtest() //take attention to test this function you need to add the file in cooja
{
	int fd;
	char testc;
	FOPEN(fd,"toto.txt", CFS_READ);
	cfs_read(fd,&testc,sizeof(char));
	printf("caractere = %c\n",testc);
}*/



static void ConfigRead(int offset, void* msg,int identificator)
{
	printf("we are in configRead\n");
	printf("identificator = %d\n",identificator);
	fd_read = cfs_open("write.txt", CFS_READ);
	printf("fd_read = %d\n",fd_read);
	if(fd_read < 0)
	{
		printf("error\n");
	}
	printf("we open the file\n");
	cfs_seek(fd_read, (cfs_offset_t)offset, CFS_SEEK_SET);
	if(identificator == 7)
	{
		printf("we try to read a RoundStartMsg\n");
		RoundStartMsg* rostartMsg = (RoundStartMsg*)msg;
		cfs_read(fd_read, rostartMsg, sizeof(RoundStartMsg));
		UpdateData((void*)rostartMsg,identificator);
		msg = (void*)rostartMsg;
	}
	if(identificator == 8)
	{
		printf("we try to read a ExpDescriptor\n");
		ExpDescriptor* expMsg = (ExpDescriptor*)msg;
		cfs_read(fd_read, expMsg, sizeof(ExpDescriptor));
		UpdateData((void*)&expMsg,identificator);
		msg = (void*)expMsg;
	}
	cfs_close(fd_read);
}

static void prepareNewRun()
{
	printf("we will prepare a new run\n");
	exp_descriptor->password = 0;
	ConfigRead(0,(void*)&exp_descriptor,8);
	printf("we have prepared a new run\n");
}

static void getNextTest(RoundStartMsg* startmsg)
{
	printf("we will gegt a new test\n");
	if(next_round_seqn < exp_descriptor->num_rounds*exp_descriptor->repetitions)
	{
		ConfigRead(sizeof(ExpDescriptor)+next_round_seqn*sizeof(RoundStartMsg),(void*)&startmsg,7);
	}
	printf("we getted a new test\n");
}

static void fillData()
{
	printf("we fill the data\n");
	int offsetTest = 0;
	int * returnOffsetTest = &offsetTest;
	int *roundOffset = NULL; // we never look at this offset
	int i = 0;
	RoundStartMsg  RoundTest;
	RoundTest.run_id = 0;
	ExpDescriptor expTest;
	expTest.num_rounds = 4;
	expTest.password = EXP_DESCRIPTOR_PASSWORD;
	logWrite((uint8_t*)&expTest, sizeof(ExpDescriptor*),returnOffsetTest);

	for(i = 0;i<4;i++)
	{
		logWrite((uint8_t*)&RoundTest, sizeof(RoundStartMsg*),roundOffset);
		RoundTest.run_id += 1;
	}
	printf("we have filled the data\n");
	counter = 0;
}
/*---------------------------------------------------------------------------*/
PROCESS(flashTest_process, "Flash test");
AUTOSTART_PROCESSES(&flashTest_process);
/*---------------------------------------------------------------------------*/

PROCESS_THREAD(flashTest_process, ev, data)
{
	PROCESS_BEGIN();
	printf("we are in the process\n");
	fillData();
	prepareNewRun();
	//readtest();
  PROCESS_END();
}

