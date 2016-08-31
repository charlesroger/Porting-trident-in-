#include "contiki.h"
#include <stdio.h>

#define PAYLOAD_LENGTH 98 // set the same in the Makefile (MSG_SIZE)
#define MAX_NR_NODES 40
#define GATEWAY 1000

typedef struct LogDownlData {
	uint8_t session_id;
	uint8_t seqn;
	uint32_t next_cookie;
} LogDownlData;

typedef struct OrderMsg {
  uint8_t order;			
} OrderMsg;

typedef struct DataMsg {
  uint8_t rssi;
  uint8_t lqi;
  uint8_t round;
  uint8_t initiatorNode;
} DataMsg;

typedef struct CountIdOrder {
  uint8_t biggestId ;
  uint8_t counter ;
} CountIdOrder;

/////////////////////////////Structures for download/////////////////////////////////////////////////

typedef struct LogRecordStatsDownload {
  uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
	uint16_t avgTemperature;
  uint16_t avgHumidity;
  uint16_t initBattery;
  uint16_t endBattery;
  uint16_t rx_packets[MAX_NR_NODES];
  uint8_t rx_rssi[MAX_NR_NODES];
  uint8_t rx_lqi[MAX_NR_NODES];
  uint8_t rx_noise[MAX_NR_NODES];
	uint8_t target_id = GATEWAY;
} LogRecordStats;

typedef struct LogRecordStatsDownload {
  uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
  uint16_t avgTemperature;
  uint16_t avgHumidity;
  uint16_t initBattery;
  uint16_t endBattery;
  uint16_t rx_packets[MAX_NR_NODES];
  uint8_t rx_rssi[MAX_NR_NODES];
  uint8_t rx_lqi[MAX_NR_NODES];
  uint8_t rx_noise[MAX_NR_NODES];
	uint8_t GATEWAY;
} LogRecordStats;

typedef struct LogRecordNewExpDownload{
	uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
	uint8_t  marker[8]; // = "TRIDENT\0" for "synchronisation" in case of error
	uint32_t config_id; 
	uint16_t run_id;
	uint16_t round_seqn;
	uint8_t node_id;
	uint8_t GATEWAY;
} LogRecordNewExp;


typedef struct LogRecordRxDownload{
	uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
	uint8_t node_id;
	uint8_t noise;
	uint16_t msg_seqn;
	uint8_t rssi;
	uint8_t lqi;
	uint8_t GATEWAY;
} LogRecordRx;

typedef struct LogRecordRxErrorDownload{
	uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
	uint8_t node_id;
	uint16_t msg_seqn;
	uint8_t rssi;
	uint8_t lqi;
	uint8_t trident_status;
	uint8_t GATEWAY;
} LogRecordRxError;

typedef struct LogRecordTxDownload{
	uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
	uint8_t noise;
	uint16_t msg_seqn;
	uint8_t GATEWAY;
} LogRecordTx;

typedef struct LogRecordTxErrorDownload{
	uint8_t record_type;
	uint8_t seqn;
	uint8_t volume_id;
	uint8_t session_id;
	uint16_t msg_seqn;
	uint8_t trident_status;
	uint8_t tos_status;
	uint8_t GATEWAY;
} LogRecordTxError;


////////////////////////////////////Structure for reading///////////////////////////////////////////

typedef struct LogRecordStats {
  uint8_t record_type;
  uint16_t avgTemperature;
  uint16_t avgHumidity;
  uint16_t initBattery;
  uint16_t endBattery;
  uint16_t rx_packets[MAX_NR_NODES];
  uint8_t rx_rssi[MAX_NR_NODES];
  uint8_t rx_lqi[MAX_NR_NODES];
  uint8_t rx_noise[MAX_NR_NODES];
} LogRecordStats;

typedef struct LogRecordNewExp{
	uint8_t record_type;
	uint8_t  marker[8]; // = "TRIDENT\0" for "synchronisation" in case of error
	uint32_t config_id; 
	uint16_t run_id;
	uint16_t round_seqn;
	uint8_t node_id;
} LogRecordNewExp;


typedef struct LogRecordRx{
	uint8_t record_type;
	uint8_t node_id;
	uint8_t noise;
	uint16_t msg_seqn;
	uint8_t rssi;
	uint8_t lqi;
} LogRecordRx;

typedef struct LogRecordRxError{
	uint8_t record_type;
	uint8_t node_id;
	uint16_t msg_seqn;
	uint8_t rssi;
	uint8_t lqi;
	uint8_t trident_status;
} LogRecordRxError;

typedef struct LogRecordTx{
	uint8_t record_type;
	uint8_t noise;
	uint16_t msg_seqn;
} LogRecordTx;

typedef struct LogRecordTxError{
	uint8_t record_type;
	uint16_t msg_seqn;
	uint8_t trident_status;
	uint8_t tos_status;
} LogRecordTxError;

typedef nx_struct LogDownlReq {
	nx_uint8_t session_id;
	nx_uint8_t volume_id;
	nx_uint32_t start_cookie;
	nx_uint8_t max_packets;
	nx_uint8_t data_size;
} LogDownlReq;

