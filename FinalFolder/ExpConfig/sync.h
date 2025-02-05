#include "contiki.h"
#include <stdio.h>
#define MAX_NR_NODES 40
#define EXP_DESCRIPTOR_PASSWORD 0xBEEFBEEF

typedef struct OrderMsg {
  uint8_t order;			// the order depend on the value of the integer 1 is a sync order
  uint8_t nbNode;
} OrderMsg;

typedef struct CountIdOrder {
  uint8_t biggestId ;
  uint8_t counter ;
} CountIdOrder;

typedef struct Datastruct {
	uint8_t identificator;
	uint8_t number;
	uint8_t id;
} Datastruct;

typedef struct RoundStartMsg {
	uint8_t type;			// among the above dissemination enum
  uint32_t config_id; 	// configuration id
  uint16_t run_id;		// unique (random) number to distinguish runs
  uint16_t round_seqn; 	// round sequence number
  uint16_t num_bursts;
  uint16_t burst_size;
  uint16_t timeslot;
  uint16_t env_log_interval; // seconds
  uint16_t burst_imi;		// inter-packet interval in a burst
  uint8_t channel;
  uint8_t power;
  uint8_t flags;
  uint8_t senders  [ (MAX_NR_NODES-1)/8 + 1 ];
  uint8_t listeners[ (MAX_NR_NODES-1)/8 + 1 ];
} RoundStartMsg;

typedef struct ExpDescriptor {
	uint32_t password;	  // should contain the valid password
	uint32_t config_id;
	uint16_t run_id;
	uint16_t num_rounds;
	uint16_t repetitions;
	uint8_t  go_lpl; // bool
} ExpDescriptor;

