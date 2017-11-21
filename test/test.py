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
		p = subprocess.Popen('python ../chat.py', shell = True)
		self.app = app.test_client()
		self.app.testing = True
		

	def test_home_status_code(self):
		result = urllib2.urlopen("http://localhost:5000/")
		self.assertEqual(result.code,200)
		
		

	def setDown(self):
		p.kill()
		
		
if __name__== '__main__':
	unittest.main()			
