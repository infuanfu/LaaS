#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Example program to receive packets from the radio
#
# João Paulo Barraca <jpbarraca@gmail.com>
#
from nrf24 import NRF24, GPIO
import time
from datetime import datetime
import sys


pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

radio = NRF24()
radio.begin(0, 0, 25, 27)

radio.setRetries(1,1)

radio.setPayloadSize(24)
radio.setChannel(0x60)
radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(1)

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])

radio.startListening()
radio.stopListening()

#radio.printDetails()

radio.startListening()

time.sleep(2)

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)

    recv_buffer = []
    radio.read(recv_buffer)
    

    #print "[{}] {}".format(datetime.now().isoformat(' '), recv_buffer[0])
    print "{}".format(recv_buffer[0])

    sys.stdout.flush()
