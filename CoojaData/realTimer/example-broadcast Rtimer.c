
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

#define MAX_SIZE_MESSAGE 255
#define PERIOD RTIMER_SECOND

/*---------------------------------------------------------------------------*/
PROCESS(radiosky_process, "Broadcast example");
AUTOSTART_PROCESSES(&radiosky_process);
/*---------------------------------------------------------------------------*/

static void
broadcast_recv_char(struct broadcast_conn *c, const linkaddr_t *from)
{
  leds_toggle(LEDS_RED);
  printf("Broadcast message received from %d.%d", from->u8[0], from->u8[1]);
  printf(" : %s\n",(char *)packetbuf_dataptr());
}

static const struct broadcast_callbacks broadcast_call = {broadcast_recv_char};
static struct broadcast_conn broadcast;

static char message[MAX_SIZE_MESSAGE];

static void
broadcast_rtimer(struct rtimer *t, void * ptr)
{
	sprintf(message, "I am node %d", node_id);
	packetbuf_copyfrom(message, 15);

	if ( node_id == 1)
	{
		//printf("Calling\n");
		leds_toggle(LEDS_BLUE);
		broadcast_send(&broadcast);
		leds_toggle(LEDS_GREEN);
		printf("Broadcast message sent / %d\n", PERIOD);
	}

	rtimer_set(t, RTIMER_TIME(t) + PERIOD, 1, broadcast_rtimer, ptr);
}

/*---------------------------------------------------------------------------*/
PROCESS_THREAD(radiosky_process, ev, data)
{
  	static struct rtimer t;

  	PROCESS_EXITHANDLER(broadcast_close(&broadcast);)

 	PROCESS_BEGIN();

	broadcast_open(&broadcast, 129, &broadcast_call);

	if( node_id == 1 )
	{
		rtimer_set(&t, RTIMER_NOW() + PERIOD, 1, broadcast_rtimer, NULL);
	}

  	while(1)
	{
		PROCESS_YIELD();
  	}

  	PROCESS_END();
}
/*---------------------------------------------------------------------------*/
