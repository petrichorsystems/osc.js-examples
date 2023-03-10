#! /usr/bin/python3

import liblo
from liblo import *
import queue, sys, time

responses = queue.Queue()

class OscServer(ServerThread):
    def __init__(self):
        ServerThread.__init__(self, 7500)
        
    @make_method('/cyperus/address', 'ss')
    def osc_address_handler(self, path, args):
        s = args
        responses.put(s)
        print("received '/cyperus/address'")

    @make_method(None, None)
    def fallback(self, path, args):
        print("fallback, received '{}'".format(path))
        
def test_single_channel_single_bus_sine_follower_delay(dest):
    liblo.send(dest, "/test", 44, 11, 4.5, "the white cliffs of dover")

    # response = responses.get()
    # print('/cyperus/address: ', response)

if __name__ == '__main__':
    #outgoing connection
    dest = liblo.Address('127.0.0.1', 7400)

    #incoming server
    # server = OscServer()

    # server.start()

    test_single_channel_single_bus_sine_follower_delay(dest)

    input("press enter to quit...\n")
