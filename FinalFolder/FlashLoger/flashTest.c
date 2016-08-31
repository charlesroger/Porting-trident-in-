
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


//typedef struct test {
//	int identificator;
//} test;


static int test;
static int readtest;
static int offsetTest = 0;
static int * currentOffset = &offsetTest;
static int flashUse;
static int fd_write,fd_read;
static Datastruct dataTab[10];
static Datastruct readDataTab[10];
static int i = 0;
static int writedBytes;


static int logWrite(const uint8_t * const record, int length, int * offset)
{
	fd_write = cfs_open("write.txt", CFS_WRITE | CFS_APPEND);
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
static void fillData()
{
	for(i = 0; i < 10 ; i++)
	{
		dataTab[i].number = i;
		dataTab[i].id = node_id;
		dataTab[i].identificator = 1;
		printf("initial number = %d\n",dataTab[i].number);
		printf("initial id = %d\n",dataTab[i].id);
	}
}



/*static void readData()
{
	printf("offset = %d\n",*currentOffset);
	fd_read = cfs_open("write.txt", CFS_READ);

	cfs_seek(fd_read, (cfs_offset_t)*currentOffset, CFS_SEEK_SET);
	readtest = cfs_read(fd_read, &test, sizeof(test));

	if(readtest == sizeof(dataTab))
	{
	printf("reading ended with the correct number of bytes\n");
	}

	printf("identificator = %d\n",test.identificator);

	cfs_close(fd_write);
}*/





static void readData()
{
	printf("offset = %d\n",*currentOffset);
	fd_read = cfs_open("write.txt", CFS_READ);

	cfs_seek(fd_read, (cfs_offset_t)*currentOffset, CFS_SEEK_SET);
	readtest = cfs_read(fd_read, readDataTab, sizeof(dataTab));

	if(readtest == sizeof(dataTab))
	{
	printf("reading ended with the correct number of bytes\n");
	}

	for(i = 0 ; i < 10 ; i++)
	{
		printf("readed number = %d\n",readDataTab[i].number);
		printf("readed id = %d\n",readDataTab[i].id);
	}
	cfs_close(fd_write);
}

/*---------------------------------------------------------------------------*/
PROCESS(flashTest_process, "Flash test");
AUTOSTART_PROCESSES(&flashTest_process);
/*---------------------------------------------------------------------------*/

PROCESS_THREAD(flashTest_process, ev, data)
{
	PROCESS_BEGIN();
	printf("process begin\n");
	fillData();
	printf("fill data ended\n");
	test = logWrite((uint8_t*)&dataTab, sizeof(dataTab),currentOffset);	
	printf("logWrite ended\n");
	printf("current offset : %d\n",*currentOffset);
	printf("we try to write :  %d\n",sizeof(dataTab));
	readData();
  cfs_close(fd_write);
  PROCESS_END();
}

