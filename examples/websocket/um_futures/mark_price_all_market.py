#!/usr/bin/env python

import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = UMFuturesWebsocketClient(on_message=message_handler)

my_client.mark_price_all_market(
    id=13,
    speed=1,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
