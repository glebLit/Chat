#!/usr/bin/env python
import unittest
import urllib2
import time
from flask import Flask
from flask_socketio import SocketIO, emit
from socketIO_client import SocketIO, LoggingNamespace
from socketio import packet
import socket
 
app = Flask(__name__)
class FlaskTests(unittest.TestCase):
    global result
    result = urllib2.urlopen("http://localhost:5000/")
    def setUp(self):
        
        self.app = app.test_client()
        self.app.testing = True

       
    def test_home_status_code200(self):
        self.assertEqual(result.code,200)
     

    def test_html (self):
    	result = urllib2.urlopen("http://localhost:5000/")
        self.assertEqual(result.read()[1:46], '!DOCTYPE html>\n<html lang="en">\n  <head>\n    ') 


       

    def test_send_msg(self):
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

    def test_recieve_msg(self):
    	global msg
    	def on_aaa_response(*args):
    		global msg 
    		msg = args[0]
    	def on_connect():
    		print('connect')	

    	socketIO = SocketIO('localhost', 5000)
    	socketIO.on('connect', on_connect)
    	socketIO.on('my response', on_aaa_response)
    	socketIO.emit('my event', {'message': 'test', "user_name": 'test'})
    	socketIO.wait(seconds=1)
    	self.assertEqual(msg, {u'message': u'test', u'user_name': u'test'})

    def test_delete_client(self):
    	global msg
    	def on_aaa_response(*args):
    		global msg 
    		msg = args[0]
    	def on_connect():
    		print('connect')	

    	socketIO = SocketIO('localhost', 5000)
    	socketIO.on('connect', on_connect)
    	socketIO.on('my response', on_aaa_response)
    	socketIO.emit('my event', {'data': u'Anonimus Disconnected'})
    	socketIO.wait(seconds=1)
    	self.assertEqual(msg, {u'message': u'Anonimus left chat room', u'user_name': u'server'})

    def test_new_client(self):
    	global msg
    	def on_aaa_response(*args):
    		global msg 
    		msg = args[0]
    	def on_connect():
    		print('connect')	

    	socketIO = SocketIO('localhost', 5000)
    	socketIO.on('connect', on_connect)
    	socketIO.on('my response', on_aaa_response)
    	socketIO.emit('my event', {u'data': u'User Connected'})
    	socketIO.wait(seconds=1)	
    	self.assertEqual(msg, {u'message': u'One more user!', u'user_name': u'server'})

    def setDown(self):
        pass       
       
if __name__== '__main__':
    unittest.main()	
