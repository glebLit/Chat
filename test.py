#!/usr/bin/env python
import unittest
import urllib2
import os
import threading
import subprocess
from flask import Flask
app = Flask(__name__)
class FlaskTests(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True
		

	def test_home_status_code(self):
		p = subprocess.Popen('python chat.py', shell = True)
		result = urllib2.urlopen("http://localhost:5000/")
		#print result.code
		self.assertEqual(result.code,200)
		p.kill()
		

	def setDown(self):
		pass
		
if __name__== '__main__':
	unittest.main()			
