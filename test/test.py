#!/usr/bin/env python
import unittest
import urllib2
import time
from flask import Flask
from flask_socketio import SocketIO, emit
from socketIO_client import SocketIO
from socketio import packet
import socketio
 
app = Flask(__name__)
class FlaskTests(unittest.TestCase):
    global result
    result = urllib2.urlopen("http://localhost:5000/")
    def setUp(self):
        
        self.app = app.test_client()
        self.app.testing = True

       
    def test_home_status_code200(self):
        self.assertEqual(result.code,200)
    def test_home_status_code404(self):
        self.assertNotEqual(result.code, 404)
    def test_home_status_code500(self):
        self.assertNotEqual(result.code, 500)
    def test_home_status_code502(self):
        self.assertNotEqual(result.code, 502)
    def test_home_status_code524(self):
        self.assertNotEqual(result.code, 524)
    def test_headers(self):
    	self.assertEqual(int(result.info()['Content-Length']),3985)    

    def test_html (self):
    	result = urllib2.urlopen("http://localhost:5000/")
        self.assertEqual(result.read()[1:46], '!DOCTYPE html>\n<html lang="en">\n  <head>\n    ') 


       

    def test_send_msg(self):
    	def answer(msg):
    		print msg
    	socketIO = SocketIO('localhost', 5000)
    	
    	
    	socketIO.emit('my event', {'message': 'test', "user_name": 'test'})
    	pkt = packet.Packet()
    	self.assertEqual(pkt.packet_type, packet.EVENT)
    	self.assertTrue(socketIO.connected) 

    def test_connected(self):
    	socketIO = SocketIO('localhost', 5000)
    	self.assertTrue(socketIO.connected)

    def test_disconnectsd(self):
    	socketIO = SocketIO('localhost', 5000)
    	socketIO.disconnect()
        self.assertFalse(socketIO.connected)	
        
    def test_wait(self):
    	socketIO = SocketIO('localhost', 5000)
    	socketIO.emit('wait_with_disconnect')
        timeout_in_seconds = 5
        start_time = time.time()
        socketIO.wait(timeout_in_seconds)
        self.assertTrue(time.time() - start_time-1 < timeout_in_seconds)    




    def setDown(self):
        pass       
       
if __name__== '__main__':
    unittest.main()	
